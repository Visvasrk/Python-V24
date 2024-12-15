from pathlib import Path
file_to_open=Path('filereader.txt')
contents=file_to_open.read_text().splitlines()
#assigning a empty string variable
string=" "
for line in contents:
    string+=line
print(string)
print(len(string))
