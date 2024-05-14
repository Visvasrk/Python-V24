#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
user=input("Your user Name : ")
password = eval(input("Your password : "))
if password == 1014569:
   print ("you can enter")
else :
   print("access denied \n"*1000) 