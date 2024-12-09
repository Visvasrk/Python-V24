from pathlib import Path
path=Path('filereader.txt')
content=path.read_text()
print(content)
#Or we can directly read the file by
#print(path.read_text())
#Or
#print(Path('filereader.txt').read_text())

