#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
print("THIS IS HOW TO FIND THE CELSIUS TO KELVIN AND KELVIN TO CELCIUS")
print("""

""")
print("FORMULA TO CHANGE CELSIUS INTO KELVIN :  K = C+273")
print("FORMULA TO CHANGE KELVIN INTO CELSIUS :  C = K-273")
CELSIUS = int(input("INPUT IN CELSIUS :  "))
KELVIN = CELSIUS+273
print("kelvin = ",KELVIN )
kelvin = int(input("ENTER TEMPERATURE IN KELVIN : "))
celsius=kelvin-273
print("celsius = ",celsius,"°")