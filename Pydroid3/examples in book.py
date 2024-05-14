#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
print("Hi hello how are you? ") 
print(float(100) ) 
print(int(100)) 
print(complex (99+1j)) 
print(eval("100")) 
print(bool(True)) 
x=input(" Write any number : " ) 
print(int(x)) 
print(eval(x)) 
print(float(x)) 
print(complex(x)) 
print(bool(x)) 
print("___________________________________________") 
print("EXAMPLE 5 IN BOOK") 
print("SQUARES AND CUBES") 
a=eval(input("Enter a number to be squared\cubed : ")) 
square = a**2
cube = a**3
print(" square of ", a, " is" ,square);
print(" cube of ", a, " is" ,cube);
print("___________________________________________")
print("EXAMPLE 4 IN BOOK") 
print("All ARITHMETIC OPERATION FOR 2 NUMBERS") 
b=eval(input ("Write the first number : ")) 
c=eval(input (" Write the second number : ")) 
print(b, "+", c, "=", b+c) 
print(b, "-", c, "=", b-c)
print(b, "x", c, "=", b*c)
print(b, "÷", c, "=", b/c)
print(b, " power of ", c, "=", b**c)
print(b, "modulus of ", c, "=", b%c)
print(b, "//", c, "=", b//c) 
print("___________________________________________") 
