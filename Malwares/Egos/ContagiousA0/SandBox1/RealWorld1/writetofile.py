#here we will talk about how to write a statement to the file
#This program writes only one single line to the file.
from pathlib import Path
writetofile=Path('writefile.txt')
message=str(input('Enter the line you need to write in the file : '))
writetofile.write_text(message)
