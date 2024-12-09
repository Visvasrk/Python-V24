from pathlib import Path
def countwords(filename):
    filetocount=Path(filename).read_text()
    words=filetocount.split()
    num_words=len(words)
    print(f'The file named {filename} has {num_words} words...')
wordlists=['filereader.txt','wordlist.txt','makefile.txt','writefile.txt']
for wordlist in wordlists:
    try:
        countwords(wordlist)
    except FileNotFoundError:
        print(f'Sorry the file named {wordlist} is not avaliable')
        #if you don't want the python to send any exceptions, and want to pass it silently:Use 'pass'
        #pass
        

   
