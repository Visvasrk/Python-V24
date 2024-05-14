#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
x=eval(input("write a number to find it's square root :  "))
y=x**(1/2) 
print("The square root of ",x, "is ",y) 