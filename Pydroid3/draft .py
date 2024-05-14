import colorama 
from colorama import Fore 
import PIL 

#length scale conversion
def cm2m():
       print("CENTIMETER TO METER ")
       cm1=eval(input("ENTER VALUE IN CENTIMETER : "))
       m1=cm1/100
       print(" CENTIMETER IN METER IS : ",m1)
def m2cm():
       print(" METER TO CENTIMETER ")
       m2=eval(input(" ENTER VALUE IN METER : "))
       cm2=m2*100
       print(" METER IN CENTIMETER IS : ",cm2 )
def m2km():
       print(" METER TO KILOMETER")
       m3=eval(input(" ENTER VALUE IN METER : "))
       km1=m3/1000
       print(" METER IN KILOMETER IS : ",km1)     
def km2m():
       print(" KILOMETER TO METER ")
       km2=eval(input(" ENTER VALUE IN KILOMETER : "))
       m4=km2*1000
       print(" KILOMETER IN METER IS : ",m4)
       
       
#weight scale conversion     
def kg2g():
       print(" KILOGRAM TO GRAM ")
       kg1=eval(input(" ENTER VALUE IN KG : "))
       g1=kg1*1000
       print(" KG IN G : " ,g1 )
def g2kg():
       print(" GRAM TO KILOGRAM ")
       g2=eval(input(" ENTER VALUE IN G : "))
       kg2=g2/1000
       print(" G IN KG : " ,kg2 )
def g2mg():
       print(" GRAM TO MILLIGRAM ")
       g3=eval(input(" ENTER VALUE IN G : "))
       mg1=g3*1000
       print(" G IN MG : " ,mg1 )      
def mg2g():
       print(" MILLIGRAM TO GRAM ")
       mg2=eval(input(" ENTER VALUE IN MG : "))
       g4=mg2/1000
       print(" MG IN G : " ,g4 )      
#litre scale conversion 
def ml2l():
       print("MILLILITRE TO LITRE")
       ml1=eval(input("ENTER VALUE IN MILLILITRE: "))
       l1=ml1/1000
       print(" ML IN L : ",l1)
def l2ml():
       print("LITRE TO MILLILITRE")
       l2=eval(input(" ENTER VALUE IN LITRE : "))
       ml2=l2*1000
       print(" L IN ML : ",ml2)
def l2kl():
       print("LITRE TO KILOLITRE")
       l3=eval(input(" ENTER VALUE IN LITRE "))
       kl1=l3/1000
       print(" L IN KL : ",kl1)
       
def kl2l():
       print ("KILOLITRE TO LITRE ")         
       kl2=eval(input("ENTER VALUE IN KILOLITRE : "))   
       l4=kl2*1000  
       print(" KL IN L : ",l4)                      

#volume conversion 
def m22cm2():
       print(" METER² TO CENTIMETER²")
       m21=eval(input("ENTER VALUE IN METER ² : "))
       cm21=m21*(100**2)
       print(" M² IN CM² : ",cm21)
def cm22m2():
       print(" CENTIMETER² TO METER²")
       cm22=eval(input("ENTER VALUE IN CM² : "))
       m22=cm22/(100**2)
       print(" CM² IN M² : ",m22)
def cm32m3():
       print(" CENTIMETER³ TO METER³")      
       cm31=eval(input("ENTER VALUE IN CM³ : "))
       m31=cm31/(100**3)
       print(" CM³ IN M³ : ",m31)
def m32cm3():
       print(" METER³ TO CENTIMETER³  ")   
       m32=eval(input(" ENTER VALUE IN M³ : "))
       cm32=m32*(100**3)
       print(" M³ IN CM³ : ",cm32)
#Heat scale conversion 
def k2c():
       print(" KELVIN TO CELSIUS ")
       k2=eval(input("ENTER TEMPERATURE IN KELVIN : "))
       c2=k2-273
       print(" YOUR TEMPERATURE IN CELSIUS : ,",c2)
       
def c2k():
       print(" CELSIUS TO KELVIN ")
       c1=eval(input (" ENTER TEMPERATURE IN CELSIUS : "))
       k1=c1+273
       print(" YOUR TEMPERATURE IN KELVIN : ",k1)
def c2f():
       print(" CELSIUS TO FAHRENHEIT")
       c3=eval(input("ENTER TEMPERATURE IN CELSIUS : "))
       f1=(c3 *(9/5)) + 32 
       print(" YOUR VALUE IN FAHRENHEIT : ",f1)
def f2c():
       print("FAHRENHEIT TO CELSIUS ")
       f2=eval(input("ENTER TEMPERATURE IN FAHRENHEIT : "))
       c4=(f2 - 32) * (5/9)
       print(" YOUR VALUE IN CELSIUS : ",c4)

#mass and weight conversion
def w2m():
       print(" WEIGHT TO MASS ")
       w1=eval(input(" ENTER YOUR WEIGHT IN N : "))
       mas1=w1/9.8
       print(" YOUR MASS IS : ",mas1," kg")
def m2w():   
       mas2=eval(input(" ENTER YOUR MASS IN KG : "))
       w2=mas2*9.8
       print(" YOUR WEIGHT IS : ",w2, " N")
#speed scale conversion 
def kmh1():
       print("KM\H INTO M\S")
       kmh11=eval(input("ENTER THE VALUE IN KMH-1 : "))
       ms11=kmh11/3.6
       print(" THE VALUE IN MS-1 :",ms11)
   
def ms1():
       print("M\S INTO KM\H")   
       ms12=eval(input("ENTER VALUE IN MS-1 : "))
       kmh12=ms12*(3.6)
       print(" THE VALUE IN KMH-1 : ",kmh12)
#end
kmh1()       
ms1()