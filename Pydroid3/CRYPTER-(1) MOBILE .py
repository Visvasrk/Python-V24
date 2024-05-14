# encrypt and decrypt a text using a simple algorithm of offsetting the letters 
import colorama
from colorama import Fore 

key = 'Aa%1Bb|2Cc3D[¢`~•/\\d!4Ee5F=fG]g>°Hh×6Ii<JjK.k{LlM7*m√?\"N€n®₹O\'oP}p:Qq,@8Rr#SsπTt£U;_9uV&÷vW0-w+℅∆Xx(Y$yZ)z ©'
def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext:
        try:
            i = (key.index(l) + n) % 108
            result += key[i]
        except ValueError:
            result += l

    return result

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 108
            result += key[i]
        except ValueError:
            result += l

    return result

#now setting user input ,and here offset is the authentication key 
# DOOR MAT DESIGN
# should use odd number
#N, M = map(int, input().split())
N, M = 12, 36
design = list(
    f"{'.|.'*i:-^{M}}"
    for i in range(1, N, 2)
)
print(
    "\n".join(
        design + \
        [f"{'CRYPTER-1':-^{M}}"] + \
        design[::-1]
    )
,"\n\n\n")
print("WELCOME TO CRYPTER 1 \n \n  ")
print("CHOOSE YOUR MODE : \n ")
print(Fore.RED+"[1]  ENCRYPT")
print(Fore.GREEN+"[2]  DECRYPT")
print(Fore.CYAN+"[3]  ABOUT")
print(Fore.BLUE+"[4]  EXIT\n")
print(Fore.RED+"DONE BY SANJAY SHRINIVAAS .V ")
print(Fore.YELLOW+"CLASS :  JUNIOR TENTH --- A \n\n\n\a\a ")
choose = input(Fore.WHITE+"ENTER YOUR INPUT : ")
if choose == '[1]' :
    print(Fore.RED+"ENTER TEXT TO\a\a ENCRYPT\n ")
    text=input(Fore.YELLOW+"ENTER HERE : \n \a \n ")
    offset=int(input("\n ENTER AUTHENTICATION KEY : "))
    encrypted = encrypt(offset, text)

    print(Fore.GREEN+'\a\a\a Encrypted:', encrypted)

elif choose == '[2]' : 
    print(Fore.GREEN+"ENTER TEXT TO DECRYPT\n")
    text=input(Fore.BLUE+"ENTER HERE : \n \a \n ")
    offset=int(input("\n ENTER AUTHENTICATION KEY : "))
    decrypted = decrypt(offset, text)

    print(Fore.CYAN+'\a\a\a Decrypted:', decrypted)
elif choose == '[3]' :
    print("Convert the string to a byte string, \n so that it can be encrypted.\n Instance the Fernet class with the \a encryption key.\n Then encrypt the string with the Fernet instance.\n Then it can be decrypted with Fernet class instance and it \n should be instanced with the same key used \n for encryption \a ")
    
elif choose == '[4]'  :
       print("THANKYOU\a\a\a ")
       exit()     
else :
    print("  enter the string like \" [1] \" ")     
    
# THE END         



