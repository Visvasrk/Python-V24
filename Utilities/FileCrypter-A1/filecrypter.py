##This is a python crypto-grapher, which is used to encrypt or decrypt files.
#Note : Ensure that you run this file on a safe and secured isolated directory.
#You can encrypt or decrypt the files in the directory specifically or seperately.

#Import the necessary modules
from cryptography.fernet import Fernet
import time
import os
import sys

#Define the menu banners and other text variables
menubanner1 = '''
        WELCOME TO FILE-CRYPTER
 _________________________________________
|                                         |
| Select from the Menu                    |
|                                         |
| [1]Encrypt All Files in Directory Tree  |
| [2]Decrypt All Files in Directory Tree  |
| [3]Encrypt All Files in a Directory     |
| [4]Decrypt All Files in a Directory     |
| [5]Encrypt a Specific File              |
| [6]Decrypt a Specific File              |
| [7]Navigate to the Keys Directory       |
| [8]List Directory Tree                  |
| [9]Help                                 |
| [0]Exit                                 |
|                                         |
|_________________________________________|

[NOTE] : You can use a password only once.
	 All the passwords set by you are one time passwords. (OTP)


'''

enctree = '''
 __________________________________________________________________________________________________________________________
|                                                   CRYPTER TREE ENCRYPTION                                                |
|__________________________________________________________________________________________________________________________|


[NOTE] :
	-This is a very useful feature in crypter file encrypter and decrypter.
	-This utility helps in encrypting the entire directory tree.
	-This includes the encryption of all the files in all the subdirectories of the target directory.
	-Beware, crypter is safe to use untill you remember the password for decryption.

[USAGE] :

	Step 1: Enter the full absolute path of the target directory.
		If the target directory is the current directory, then enter \'.\'
		Beware, the path of the target you entered must be 100% correct.

	Step 2: Crypter encrypts all the files in the directory tree.

	Step 3: Once prompted for the password, please enter as strong and secure password.

	Step 4 : Remember the password. Forgeting the password may lead to irreversible file corruption, that is, all the files will stay encrypted FOREVER!!!

'''

dectree = '''
 __________________________________________________________________________________________________________________________
|                                                   CRYPTER TREE DECRYPTION                                                |
|__________________________________________________________________________________________________________________________|


[NOTE] :
        -This is a very useful feature in crypter file encrypter and decrypter.
        -This utility helps in decrypting the entire directory tree, which has been encrypted by Crypter Tree Encryption utility ONLY!
	-You may not be able to decrypt the tree if you use any other crypter utility.
        -This includes the decryption of all the files in all the subdirectories of the target directory.
        -Beware, crypter is safe to use untill you remember the password for decryption.

[USAGE] :

        Step 1: Enter the full absolute path of the target directory.
                If the target directory is the current directory, then enter \'.\'
                Beware, the path of the target you entered must be 100% correct.

        Step 2: You will be promted for the decryption password.

        Step 3: After entering the RIGHT password, all the files in the directory trees will be decrypted.

        Step 4: Remember the password. Forgeting the password may lead to irreversible file corruption, that is, all the files will stay encr>

'''



encdir = '''
 __________________________________________________________________________________________________________________________
|                                              CRYPTER DIRECTORY ENCRYPTION                                                |
|__________________________________________________________________________________________________________________________|


[NOTE] :
        -This is a very useful feature in crypter file encrypter and decrypter.
        -This utility helps in encrypting all the files in the directory target
        -The subdirectories of the target directory will not be encrypted
        -Beware, crypter is safe to use untill you remember the password for decryption.

[USAGE] :

        Step 1: Enter the full absolute path of the target directory.
                If the target directory is the current directory, then enter \'.\'
                Beware, the path of the target you entered must be 100% correct.

        Step 2: Cryptet encrypts all the files in the target directory, leaving the files of the subdirectories undisturbed.

        Step 3: Once prompted for the password, please enter as strong and secure password.

        Step 4 : Remember the password. Forgeting the password may lead to irreversible file corruption, that is, all the files will stay encr>

'''

decdir = '''
 __________________________________________________________________________________________________________________________
|                                                   CRYPTER TREE DECRYPTION                                                |
|__________________________________________________________________________________________________________________________|


[NOTE] :
        -This is a very useful feature in crypter file encrypter and decrypter.
        -This utility helps in decrypting the files of the target directory only, which has been encrypted by Crypter Directory Encryption utility ONLY!
        -You may not be able to decrypt the directory if you use any other crypter utility.
        -This includes the decryption of all the files in the target directory only, leaving the subdirectories undistrubed.
        -Beware, crypter is safe to use untill you remember the password for decryption.

[USAGE] :

        Step 1: Enter the full absolute path of the target directory.
                If the target directory is the current directory, then enter \'.\'
                Beware, the path of the target you entered must be 100% correct.

        Step 2: You will be promted for the decryption password.

        Step 3: After entering the RIGHT password, all the files in the directory except in the subdirectories will be decrypted.

        Step 4: Remember the password. Forgeting the password may lead to irreversible file corruption, that is, all the files will stay encr>

'''

fileenc = '''
 __________________________________________________________________________________________________________________________
|                                                   CRYPTER FILE ENCRYPTION                                                |
|__________________________________________________________________________________________________________________________|

'''
filedec = '''
 __________________________________________________________________________________________________________________________
|                                                   CRYPTER FILE DECRYPTION                                                |
|__________________________________________________________________________________________________________________________|

'''
keybanner = '''
 __________________________________________________________________________________________________________________________
|                                                   WHERE THE KEYS ARE KEYED                                               |
|__________________________________________________________________________________________________________________________|

'''

epoch = time.time()
crttime = time.ctime(epoch)
cm = f"[Crypter@{crttime}] >"


#Define the functional variables
join = os.path.join
absolute = os.path.abspath
ls = os.listdir
mkdir = os.mkdir
rmdir = os.rmdir
makedirs = os.makedirs
remove = os.remove
walk = os.walk
epoch = time.time()
crttime = time.ctime(epoch)
exists = os.path.exists


#Define the files and paths
crtfile = os.path.basename(__file__)
homepath = os.path.expanduser("~")
localkeypath = '.Crypter/files/keys/'
keypath = absolute(join(homepath, localkeypath))
crtdir = absolute(os.getcwd())


#Define a function to show the help screen for the user
def Help():
	pass

#Define a function to clear the terminal screen
def Clear(delay):
	time.sleep(delay)
	os.system('clear')

#Define a function to check the existence of the files and filepaths.
def Check():
	if exists(keypath):
		if exists(absolute(keypath)):
			return True
	else:
		makedirs(keypath)
		return True

#Define a function to generate a key
def GenerateKey():
	key = Fernet.generate_key()
	return key

#Define a function to save the key to a file
def SaveKey(key):
	#Get input from the user about the file name
	name = input(f"{cm} Enter a New Password (eg- \'Passwd12@crypter\', etc): ")
	#save the key to a file with specific name
	if Check():
		#check if the file with the name already exists
		if exists(absolute(join(keypath, name))):
			print(f"{cm} Sorry, the password \'{name}\' already exists, provide another unique password.")
			SaveKey(key)
		else:
			with open(absolute(join(keypath, name)), 'wb') as keyfile:
				keyfile.write(key)
			print(f"{cm} Decryption password successfully stored as \'{name}\'.")

#Define a function to Load the key from a file
def LoadKey():
	#Get input from the user about the keyfile name
	keyfile = input(f"{cm} Enter the decryption password : ")
	if Check():
		if exists(absolute(join(keypath, keyfile))):
			with open(absolute(join(keypath, keyfile)), 'rb') as file:
				key = file.read()
				keytup = (keyfile, key)
				return keytup
		else:
			print(f"{cm} Sorry, the password \'{keyfile}\' is invalid. Provide correct credentials.")
			LoadKey()
#Define a function to delete the old keys after encryption
def DelKey(key):
	if exists(absolute(join(keypath, key))):
		target = absolute(join(keypath, key))
		os.remove(target)
	else:
		print(f"{cm} Sorry, invalid request.")

#Define a function to encrypt the files in a directory
def EncryptFilesInDir(directory):
	#generate a key
	key = GenerateKey()
	for obj in ls(directory):
		if os.path.isfile(absolute(join(directory, obj))) and obj != crtfile:
			crypter = Fernet(key)
			target = absolute(join(directory, obj))
			with open(target, 'rb') as file:
				content = file.read()
				chiper = crypter.encrypt(content)
			with open(target, 'wb') as file:
				file.write(chiper)
				print(f'{cm} File {obj} successfully encrypted.')
	SaveKey(key)

#Define a functionto decrypt the files in a directory
def DecryptFilesInDir(directory):
	#Load the key from a pre-existing keyfile
	keytup = LoadKey()
	keyfile = keytup[0]
	key = keytup[1]

	for obj in ls(directory):
		if os.path.isfile(absolute(join(directory, obj))) and obj != crtfile:
			crypter = Fernet(key)
			target = absolute(join(directory, obj))
			with open(target, 'rb') as file:
				content = file.read()
				plaintext = crypter.decrypt(content)
			with open(target, 'wb') as file:
				file.write(plaintext)
				print(f'{cm} File {obj} successfully decrypted.')
	DelKey(keyfile)


#Define a function to encrypt all the files in the directory tree
def EncryptTree(basedir):
	#generate a fernet key
	key = GenerateKey()
	for dirpath, directories, files in walk(basedir):
		for obj in files:
			if absolute(dirpath) != absolute(keypath):
				if obj != crtfile:
					crypter = Fernet(key)
					target = absolute(join(dirpath, obj))
					with open(target, 'rb') as file:
						content = file.read()
						chiper = crypter.encrypt(content)
					with open(target, 'wb') as file:
						file.write(chiper)
					print(f'{cm} File {obj} successfully encrypted.')
	SaveKey(key)

#Define a function to decrypt the directory tree
def DecryptTree(basedir):
	#load key from keyfile
	keytup = LoadKey()
	keyfile = keytup[0]
	key = keytup[1]

	for dirpath, directories, files in walk(basedir):
		for obj in files:
			if absolute(dirpath) != absolute(keypath):
				if obj != crtfile:
					crypter = Fernet(key)
					target = absolute(join(dirpath, obj))
					with open(target, 'rb') as file:
						content = file.read()
						plaintext = crypter.decrypt(content)
					with open(target, 'wb') as file:
						file.write(plaintext)
					print(f'{cm} File {obj} successfully decrypted.')
	DelKey(keyfile)

#Define a function to encrypt a particular file alone
def EncryptFile(filepath):
	#generate a fernet key
	key = GenerateKey()
	if exists(absolute(filepath)):
		crypter = Fernet(key)
		if os.path.isfile(absolute(filepath)):
			target = absolute(filepath)
			with open(target, 'rb') as file:
				content = file.read()
				chiper = crypter.encrypt(content)
			with open(target, 'wb') as file:
				file.write(chiper)
			print(f'{cm} File {os.path.basename(filepath)} successfully encrypted.')
		else:
			print(f"{cm} Sorry, the path {absolute(filepath)} is not a file.")
	else:
		print(f"{cm} Sorry, the path {absolute(filepath)} does not exist.")
	#Save the key
	SaveKey(key)


#Define a function to decrypt a particular file alone
def DecryptFile(filepath):
	#Load the key
	keytup = LoadKey()
	keyfile = keytup[0]
	key = keytup[1]

	if exists(absolute(filepath)):
		crypter = Fernet(key)
		if os.path.isfile(absolute(filepath)):
			target = absolute(filepath)
			with open(target, 'rb') as file:
				content = file.read()
				plaintext = crypter.decrypt(content)
			with open(target, 'wb') as file:
				file.write(plaintext)
			print(f'{cm} File {os.path.basename(filepath)} successfully decrypted.')
		else:
			print(f"{cm} Sorry, the path {absolute(filepath)} is not a file.")
	else:
		print(f"{cm} Sorry, the path {absolute(filepath)} does not exist.")
	DelKey(keyfile)

#Define the main function

def Menu(banner):
	print(banner)

def FileCrypter():
	Menu(menubanner1)
	choice = int(input("Select : "))
	print("")
	Clear(2)
	if choice == 1:
		Menu(enctree)
		basedir = input(f"{cm} Enter the absolute path of the directory tree you want to encrypt (\'.\' for current directory) : ")
		EncryptTree(basedir)
		Clear(5)
	elif choice == 2:
		Menu(dectree)
		basedir = input(f"{cm} Enter the absolute path of the directory tree you want to decrypt (\'.\' for current directory) : ")
		DecryptTree(basedir)
		Clear(5)
	elif choice == 3:
		Menu(encdir)
		directory = input(f"{cm} Enter the absolute path of the directory you want to encrypt (\'.\' for current directory) : ")
		EncryptFilesInDir(directory)
		Clear(5)
	elif choice == 4:
		Menu(decdir)
		directory = input(f"{cm} Enter the absolute path of the directory you want to decrypt (\'.\' for current directory) : ")
		DecryptFilesInDir(directory)
		Clear(5)
	elif choice == 5:
		Menu(fileenc)
		filename = input(f"{cm} Enter the name of the file you want to encrypt (eg- hello.txt) : ")
		parentpath = input(f"{cm} Enter the absolute (or) relative path of the directory in which \'{filename}\' is present (\'.\' if it is current directory ):")
		targetpath = absolute(join(parentpath, filename))
		EncryptFile(targetpath)
		Clear(5)
	elif choice == 6:
		Menu(filedec)
		filename = input(f"{cm} Enter the name of the file you want to decrypt (eg- hello.txt) : ")
		parentpath = input(f"{cm} Enter the absolute (or) relative path of the directory in which \'{filename}\' is present (\'.\' if it is current directory ):")
		targetpath = absolute(join(parentpath, filename))
		DecryptFile(targetpath)
		Clear(5)
	elif choice == 7:
		Menu(keybanner)
		print(f"{cm} Navigating to the keys directory... ")
		time.sleep(1)
		os.chdir(absolute(keypath))
		print(f"{cm} Successfully Navigated to the \'Keys\' directory.")
		Clear(5)
	elif choice == 8:
		print(f"{cm} Please Wait, listing the directory tree...\n")
		os.system('tree')
		print(f"\n{cm} Tree Clears in 10 Seconds...")
		Clear(10)
	elif choice == 9:
		Help()
	elif choice == 0:
		sys.exit(0)
		os.system('clear')
	elif choice == 404:
		os.system('clear')
	else:
		print(f"INVALID CHOICE : {choice}, select your choice again.")
		FileCrypter()

#Define the main function
def Main():
	while True:
		try:
			FileCrypter()
		except KeyboardInterrupt:
			os.system('clear')
			sys.exit(1)
		except Exception as e:
			print(f"{cm} An error had occured during the process.\n{cm} Error : {e}\n")

#Execute
Main()
