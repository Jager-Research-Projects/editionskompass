"""Prüft Buchdateinamen, keine XML-Inhalte. Nur Python-Standardbibliothek."""
from pathlib import Path
import argparse,re,sys
PATTERN=re.compile(r'^rk_([0-9]{4}|undatiert)_(b[0-9]{4})\.xml$')
RESERVED=re.compile(r'^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)',re.I)
def check_names(names):
    errors=[];folded=set();ids=set()
    for name in names:
        if re.search(r'[<>:"/\\|?*\x00-\x1f]',name):errors.append(name+': problematisches Zeichen')
        if name.endswith(('.', ' ')):errors.append(name+': Punkt/Leerzeichen am Ende')
        if RESERVED.match(name):errors.append(name+': reservierter Windows-Gerätename')
        if not re.fullmatch(r'[a-z0-9_.-]+',name):errors.append(name+': nicht in ASCII-Kleinschreibung')
        match=PATTERN.fullmatch(name)
        if not match:errors.append(name+': erwartet rk_<jahr>_<buch-id>.xml')
        elif match[1]=='0000':errors.append(name+': undatiert statt 0000 verwenden')
        key=name.lower()
        if key in folded:errors.append(name+': Namenskollision ohne Groß-/Kleinschreibung')
        folded.add(key)
        if match:
            if match[2] in ids:errors.append(name+': Buchkennung mehrfach im maßgeblichen Bestand')
            ids.add(match[2])
    return errors
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder',type=Path,help='Ordner mit den maßgeblichen Buchdateien, z.B. data/tei')
    args=parser.parse_args()
    if not args.folder.is_dir():parser.error('Der Datenordner existiert nicht.')
    names=sorted(p.name for p in args.folder.iterdir() if p.is_file() and p.suffix.lower()=='.xml')
    if not names:parser.error('Keine XML-Buchdateien gefunden.')
    errors=check_names(names)
    if errors:
        print('\n'.join(errors));return 1
    print(f'PASS: {len(names)} Dateinamen entsprechen dem Muster; Namen und Buchkennungen eindeutig.')
    print('XML-Inhalte und Datierung in Metadaten zusätzlich prüfen.')
    return 0
if __name__=='__main__':sys.exit(main())
