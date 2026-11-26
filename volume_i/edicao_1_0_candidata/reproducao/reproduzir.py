"""Reexecuta somente os controles científicos selecionados, sem rede ou motores."""
from pathlib import Path
import subprocess, sys, tempfile, shutil, json, hashlib, platform

O=Path(__file__).resolve().parent
cases=[('VI02','VI02_codigo_original.py','VI02_expected_original.json',[]),
       ('VI03','VI03_codigo_original.py','VI03_expected_original.json',['tempo_segundos']),
       ('VI05','controles_complementares.py','CONTROLES_COMPLEMENTARES.json',['tempo_segundos'])]

def main():
    dest=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(tempfile.mkdtemp(prefix='etlr_controles_'))
    if dest==O or O in dest.parents:
        raise SystemExit('Escolha um diretório de saída fora do pacote editorial.')
    dest.mkdir(parents=True,exist_ok=True)
    reports=[]
    for tag,code,expected,ignore in cases:
        with tempfile.TemporaryDirectory(prefix='etlr_exec_') as td:
            p=Path(td)/code;shutil.copyfile(O/code,p)
            r=subprocess.run([sys.executable,'-X','utf8',str(p)],cwd=td,capture_output=True,timeout=300)
        (dest/(tag+'.stdout.json')).write_bytes(r.stdout)
        (dest/(tag+'.stderr.txt')).write_bytes(r.stderr)
        actual=json.loads(r.stdout);reference=json.loads((O/expected).read_text(encoding='utf-8-sig'))
        for data in (actual,reference):
            for key in ignore:data.pop(key,None)
        reports.append(dict(id=tag,codigo=code,sha256_codigo=hashlib.sha256((O/code).read_bytes()).hexdigest(),returncode=r.returncode,stderr_vazio=not r.stderr,igualdade_semantica=actual==reference,campos_excluidos=ignore))
    report=dict(python=platform.python_version(),controles=reports,aprovado=all(c['returncode']==0 and c['stderr_vazio'] and c['igualdade_semantica'] for c in reports),limite='Controles sintéticos delimitados; sem validação empírica, motores, prova mecanizada ou execução de todas as suítes históricas.')
    (dest/'REPRODUCAO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if not report['aprovado']:raise SystemExit(1)

if __name__=='__main__':main()
