from pathlib import Path
import sys,json
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'inhalte'))
from ausbau import W
for lang in ['de','en']:
 de=lang=='de';parts=['# '+('Git-Wissen kompakt' if de else 'Compact Git knowledge'),'83 '+('Aussagen' if de else 'statements')+' · 25 Antipatterns · 24 '+('Begriffe' if de else 'terms'),'## '+('Mythos und Fakt' if de else 'Myth and fact')]
 for n in W['nodes']:
  x=n if de else n['en'];parts+=['### '+n['id']+' · '+(('Irrtum' if de else 'Myth') if n['kind']=='M' else ('Fakt' if de else 'Fact'))+' · '+x.get('claim',x['title']),x.get('detail') or ' '.join(x.get(k,'') for k in ['surprise','utility','limits'])]
 parts+=['## Antipatterns']
 for c in W['academy'][lang]['cards']:
  parts+=['### '+c['code']+' · '+c['title'],('Muster: ' if de else 'Pattern: ')+c['bad'],('Besser: ' if de else 'Better: ')+c['good'],('Geltungsgrenze: ' if de else 'Boundary: ')+c['boundary']]
 parts+=['## '+('Begriffe' if de else 'Terms')]
 for g in W['glossary']:
  x=g if de else g['en'];parts+=['### '+x['term'],x['description']]
 parts+=['Editionskompass · 27.10.2026','Quellen / Sources: Git-Entdeckungsreise; Git Antipattern Academy.']
 (R/f'dist/assets/wissen-{lang}.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
p=R/'dist/assets/provenienz.json';d=json.loads(p.read_text(encoding='utf-8'))
for file,source in [('korpus.png','raetselkorpus-prototyp/dist/assets/seminar.png'),('drittmittel.png','die-andere-stadt-prototyp/dist/assets/team.png')]:
 if not any(x['file']==file for x in d['illustrations']):d['illustrations'].append({'file':file,'source':source,'type':'AI-generated illustration, reused from existing prototype'})
d['learningCollections']={'statements':83,'antipatterns':25,'terms':24,'sources':W['sources']}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
