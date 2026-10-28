from pathlib import Path
from pypdf import PdfReader
import json
R=Path(__file__).resolve().parents[1];checked=0
for src in (R/'dist').rglob('*.pdf'):
 dst=R/'_site'/src.relative_to(R/'dist');a=PdfReader(src);b=PdfReader(dst)
 assert len(a.pages)==len(b.pages),src
 assert a.trailer['/Root'].get('/Lang')==b.trailer['/Root'].get('/Lang'),src
 assert ('/StructTreeRoot' in a.trailer['/Root'])==('/StructTreeRoot' in b.trailer['/Root']),src
 for before,after in zip(a.pages,b.pages):
  assert before.mediabox==after.mediabox,src
  assert (before.extract_text() or '')==(after.extract_text() or ''),src
  for ref in after.get('/Annots',[]):
   action=ref.get_object().get('/A')
   if action:
    uri=str(action.get_object().get('/URI',''))
    assert not any(x in uri for x in ['127.0.0.1:8897','localhost:8897','editionskompass.tomsummer.chatgpt.site']),[str(src),uri]
 checked+=1
(R/'reports/pdf-check.json').write_text(json.dumps({'pdfs':checked,'checks':['same page count','same page dimensions','same extracted text','language preserved','structure tags preserved','preview URLs removed']},indent=2),encoding='utf-8')
print('PASS',checked,'PDF exports: text, geometry, language and tags preserved')
