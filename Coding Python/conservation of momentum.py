#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
print(str) ;
print("""


         FINDING CONSERVATION OF MOMENTUM

""") 
print("_____________________________________________")


ma=float(input("MASS OF OBJECT A: "   "(Kg) ")) 
mb=float(input("MASS OF OBJECT B: "   "(Kg) ")) 
ua=float(input("INITIAL VELOCITY OF OBJECT A: "   "(m/s) ")) 
ub=float(input("INITIAL VELOCITY OF OBJECT B: "   "(m/s) "))
va=float(input("FINAL VELOCITY OF OBJECT A: "   "(m/s) ")) 
vb="v"
print("FIND  " + vb +"  OF OBJECT B") 
print("""



""") 
print("FINDING CONSERVATION OF MONENTUM")
print("""


""") 
print("_____________________________________________")
print("""CONSERVATION OF MOMENTUM = 
          MAUA+MBUB = MAVA+MBVB
        



     mass of object A X initial velocity of  object A + mass of object B X initial              velocity of object B
    =mass of object A X final velocity of    object A + mass of object B X final velocity of object B """) 
 
print("_____________________________________________") 
print("""

""") 
print(" BEFORE COLLISION") 
print("""


""") 
print(" maua = ",ma, "X",ua, "= ",ma*ua) 
print(" mbub = ",mb, "X",ub, "= ",mb*ub) 
print ("""

""") 
print(" maua+mbub = ", ma*ua + mb*ub) 
print("""

""") 
print("_____________________________________________")
print("AFTER COLLISION")
print("""


""") 
print("(ma+mb) v") 

print("=(" ,ma+mb, ")",vb) 
print("""

""") 
print("maua+mbub = (ma+mb) v") 
print("""

""") 
print("=", ma ,"X", ua,"+",mb, "X" ,ub, "=" ,ma,"+",mb , vb)
print("=", ma*ua+mb*ub, "=", ma+mb , vb) 

print("=", vb, "=",((ma*ua) +(mb*ub) ) /(ma+mb) ,"(m\s)") 
