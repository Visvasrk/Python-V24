#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);

print("THIS IS A TUPLE ") 
T1=("HELLO ", 200020,"HI", 100010) 
print(T1) 
print("THIS IS A LIST ") 
L1=["HI ","HELLO",2022,2023]
print(L1)
print("THIS IS A SET")
S1=set(["Sanjay",100,"infant",99.999999999])
print (S1)
print("THIS IS A DICTIONARY.") 
D1={"Sanjay":1000,"Infant":1100}
print(D1.keys())
print(D1.values()) 
  