"""Build the portal, then export a GitHub Pages project-site artifact."""
from pathlib import Path
from urllib.parse import urlsplit
import argparse,subprocess,sys,json,shutil,re
from pypdf import PdfReader,PdfWriter
from pypdf.generic import NameObject,TextStringObject
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--skip-portal',action='store_true');args=p.parse_args()
cfg=json.loads((R/'publication.json').read_text(encoding='utf-8'));base=cfg['base_path'].rstrip('/');origin=cfg['origin'].rstrip('/');assert re.fullmatch(r'/[a-zA-Z0-9_-]+',base)
if not args.skip_portal:subprocess.run([sys.executable,str(R/'scripts/build_portal.py')],cwd=R,check=True)
out=R/'_site';out.mkdir(exist_ok=True)
assert out.resolve().parent==R.resolve()
# Only the generated deployment folder is cleared; editorial sources stay intact.
for child in out.iterdir():
 if child.is_dir():shutil.rmtree(child)
 else:child.unlink()
root_path=re.compile(r'(?<![A-Za-z0-9:/_.-])/(assets|de|en)/')
old_origin='https://editionskompass.tomsummer.chatgpt.site'
legacy={'https://anna-editionskompass.windy-anole-0248.chatgpt.site/':{'de':'/de/projekte/kleinprojekt/','en':'/en/projects/anna/full/'},'https://akademie-editionskompass.windy-anole-0248.chatgpt.site/':{'de':'/de/projekte/langzeitedition/','en':'/en/projects/albrecht/full/'}}
def text_urls(s,lang):
 s=s.replace(old_origin,base)
 for old,targets in legacy.items():s=s.replace(old,base+targets[lang])
 return root_path.sub(lambda m:base+'/'+m[1]+'/',s)
pdf_links=[]
def pdf_uri(uri,lang):
 for old,targets in legacy.items():
  if uri.startswith(old):return origin+base+targets[lang]+uri[len(old):]
 u=urlsplit(uri)
 if uri.startswith('/') and not uri.startswith('//') and re.match(r'^/(?:assets|de|en)/',uri):return origin+base+uri
 if u.netloc in ['127.0.0.1:8897','localhost:8897'] or uri.startswith(old_origin):
  if re.match(r'^/(?:assets|de|en)/',u.path):return origin+base+u.path+('?' +u.query if u.query else '')+('#'+u.fragment if u.fragment else '')
 return uri
for src in (R/'dist').rglob('*'):
 if not src.is_file():continue
 dst=out/src.relative_to(R/'dist');dst.parent.mkdir(parents=True,exist_ok=True)
 rel=src.relative_to(R/'dist');lang='en' if rel.parts[0]=='en' or src.stem.endswith('-en') else 'de'
 if src.suffix.lower() in ['.html','.css','.js','.json','.svg','.md','.txt','.xml']:
  try:dst.write_text(text_urls(src.read_text(encoding='utf-8-sig'),lang),encoding='utf-8')
  except UnicodeDecodeError:shutil.copy2(src,dst)
 elif src.suffix.lower()=='.pdf':
  reader=PdfReader(src);changes=[]
  for page in reader.pages:
   for ref in page.get('/Annots',[]):
    a=ref.get_object();action=a.get('/A')
    if action:
     action=action.get_object();uri=action.get('/URI')
     if uri:
      new=pdf_uri(str(uri),lang)
      if new!=str(uri):action[NameObject('/URI')]=TextStringObject(new);changes.append({'from':str(uri),'to':new})
  if changes:
   writer=PdfWriter();writer.clone_document_from_reader(reader)
   with dst.open('wb') as f:writer.write(f)
   pdf_links.append({'file':dst.relative_to(out).as_posix(),'links':changes})
  else:shutil.copy2(src,dst)
 else:shutil.copy2(src,dst)
(out/'.nojekyll').touch()
(R/'reports').mkdir(exist_ok=True)
(R/'reports/pages-export.json').write_text(json.dumps({'base_path':base,'origin':origin,'files':sum(x.is_file() for x in out.rglob('*')),'pdfLinkUpdates':pdf_links,'approved':cfg['approved']},ensure_ascii=False,indent=2),encoding='utf-8')
print('Exported GitHub Pages artifact:',out,'base path:',base)
