from pathlib import Path
textfile=Path('filereader.txt')
contents=textfile.read_text().splitlines()
for line in contents:
    print(line)
