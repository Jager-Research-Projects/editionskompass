from pathlib import Path
import json,shutil,sys
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'inhalte'))
from integration import MODULES
D=R/'dist';B=R/'inhalte/uebersetzung';catalog=json.loads((R/'inhalte/materialkatalog-en.json').read_text(encoding='utf-8'))
for key in ['emre','christine','dorothee','agenten']:
 m=next(m for m in MODULES if m['id']==key);route='/en/perspectives/'+key+'/full/';dest=D/route.strip('/');source=B/'bilder'/f'{key}-workshop-en-v1.png';assert source.exists()
 rel='assets/'+source.name;shutil.copy2(source,dest/rel)
 item=next(x for x in catalog if x['module']==key and 'PNG' in x['formats']);old=Path(item['formats']['PNG']).name;item['formats']['PNG']=route+rel;item['title']={'emre':'Workshop overview · Emre Kaya','christine':'Workshop overview · Christine Fühlhaber','dorothee':'Workshop overview · Dorothée Meisner','agenten':'Workshop overview · Nora and the agent'}[key]
 for p in dest.rglob('*'):
  if p.suffix in ['.html','.js','.json','.md']:
   text=p.read_text(encoding='utf-8');new=text.replace(old,source.name)
   if new!=text:p.write_text(new,encoding='utf-8')
(R/'inhalte/materialkatalog-en.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf-8')
cache=B/'pdf'
for item in catalog:
 if 'PDF' not in item['formats']:continue
 rel=Path(item['formats']['PDF'].removeprefix('/en/'));pdf=cache/rel
 if pdf.exists():shutil.copy2(pdf,D/'en'/rel)
print('English illustrated workshop cards installed; cached English PDFs restored.')
for source in (B/'png').rglob('*.png'):
 target=D/'en'/source.relative_to(B/'png');target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
