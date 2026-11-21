"""Executa suíte, grava resultados e resumo verificável em UTF-8 JSON."""
from pathlib import Path
import unittest, json, hashlib, time, sys, io
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root))
suite=unittest.defaultTestLoader.discover(str(root/'tests'),pattern='test_*.py',top_level_dir=str(root))
stream=io.StringIO()
result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
logs=stream.getvalue()
(root/'TESTES_EXECUCAO.txt').write_text(logs,encoding='utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={
    'protocol':'ETLR-MO-02 / motor contextual; modelagem sintética',
    'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
    'skipped':len(result.skipped),'successful':result.wasSuccessful(),
    'finite_configurations_in_one_test':80,
    'test_source_sha256':sha(root/'tests'/'test_motor.py'),
    'engine_sha256':sha(root/'etlr_contextual'/'motor.py'),
    'limits':['testes finitos e sintéticos','interpretador Python externo',
              'condições iniciais/receitas fornecidas','não demonstra autopoiese ou autogeração universal',
              'testemunho de individuação fornecido como hipótese'],
}
(root/'RESULTADOS.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(logs)
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(0 if result.wasSuccessful() else 1)