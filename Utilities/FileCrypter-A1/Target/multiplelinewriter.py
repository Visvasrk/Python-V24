#here we are gonna write multiple lines to the given file and add them to the file.
from pathlib import Path
filetowrite=Path('filereader.txt')
contenttowrite=str(input('Enter the text to write in the document : '))+"\n"
content=filetowrite.read_text()+contenttowrite
filetowrite.write_text(content)
