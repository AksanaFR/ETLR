# SPDX-License-Identifier: MIT
"""ETLR-MO-02: protótipo finito do motor contextual; circulação privada.

Implementação original para ensaio metodológico. Não implementa integralmente
ETLR Volume I nem demonstra autopoiese, consciência ou autogeração universal.
"""
from .motor import (CORE, Rule, Context, Question, Trace, State, new_state,
                    step, run, change_field, replicate, refract, audit,
                    require_ready, MissingCondition, valid_witness, summarize)
__all__ = ['CORE','Rule','Context','Question','Trace','State','new_state',
           'step','run','change_field','replicate','refract','audit',
           'require_ready','MissingCondition','valid_witness','summarize']