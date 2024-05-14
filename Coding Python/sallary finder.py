#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
name=input("YOUR USER NAME :  ")
print(name) 
age=int(input("YOUR AGE:  ")) 
print(age) 
salary=int(input("YOUR MONTHLY SALARY :  ")) 
print (salary) 
advance=float(input("YOUR ADVANCE CHARGES :  ")) 
print (advance) 
print("your yearly salary is ",(salary-advance)*12) 
print("your monthly income is", salary-advance) 


