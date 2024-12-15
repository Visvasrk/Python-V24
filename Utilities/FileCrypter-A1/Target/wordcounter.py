from pathlib import Path
def countwords(filename):
    path=Path(filename).read_text()
    words=path.split()
    word_count=len(words)
    print(f'The file named {filename} has {word_count} words...')
 
wordlists=['filereader.txt','wordlist.txt','writefile.txt']   
for wordlist in wordlists:
    countwords(wordlist)
    
