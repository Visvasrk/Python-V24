#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
a=eval(input("LENGTH 1 : ")) 
b=eval(input("LENGTH 2 : "))
c=eval(input("LENGTH 3 : "))
p=a+b+c
s=p/2
print("Side a is ",a) 
print("Side b is ",b) 
print("Side c is ",c) 
print("Perimeter is ",p) 
print("semi-perimeter is ",s) 
print("THE FORMULA TO FIND AREA OF TRIANGLE IS : ") 
print("(s*(s-a)*(s-b)*(s-c))**(1/2)") 
print("Executing........") 
q=0
while (q<=100) :
      print("Executing program.......",q) 
      q=q+1
      
print("Area is ",(s*(s-a)*(s-b)*(s-c))**(1/2)) 