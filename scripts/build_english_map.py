from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
data=json.loads((R/'inhalte/uebersetzung/en.json').read_text(encoding='utf-8'))
(R/'dist/assets/english-map.js').write_text('window.EDITIONS_EN='+json.dumps(data,ensure_ascii=False)+';',encoding='utf-8')
print('Published English translation memory:',len(data),'entries')
