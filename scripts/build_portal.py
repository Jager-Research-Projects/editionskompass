"""Rebuild native pages, imported full applications, catalog and reading materials."""
from pathlib import Path
import subprocess,sys
R=Path(__file__).resolve().parents[1]
for name in ['integrate_module.py','build.py','integrate_module.py','prune_delivery.py','wissensmaterial.py']:
 subprocess.run([sys.executable,str(R/'scripts'/name)],cwd=R,check=True)

if (R/'inhalte/uebersetzung/en.json').exists():
 for name in ['build_english_map.py','complete_english_knowledge.py','build.py','integrate_module.py','prune_delivery.py','build_english.py','apply_english_art.py','wissensmaterial.py']:
  subprocess.run([sys.executable,str(R/'scripts'/name)],cwd=R,check=True)

subprocess.run([sys.executable,str(R/'scripts/build_databases.py')],cwd=R,check=True)
subprocess.run([sys.executable,str(R/'scripts/build_workshop.py')],cwd=R,check=True)

subprocess.run([sys.executable,str(R/'scripts/finalize_publication.py')],cwd=R,check=True)
