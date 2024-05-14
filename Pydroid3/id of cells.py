#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
a=100
print(id(a) ) 
b=a
print(id(b)) 
a=1000
print(id(a)) 
print(a, b) 
print(id(b)) 