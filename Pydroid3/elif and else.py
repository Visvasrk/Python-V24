#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
x=7
print(x == 7) 
print(x >= 3) 
print(x != 10) 
print(x >5) 
print(x <10) 
print(x <= 10) ;


print("""



if else statements""") 

x=10
print (x) 
if x!=110:
   print("yes") 
else:
        print("no") ;
        
        
        
        
num=100
print (num) 
if num == 10:
   print("yes") 
else:
  if num == 5:
     print ("yes") 
  else:
    if num == 20:
       print ("yes") 
    else:
      if num != 1000:
         print("no it is 100") ;
    