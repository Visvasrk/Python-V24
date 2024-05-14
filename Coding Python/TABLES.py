#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
x =int(input("ENTER A NUMBER : ") ) 
y =1

print(x , " TABLES") 

while y<=1500:
   print(x ,"X",y,"=",x*y) 
   y = y+1

    