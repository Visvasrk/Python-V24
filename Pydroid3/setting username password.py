 #!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
Username= input("Enter your new username : ")
conf_username=input("Confirm your  : ")
if Username == conf_username:
   Password = eval(input("Set a password : "))
else:
   print(" \a Confirmation password incorrect,TRY AGAIN ")
   Username= input("Enter your new username : ")
   conf_username=input("Confirm your username : ");
conf_password=eval(input("Confirm your password : "))
savedD1={"Username":Username, "Password":Password}
if Password==conf_password :
   print(savedD1.keys)
   print(savedD1.values)
   print("you can enter ")
   
else: 
   print("\a Try Again from Beginning,password or username is incorrect " );
print(savedD1.keys)
print(savedD1.values) 

