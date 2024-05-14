#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
username=input("YOUR USERNAME : ")
yourname=input("YOUR NAME : ")
setpass=eval(input("SET YOUR PASSWORD : ")) 
yourage=int(input("ENTER YOUR AGE : "))
yourmobile=int(input("ENTER YOUR MOBILE NUMBER : "))
x=1
d1={"USERNAME":username,"NAME":yourname,"PASSWORD":setpass, "AGE":yourage, "MOBILE":yourmobile}
l1=[d1]
print(d1.keys(),"___THESE ARE YOUR KEYS") 
print(d1.values(),"___THESE ARE YOUR VALUES") 
print(l1) 
    