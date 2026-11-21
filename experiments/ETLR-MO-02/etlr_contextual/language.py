"""ETLR-L0: linguagem declarativa mínima, sem avaliação de código externo.

Sete campos definem um experimento em um domínio; não determinam toda a
semântica da ETLR. O mecanismo de confronto é explícito em motor.py.
"""
from .motor import new_state, run, summarize, MissingCondition

NAMES = ('ESPACO','CAMPO','INDIVIDUO','LIMITE','OBSERVADO','PERGUNTA','RECURSO')


def parse(source: str):
    vals = {}
    for line_no, raw in enumerate(source.splitlines(),1):
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        pieces = line.split(None,1)
        if len(pieces)!=2 or pieces[0] not in NAMES:
            raise MissingCondition(f'LINHA_{line_no}:CAMPO_DESCONHECIDO')
        key,val=pieces
        if key in vals:
            raise MissingCondition(f'LINHA_{line_no}:CAMPO_DUPLICADO_{key}')
        if not val.strip():
            raise MissingCondition(f'LINHA_{line_no}:CAMPO_VAZIO_{key}')
        vals[key]=val.strip()
    if set(vals)!=set(NAMES):
        raise MissingCondition('CAMPOS_FALTANTES:'+','.join(sorted(set(NAMES)-set(vals))))
    try:
        limit = None if vals['LIMITE'].upper()=='DESCONHECIDO' else int(vals['LIMITE'])
        obs = int(vals['OBSERVADO'])
        fuel = int(vals['RECURSO'])
    except ValueError as e:
        raise MissingCondition('NUMERO_INVALIDO') from e
    if vals['PERGUNTA'] not in ('CHECK','WHY_SHORT'):
        raise MissingCondition('PERGUNTA_NAO_IMPLEMENTADA')
    return new_state(vals['ESPACO'],vals['CAMPO'],vals['INDIVIDUO'],limit,
                     obs,vals['PERGUNTA'],fuel)


def execute(source: str, max_steps: int=30):
    return run(parse(source),max_steps)