#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
num = 3
if num == 1:
  print("One")
else: 
  if num == 2:
    print("Two")
  else: 
    if num == 3: 
      print("Three")
    else: 
      print("Something else");
    
    
num2 = 100
if num2==10:
   print("Ten ")
elif num2 ==50:
   print("fifty")
elif num2 == 80:
   print("Eighty")
elif num2 == 100:
   print("Hundred") 
else :
   print("unidentified")

