"""Confere o manifesto editorial SHA-256 usando somente a biblioteca padrão."""
from pathlib import Path, PurePosixPath
import hashlib
R=Path(__file__).resolve().parent.parent
errors=[];count=0
for line in (R/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
    expected,name=line.split('  ',1)
    rel=PurePosixPath(name)
    if rel.is_absolute() or '..' in rel.parts or ':' in name:
        errors.append('Caminho inseguro no manifesto');continue
    p=R.joinpath(*rel.parts);count+=1
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:
        errors.append(name)
print(f'{count} arquivos conferidos; {len(errors)} divergências.')
if errors:print('\n'.join(errors));raise SystemExit(1)
