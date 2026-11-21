#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Motor contextual ETLR-MO-02, biblioteca Python padrão (sem dependências).

O microinterpretador em Python continua externo às entidades simuladas.
Consequentemente, restaurar componentes do *modelo* NÃO é restaurar o Python.

Fluxo único: situar -> confrontar -> reconstituir -> retornar; se faltar uma
função constitutiva, tentar recuperar uma única função antes do confronto.
"""
from __future__ import annotations
from dataclasses import dataclass, replace, asdict
from hashlib import sha256
import json
from typing import Optional, Iterable

CORE = frozenset({'CONSTITUTE', 'CONFRONT', 'RECONSTITUTE'})


class MissingCondition(ValueError):
    """O modelo não tem condições para a transição requerida."""


@dataclass(frozen=True)
class Rule:
    """Regra de reparação que é DADO do indivíduo, e não o interpretador.

    Cada par de componentes ainda íntegros pode reconstruir o terceiro,
    consumindo uma unidade de recurso. Nenhuma regra cria recurso.
    """
    target: str
    needs: frozenset[str]


RECIPES = (
    Rule('CONSTITUTE', frozenset({'CONFRONT', 'RECONSTITUTE'})),
    Rule('CONFRONT', frozenset({'CONSTITUTE', 'RECONSTITUTE'})),
    Rule('RECONSTITUTE', frozenset({'CONSTITUTE', 'CONFRONT'})),
)


@dataclass(frozen=True)
class Context:
    space: str  # K: domínio espacial-relacional de referência
    regime: str  # H: campo/regra temporal pertinente
    individual: str  # B: identificador *candidato*, não prova de individuação
    limit: Optional[int]
    revision: int = 0


@dataclass(frozen=True)
class Question:
    kind: str  # CHECK, WHY_SHORT, EXAMINE
    subject: str = ''


@dataclass(frozen=True)
class Trace:
    index: int
    action: str
    data: str
    parent_hash: str
    digest: str


def _canon(x):
    return json.dumps(x, sort_keys=True, ensure_ascii=False,
                      separators=(',', ':'))


def _hash(i, action, data, parent):
    return sha256(_canon([i, action, data, parent]).encode('utf-8')).hexdigest()


@dataclass(frozen=True)
class State:
    context: Context
    observed: int
    agenda: tuple[Question, ...]
    parts: frozenset[str] = CORE
    recipes: tuple[Rule, ...] = RECIPES
    fuel: int = 6  # recurso externo inicialmente disponibilizado
    history: tuple[Trace, ...] = ()
    conclusions: tuple[str, ...] = ()
    branches: tuple[str, ...] = ()
    event_ids: frozenset[str] = frozenset()
    status: str = 'ACTIVE'
    generation: int = 0
    ancestor: str = ''  # hash do estado pai; sem compartilhamento de estado vivo


def _log(s: State, action: str, data: str) -> State:
    prev = s.history[-1].digest if s.history else s.ancestor or 'GENESIS'
    n = len(s.history)
    record = Trace(n, action, data, prev, _hash(n, action, data, prev))
    return replace(s, history=s.history + (record,))


def audit(s: State) -> bool:
    """Verifica toda a cadeia local de proveniência, não a verdade dos dados."""
    prev = s.ancestor or 'GENESIS'
    for n, e in enumerate(s.history):
        if (e.index != n or e.parent_hash != prev or
                e.digest != _hash(n, e.action, e.data, e.parent_hash)):
            return False
        prev = e.digest
    return True


def fingerprint(s: State) -> str:
    """Hash do conteúdo completo do estado (para identificar ascendência)."""
    data = asdict(s)
    data['parts'] = sorted(s.parts)
    data['event_ids'] = sorted(s.event_ids)
    data['recipes'] = [{'target': r.target, 'needs': sorted(r.needs)}
                       for r in s.recipes]
    return sha256(_canon(data).encode('utf-8')).hexdigest()


def validate(s: State) -> None:
    c = s.context
    if not c.space or not c.regime or not c.individual:
        raise MissingCondition('MISSING_SITUATED_CONTEXT')
    if c.limit is not None and c.limit < 0:
        raise MissingCondition('INVALID_FIELD_LIMIT')
    if c.revision < 0 or s.observed < 0 or s.fuel < 0 or s.generation < 0:
        raise MissingCondition('INVALID_NONNEGATIVE_FIELD')
    if not s.parts.issubset(CORE):
        raise MissingCondition('UNKNOWN_COMPONENT')
    if any(r.target not in CORE or not r.needs.issubset(CORE)
           for r in s.recipes):
        raise MissingCondition('UNKNOWN_REPAIR_RULE')
    if not audit(s):
        raise MissingCondition('BROKEN_PROVENANCE')


def new_state(space: str = 'canal', regime: str = 'turnos',
              individual: str = 'A', limit: Optional[int] = 12,
              observed: int = 7, question: str = 'CHECK',
              fuel: int = 6) -> State:
    s = State(Context(space, regime, individual, limit), observed,
              (Question(question),), fuel=fuel)
    validate(s)
    return _log(s, 'CONSTITUTE', f'{space}|{regime}|{individual}|obs={observed}')


def require_ready(s: State) -> bool:
    return s.parts == CORE


def _repair(s: State) -> State:
    """Uma passagem de reparação local; preserva o orçamento e a história."""
    missing = CORE - s.parts
    if not missing:
        return s
    choices = [r for r in s.recipes
               if r.target in missing and r.needs.issubset(s.parts)]
    if not choices or s.fuel < 1:
        if s.status == 'BLOCKED':
            return s  # não girar indefinidamente sem nova condição
        return _log(replace(s, status='BLOCKED'), 'BLOCKED',
                    f"missing={','.join(sorted(missing))};fuel={s.fuel}")
    r = sorted(choices, key=lambda x: x.target)[0]
    out = replace(s, parts=s.parts | {r.target}, fuel=s.fuel - 1,
                  status='ACTIVE')
    return _log(out, 'REPAIR', f"target={r.target};requires={','.join(sorted(r.needs))}")


def _confront(s: State) -> State:
    """Uma única obrigação por passagem: não gera provas por associação."""
    if not s.agenda:
        return s
    q, rest = s.agenda[0], s.agenda[1:]
    c = s.context
    if q.kind == 'CHECK':
        if c.limit is None:
            verdict = f'INDETERMINATE@rev{c.revision}: limite desconhecido'
        else:
            truth = 'ADMISSIBLE' if s.observed <= c.limit else 'INCOMPATIBLE'
            verdict = f'{truth}@rev{c.revision}: observado={s.observed}, limite={c.limit}'
        result = replace(s, agenda=rest, conclusions=s.conclusions + (verdict,))
        return _log(result, 'CONFRONT', verdict)
    if q.kind == 'WHY_SHORT':
        # Operador de abertura de hipóteses EXPLICITAMENTE configurado para este domínio.
        # Não significa geração de todas as alternativas possíveis em outros domínios.
        alternatives = ('ENVIRONMENTAL_LIMIT', 'SELF_LIMITATION', 'RELATIONAL_LIMIT')
        new = tuple(Question('EXAMINE', a) for a in alternatives)
        result = replace(s, agenda=rest + new)
        return _log(result, 'BRANCH', '|'.join(alternatives))
    if q.kind == 'EXAMINE':
        branch = f'HIP-CIC:{q.subject}:UNDETERMINED'
        result = replace(s, agenda=rest, branches=s.branches + (branch,))
        return _log(result, 'BRANCH_EVAL', branch)
    raise MissingCondition('UNKNOWN_QUESTION')


def step(s: State) -> State:
    """Único operador de evolução: mesmo tipo de entrada/saída.

    Uma operação não substitui evidência ausente nem refaz regras perdidas.
    """
    validate(s)
    if not require_ready(s):
        return _repair(s)
    if not s.agenda:
        if s.status in ('LOCAL_CLOSED', 'PENDING_EVIDENCE'):
            return s
        return replace(s, status='PENDING_EVIDENCE' if s.branches else 'LOCAL_CLOSED')
    out = _confront(s)
    if not out.agenda:
        out = replace(out, status='PENDING_EVIDENCE' if out.branches else 'LOCAL_CLOSED')
    return out


def run(s: State, max_steps: int = 30) -> tuple[State, tuple[State, ...]]:
    if max_steps <= 0:
        raise ValueError('INVALID_STEP_BUDGET')
    trace = []
    for _ in range(max_steps):
        new = step(s)
        if new == s:
            return s, tuple(trace)
        trace.append(new)
        s = new
        if s.status in ('BLOCKED', 'LOCAL_CLOSED', 'PENDING_EVIDENCE') and not s.agenda:
            return s, tuple(trace)
    # orçamento é condição de segurança da investigação; não descarta agenda
    return replace(s, status='BUDGET_PAUSED'), tuple(trace)


def change_field(s: State, event_id: str, space: str,
                 new_limit: Optional[int], new_observation: int) -> State:
    validate(s)
    if space != s.context.space:
        raise MissingCondition('CONTEXT_MISMATCH')
    if not event_id or event_id in s.event_ids:
        raise MissingCondition('DUPLICATE_OR_EMPTY_EVENT')
    if (new_limit is not None and new_limit < 0) or new_observation < 0:
        raise MissingCondition('INVALID_FIELD_EVENT')
    c = replace(s.context, limit=new_limit, revision=s.context.revision + 1)
    out = replace(s, context=c, observed=new_observation,
                  event_ids=s.event_ids | {event_id},
                  agenda=s.agenda + (Question('CHECK'),), status='ACTIVE')
    return _log(out, 'FIELD_EVENT',
                f'{event_id}|rev={c.revision}|limit={new_limit}|obs={new_observation}')


def valid_witness(w: dict[str, bool]) -> bool:
    """Obrigações ETLR-09 apenas DEMARCADAS externamente, não demonstradas."""
    needed = ('constitution','boundary','identity','continuity','participation')
    return all(w.get(k) is True for k in needed)


def refract(parent: State, new_context: Context, witness: dict[str,bool],
            observation: Optional[int] = None, question: str = 'CHECK',
            fuel: int = 0) -> State:
    """Nova unidade candidata com critérios INDICADOS externamente."""
    validate(parent)
    if not valid_witness(witness):
        raise MissingCondition('UNSUPPORTED_INDIVIDUATION')
    if parent.status != 'LOCAL_CLOSED' or parent.agenda:
        raise MissingCondition('PARENT_NOT_RESOLVED')
    child = State(new_context, parent.observed if observation is None else observation,
                  (Question(question),), parts=parent.parts,
                  recipes=parent.recipes, fuel=fuel,
                  ancestor=fingerprint(parent), generation=parent.generation+1)
    validate(child)
    return _log(child, 'REFRACT',
                f'parent={child.ancestor}|witness=externo|gen={child.generation}')


def replicate(parent: State, new_context: Context, witness: dict[str,bool],
              fuel_transfer: int = 0, observation: Optional[int] = None) -> tuple[State,State]:
    """Reprodução FUNCIONAL *condicionada* de componentes e receitas.

    Para construir cópia dos três componentes, consome 3 recursos do pai;
    transfere adicionalmente fuel_transfer ao filho. O interpretador Python
    não é reproduzido. A testemunha de individuação continua externa.
    """
    validate(parent)
    if not require_ready(parent) or not all(any(r.target == k and r.needs == CORE - {k} for r in parent.recipes) for k in CORE):
        raise MissingCondition('PARENT_FUNCTIONAL_CORE_INCOMPLETE')
    if fuel_transfer < 0 or parent.fuel < len(CORE)+fuel_transfer:
        raise MissingCondition('INSUFFICIENT_FUEL_FOR_COPY')
    if not valid_witness(witness):
        raise MissingCondition('UNSUPPORTED_INDIVIDUATION')
    if parent.status != 'LOCAL_CLOSED' or parent.agenda:
        raise MissingCondition('PARENT_NOT_RESOLVED')
    donor = replace(parent, fuel=parent.fuel-len(CORE)-fuel_transfer)
    donor = _log(donor,'REPLICATION_DONOR',
                 f'child_context={new_context.space}|cost={len(CORE)}|transfer={fuel_transfer}')
    child = refract(parent, new_context, witness, observation=observation,
                    fuel=fuel_transfer)
    child = _log(child, 'REPLICATION_CHILD',
                 f'components={len(CORE)}|recipes={len(child.recipes)}|fuel={fuel_transfer}')
    return donor, child


def summarize(s: State) -> dict:
    return {'space':s.context.space, 'regime':s.context.regime,
            'individual':s.context.individual, 'rev':s.context.revision,
            'limit':s.context.limit,'observed':s.observed,
            'ready':require_ready(s),'fuel':s.fuel,
            'parts':sorted(s.parts),'recipe_count':len(s.recipes),
            'generation':s.generation,'status':s.status,
            'conclusions':list(s.conclusions),'branches':list(s.branches),
            'history_length':len(s.history),'history_valid':audit(s)}