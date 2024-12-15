from pathlib import Path
import json

jsonfile=Path('ifexists.json')
if jsonfile.exists():
    readjsonfile=jsonfile.read_text()
    loadjsonfile=json.loads(readjsonfile)
    print(f'Hey hello you are here {loadjsonfile}...')
else:
    username=input('Enter your Username : ')
    dumpjsonfile=json.dumps(username)
    jsonfile.write_text(dumpjsonfile)
    print(f"We'll remember you when you come back, {username}!")
