#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
topic="VARIABLES"
print("TODAYS TOPIC IS ON "+topic) 
a, b, c="orange " , "is " , "my favourite"
print(a+b+c) 
x=y=z="apple"
print(x)
print(y)
print(z)
fruits=["apple", "cherry", "mango"]
w, e, r = fruits
print(w)
print(e)
print(r)
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
def myfunc() :
   global x
x=10000
myfunc() 
print(x) 
