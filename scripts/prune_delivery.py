"""Remove only superseded, hash-verified PNG delivery copies after a rebuild."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];D=R/'dist';mfile=R/'inhalte/webmedien-manifest.json'
if not mfile.exists():raise SystemExit(0)
mods=json.loads((R/'inhalte/module-manifest.json').read_text(encoding='utf-8'));count=0
for m in json.loads(mfile.read_text(encoding='utf-8')):
 rel=Path(m['original']).relative_to('inhalte/module');key=rel.parts[0];tail=Path(*rel.parts[1:])
 bases=[D/x['route'].strip('/') for x in mods if x['id']==key]
 if key=='academy':bases=[D/'de/git-verstehen/antipatterns',D/'en/understanding-git/antipatterns']
 for base in bases:
  p=base/tail
  if p.exists():
   assert p.resolve().is_relative_to(D.resolve());assert hashlib.sha256(p.read_bytes()).hexdigest()==m['originalSHA256'];p.unlink();count+=1
print('Removed superseded delivery PNGs:',count)
