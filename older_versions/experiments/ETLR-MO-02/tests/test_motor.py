# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
"""Regressões reproduzíveis e controles negativos ETLR-MO-02."""
import unittest
from dataclasses import replace
from itertools import combinations
from etlr_contextual.motor import (CORE, Context, Question, State, Trace, Rule,
  MissingCondition, RECIPES, new_state, audit, step, run, change_field,
  replicate, refract, require_ready, fingerprint)

WITNESS = dict(constitution=True,boundary=True,identity=True,
               continuity=True,participation=True)


def resolved(fuel=12):
    return run(new_state(fuel=fuel))[0]


class ETLRMotorTests(unittest.TestCase):
    def test_t1_simple_relation_and_local_fixed_point(self):
        o, tr=run(new_state(limit=12,observed=7))
        self.assertEqual(len(tr),1)
        self.assertEqual(o.status,'LOCAL_CLOSED')
        self.assertIn('ADMISSIBLE',o.conclusions[0])
        self.assertEqual(step(o),o)

    def test_t2_three_undetermined_branches(self):
        o,tr=run(new_state(limit=None,observed=4,question='WHY_SHORT'))
        self.assertEqual(len(tr),4)
        self.assertEqual(len(o.branches),3)
        self.assertEqual(o.status,'PENDING_EVIDENCE')
        self.assertTrue(all(b.endswith('UNDETERMINED') for b in o.branches))
        self.assertEqual(step(o),o)

    def test_t3_field_event_provenance_and_reentry(self):
        a,tr1=run(new_state(limit=7,observed=7))
        b,tr2=run(change_field(a,'evt_001','canal',12,9))
        self.assertEqual((len(tr1),len(tr2)),(1,1))
        self.assertEqual(b.context.revision,1)
        self.assertEqual(len(b.conclusions),2)
        self.assertTrue(b.conclusions[0].startswith('ADMISSIBLE@rev0'))
        self.assertTrue(b.conclusions[1].startswith('ADMISSIBLE@rev1'))
        self.assertTrue(audit(b))
        self.assertEqual(b.history[:len(a.history)],a.history)

    def test_n1_missing_domain_rejected(self):
        s=new_state();s=replace(s,context=replace(s.context,space=''))
        with self.assertRaises(MissingCondition):step(s)

    def test_n2_incompatible_event_domain_rejected(self):
        with self.assertRaisesRegex(MissingCondition,'CONTEXT_MISMATCH'):
            change_field(resolved(),'e','incompatível',5,4)

    def test_n3_duplicate_event_rejected(self):
        s=change_field(resolved(),'e','canal',5,4)
        with self.assertRaisesRegex(MissingCondition,'DUPLICATE'):
            change_field(s,'e','canal',8,4)

    def test_n4_unknown_limit_indeterminate(self):
        o,_=run(new_state(limit=None,question='CHECK'))
        self.assertIn('INDETERMINATE',o.conclusions[0])

    def test_n5_tampered_record_rejected(self):
        s=resolved()
        first=replace(s.history[0],data='MANIPULADO')
        bad=replace(s,history=(first,)+s.history[1:])
        self.assertFalse(audit(bad))
        with self.assertRaisesRegex(MissingCondition,'BROKEN_PROVENANCE'):
            step(bad)

    def test_n6_unknown_question_rejected(self):
        s=new_state(question='DO_THE_IMPOSSIBLE')
        with self.assertRaisesRegex(MissingCondition,'UNKNOWN_QUESTION'):
            step(s)

    def test_repair_single_loss_and_resume(self):
        parent=new_state(fuel=4)
        impaired=replace(parent,parts=CORE-{'CONFRONT'})
        repaired=step(impaired)
        self.assertEqual(repaired.parts,CORE)
        self.assertEqual(repaired.fuel,3)
        self.assertEqual(repaired.history[-1].action,'REPAIR')
        out,trace=run(repaired)
        self.assertEqual(out.status,'LOCAL_CLOSED')
        self.assertEqual(len(trace),1)
        self.assertTrue(audit(out))

    def test_repair_is_one_atomic_step(self):
        initial=replace(new_state(fuel=4),parts=CORE-{'CONFRONT'})
        intermediate=step(initial)
        self.assertFalse(intermediate.conclusions)
        final=step(intermediate)
        self.assertEqual(len(final.conclusions),1)

    def test_no_fuel_blocks_repair(self):
        s=replace(new_state(fuel=0),parts=CORE-{'CONFRONT'})
        o,trace=run(s)
        self.assertEqual(o.status,'BLOCKED')
        self.assertFalse(require_ready(o))
        self.assertEqual(step(o),o)

    def test_missing_recipe_blocks_repair(self):
        s=replace(new_state(fuel=6),parts=CORE-{'CONFRONT'},
                  recipes=tuple(r for r in RECIPES if r.target != 'CONFRONT'))
        out,_=run(s)
        self.assertEqual(out.status,'BLOCKED')

    def test_two_missing_parts_cannot_repair(self):
        s=replace(new_state(fuel=6),parts=frozenset({'CONSTITUTE'}))
        out,_=run(s)
        self.assertEqual(out.status,'BLOCKED')

    def test_self_copy_independent_child_same_motor(self):
        p=resolved(12)
        newctx=Context('outra_escala','ciclo_1','G_1',9)
        donor,child=replicate(p,newctx,WITNESS,fuel_transfer=3,observation=7)
        self.assertEqual(donor.fuel,6)
        self.assertEqual(child.fuel,3)
        self.assertEqual(p.fuel,12)
        self.assertEqual(child.parts,p.parts)
        self.assertEqual(child.recipes,p.recipes)
        self.assertEqual(child.ancestor,fingerprint(p))
        self.assertEqual(child.generation,1)
        o,_=run(child)
        self.assertEqual(o.status,'LOCAL_CLOSED')
        self.assertIn('ADMISSIBLE',o.conclusions[0])
        self.assertEqual(p.context.space,'canal')
        self.assertTrue(audit(o) and audit(donor))

    def test_two_generation_functional_copy(self):
        p=resolved(12)
        donor1, child=replicate(p,Context('S1','F1','G1',10),WITNESS,
                                fuel_transfer=3)
        closedchild,_=run(child)
        donor2, grandchild=replicate(closedchild,Context('S2','F2','G2',8),
                                     WITNESS,fuel_transfer=0)
        g,_=run(grandchild)
        self.assertEqual(g.generation,2)
        self.assertEqual(g.status,'LOCAL_CLOSED')
        self.assertEqual(donor2.fuel,0)
        self.assertEqual(grandchild.fuel,0)
        self.assertTrue(audit(g))

    def test_resource_conservation_in_copy(self):
        p=resolved(9)
        a,b=replicate(p,Context('X','Y','Z',12),WITNESS,
                      fuel_transfer=4)
        self.assertEqual(a.fuel+b.fuel+len(CORE),p.fuel)

    def test_insufficient_resource_copy_rejected(self):
        p=resolved(2)
        with self.assertRaisesRegex(MissingCondition,'INSUFFICIENT_FUEL'):
            replicate(p,Context('S','H','B',12),WITNESS)

    def test_witness_failure_blocks_reentry(self):
        w=dict(WITNESS,continuity=False)
        with self.assertRaisesRegex(MissingCondition,'UNSUPPORTED_INDIVIDUATION'):
            refract(resolved(),Context('S','T','B',12),w)

    def test_witness_failure_blocks_copy(self):
        w=dict(WITNESS,boundary=False)
        with self.assertRaisesRegex(MissingCondition,'UNSUPPORTED_INDIVIDUATION'):
            replicate(resolved(),Context('S','T','B',12),w)

    def test_stalled_parent_cannot_replicate(self):
        p,_=run(new_state(question='WHY_SHORT'))
        with self.assertRaisesRegex(MissingCondition,'PARENT_NOT_RESOLVED'):
            replicate(p,Context('S','T','B',12),WITNESS)

    def test_unknown_core_cannot_replicate(self):
        p=replace(resolved(),parts=CORE-{'CONSTITUTE'})
        with self.assertRaisesRegex(MissingCondition,'PARENT_FUNCTIONAL_CORE_INCOMPLETE'):
            replicate(p,Context('S','T','B',12),WITNESS)

    def test_loss_of_interpreter_not_repaired(self):
        # Ensaio de limite: não há representação/operador para reconstituir
        # código-fonte Python dentro de State; portanto nenhuma prova disso.
        self.assertFalse(hasattr(resolved(),'interpreter_source'))
        self.assertFalse(any(r.target=='PYTHON_RUNTIME' for r in RECIPES))

    def test_exhaustive_finite_80_configurations(self):
        # 8 máscaras de componentes x 5 orçamentos x 2 regimes de receitas
        checked=0
        names=sorted(CORE)
        for mask in range(8):
            parts=frozenset(x for i,x in enumerate(names) if mask & (1<<i))
            missing=CORE-parts
            for fuel in range(5):
                for recipes_present in (False, True):
                    s=replace(new_state(fuel=fuel),parts=parts,
                              recipes=RECIPES if recipes_present else ())
                    o=step(s)
                    possible=(len(missing)==1 and fuel>=1 and recipes_present)
                    if len(missing)==0:
                        self.assertTrue(require_ready(o))
                    elif possible:
                        self.assertEqual(o.parts,CORE)
                        self.assertEqual(o.fuel,fuel-1)
                        self.assertEqual(o.history[-1].action,'REPAIR')
                    else:
                        self.assertEqual(o.status,'BLOCKED')
                    self.assertTrue(audit(o))
                    checked+=1
        self.assertEqual(checked,80)

    def test_multi_level_requires_individualization_witness(self):
        root=resolved(20)
        levels=[]
        for n in range(1,4):
            root=refract(root,Context(f'escala_{n}',f'evento_{n}',f'G_{n}',12),
                         WITNESS,fuel=3)
            root,_=run(root)
            levels.append((root.generation,root.context.space,audit(root)))
        self.assertEqual([x[0] for x in levels],[1,2,3])
        self.assertTrue(all(x[2] for x in levels))

    def test_partial_recovery_not_claimed_to_be_total(self):
        all_lost=replace(new_state(),parts=frozenset())
        out,_=run(all_lost)
        self.assertEqual(out.status,'BLOCKED')
        self.assertFalse(require_ready(out))

    def test_stopped_system_does_not_spawn_branches(self):
        o,_=run(new_state())
        o2=step(o)
        self.assertEqual(o2,o)
        self.assertEqual(o2.branches,())


if __name__=='__main__':
    unittest.main(verbosity=2)

class ETLRLanguageTests(unittest.TestCase):
    def test_language_sample_simple(self):
        from etlr_contextual.language import execute
        src='''ESPACO canal\nCAMPO turnos\nINDIVIDUO A\nLIMITE 12\nOBSERVADO 7\nPERGUNTA CHECK\nRECURSO 6'''
        out,trace=execute(src)
        self.assertEqual(out.status,'LOCAL_CLOSED')
        self.assertEqual(len(trace),1)

    def test_language_ambiguous_branch(self):
        from etlr_contextual.language import execute
        src='''ESPACO canal\nCAMPO turnos\nINDIVIDUO A\nLIMITE DESCONHECIDO\nOBSERVADO 4\nPERGUNTA WHY_SHORT\nRECURSO 6'''
        out,trace=execute(src)
        self.assertEqual(len(out.branches),3)
        self.assertEqual(len(trace),4)

    def test_language_rejects_duplicate_fields(self):
        from etlr_contextual.language import parse
        with self.assertRaisesRegex(MissingCondition,'DUPLICADO'):
            parse('ESPACO a\nESPACO b')

    def test_language_rejects_extra_commands(self):
        from etlr_contextual.language import parse
        with self.assertRaisesRegex(MissingCondition,'DESCONHECIDO'):
            parse('EXECUTAR python')