#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
print("F=(9\5)C+32") 
print("THIS IS THE FORMULA TO FIND THE CELCIUS OR FARENHEIT")
print("F-32=(9\5)C")
print("(F-32) X 5=9C")
print("5F-(32X5)=9C")
print("5F-160=9C")
print("5F-9C-160=0")
Fahrenheit = eval(input("Enter a temperature in Fahrenheit: "))

Celsius = (Fahrenheit - 32) * 5.0/9.0

print("Fahrenheit:", Fahrenheit, "Temperature = ", Celsius, " C")
celsius =eval(input("Enter a temperature in celcius : "));

fahrenheit = ((9/5)*celsius+32)
print("celsius:",celsius, "temperature=",fahrenheit) 