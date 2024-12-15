#It is not just only a name checker. You can also check any character whether it appears in the wordlist or not.
#Just by using pathlib.
from pathlib import Path
import timeit
#let us create a name list to check whether it is in the wordlist.
userinput=input("Enter any 5 letter word to search in the wordlist given : ")
def search(filename,word):
    wordlist=Path(filename)
    words=wordlist.read_text().splitlines()
    number='0'
    for word in words:
        number=int(number)
        number+=1
        number=str(number)
        if word == userinput:
           print(f'Yes.The word {word} is in the namelist.')
           print(f'The word {word} is {number}th element of the wordlist...')
           print('')
       
search('wordlist.txt',userinput) 

