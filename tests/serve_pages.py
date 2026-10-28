from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json,argparse
R=Path(__file__).resolve().parents[1];D=R/'_site';base=json.loads((R/'publication.json').read_text())['base_path'].rstrip('/')
class Handler(SimpleHTTPRequestHandler):
 protocol_version='HTTP/1.1'
 def do_GET(self):
  path=urlsplit(self.path).path
  if path==base:self.send_response(301);self.send_header('Location',base+'/');self.end_headers();return
  if not path.startswith(base+'/'):self.send_error(404);return
  super().do_GET()
 def translate_path(self,path):
  target=(D/unquote(urlsplit(path).path[len(base)+1:])).resolve()
  return str(target) if target.is_relative_to(D.resolve()) else str(D/'__invalid__')
 def log_message(self,*args):pass
p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8898);args=p.parse_args();print('http://127.0.0.1:'+str(args.port)+base+'/',flush=True)
class Server(ThreadingHTTPServer):request_queue_size=128
Server(('127.0.0.1',args.port),Handler).serve_forever()
