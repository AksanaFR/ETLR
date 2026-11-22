# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
"""Execução verificável de reparo, clonagem e falha deliberada."""
import json
from dataclasses import replace
from etlr_contextual import (CORE, Context, new_state, step, run,
                             replicate, summarize, MissingCondition)
W = {'constitution':True,'boundary':True,'identity':True,
     'continuity':True,'participation':True}

def show(label,s):
    print(label, json.dumps(summarize(s),ensure_ascii=False,sort_keys=True))

s = new_state(fuel=12)
impaired = replace(s,parts=CORE-{'CONFRONT'})
show('01 perde um componente:',impaired)
restored = step(impaired)
show('02 reconstitui com dois componentes + receita + recurso:',restored)
parent,_ = run(restored)
show('03 pai funcional:',parent)
donor,child = replicate(parent,Context('outra_escala','novo_regime','G1',9),W,
                        fuel_transfer=3)
show('04 pai após transferência:',donor)
child_done,_ = run(child)
show('05 filho funciona com mesma regra:',child_done)
try:
    replicate(child_done,Context('S2','T2','G2',8),W,fuel_transfer=3)
except MissingCondition as ex:
    print('06 reprodução sem recurso suficiente:',str(ex))