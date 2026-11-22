# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
"""Uso: python -m etlr_contextual exemplos/01_simples.etlr"""
import sys,json
from pathlib import Path
from .language import execute
from .motor import summarize

def main():
    if len(sys.argv) != 2:
        print('Uso: python -m etlr_contextual <arquivo.etlr>', file=sys.stderr)
        return 2
    try:
        s, trace=execute(Path(sys.argv[1]).read_text(encoding='utf-8'))
        print(json.dumps({'steps':len(trace), **summarize(s)},
                          ensure_ascii=False,indent=2))
        return 0
    except (ValueError,OSError) as err:
        print(str(err),file=sys.stderr)
        return 1
if __name__=='__main__':
    raise SystemExit(main())