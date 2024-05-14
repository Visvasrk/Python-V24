import colorama 
from colorama import Fore 

def cube1():
       print("\n\n______________________________VOLUME CUBE _____________________\n ")
       cube1=eval(input(Fore.YELLOW+"Input side of cube : "))
       volumecube=cube1**3
       print("VOLUME OF CUBE : ",volumecube);
def cube2():
       print("\n\n______________________________TSA    CUBE _____________________\n ")
       cube2=eval(input(Fore.RED+"Input side of cube : "))
       TSAcube=6*(cube2**2)
       print("TOTAL SURFACE AREA OF CUBE : ",TSAcube);
       
def cube3():
       print("\n\n_____________________________ LSA     CUBE _____________________\n ")
       cube3=eval(input(Fore.CYAN+"Input side of cube : "))
       LSAcube=4*(cube3**2)
       print("LATERAL SURFACE AREA OF CUBE : ",LSAcube);
def cubo1():
       print("\n\n______________________________VOLUME CUBOID _____________________\n ")
       cubo1l=eval(input(Fore.CYAN +" Input length of cuboid : ") )
       cubo1b=eval(input(" Input breath of cuboid : ") )
       cubo1h=eval(input(" Input height of cuboid : ") ) 
       volumecubo=(cubo1l*cubo1b*cubo1h)
       print("VOLUME OF CUBOID IS : ",volumecubo);
def cubo2():
       print("\n\n______________________________TSA   CUBOID _____________________\n ")
       cubo2l=eval(input(Fore.GREEN+" Input length of cuboid : ") )
       cubo2b=eval(input(" Input breath of cuboid : ") )
       cubo2h=eval(input(" Input height of cuboid : ") ) 
       TSAcubo=2*((cubo2l*cubo2b)+(cubo2b*cubo2h)+(cubo2h*cubo2l))
       print("TOTAL SURFACE AREA OF CUBOID : ",TSAcubo);
def cubo3():
       print("\n\n______________________________LSA CUBOID   _____________________\n ")
       cubo3l=eval(input(Fore.RED+" Input length of cuboid : ") )
       cubo3b=eval(input(" Input breath of cuboid : ") )
       cubo3h=eval(input(" Input height of cuboid : ") ) 
       CSAcubo=2*cubo3h*(cubo3l+cubo3b)
       print("CURVED SURFACE AREA OF CUBOID : ",CSAcubo)
 
def cyl1():
       print("\n\n______________________________VOLUME CYLINDER  _____________________\n ")
       cyl1h=eval(input(Fore.GREEN+" Input height of cylinder : "))
       cyl1d=eval(input(" Input diameter of cylinder : "))
       rad=cyl1d/2
       VOLcyl=((22/7)*(rad**2)*(cyl1h)) 
       print("VOLUME OF CYLINDER : ",VOLcyl);
def cyl2():
       print("\n\n______________________________TSA CYLINDER _____________________\n ")
       cyl2h=eval(input(Fore.BLUE+" Input height of cylinder : "))
       cyl2d=eval(input(" Input diameter of cylinder : "))
       rad=cyl2d/2
       TSAcyl=2*(22/7)*rad*(rad+cyl2h)
       print("TOTAL SURFACE AREA OF CYLINDER : ",TSAcyl);
def cyl3():
       print("\n\n______________________________LSA CYLINDER _____________________\n ")
       cyl3h=eval(input(Fore.RED+" Input height of cylinder : "))
       cyl3d=eval(input(" Input diameter of cylinder : "))
       rad=cyl3d/2
       pi=22/7
       LSAcyl=2*(pi)*rad*cyl3h
       print("CURVED SURFACE AREA OF CYLINDER : ",LSAcyl);
print(" ADVANCED AREA FINDER   \n\n")
print("ENTER ALL VALUES IN CENTIMETER  ")
print("\n\n_________________________ADVANCED AREA FINDER _____________________\n ")
print(Fore.BLUE+" CHOOSE THE SHAPE YOU WANT TO FIND AREA FOR :  \n ")      
print(Fore.GREEN+"[1]  cube \n ")
print(Fore.RED+"[2]  cuboid \n ")
print(Fore.CYAN+"[3]  cylinder \n ")
print(Fore. YELLOW +"ENTER THE NUMBER (EXAMPLE - \" 1 \") \n ")
USERINPUT=eval(input(Fore.RED+" ENTER THE NUMBER : "));
if USERINPUT == 1 :
           print("___________________________________CUBE___________________________")
           print(Fore.BLUE+" \n CHOOSE THE TYPE OF AREA YOU WANT TO FIND :  \n ")      
           print(Fore.GREEN+"[1:1]  VOLUME \n ")
           print(Fore.RED+"[1:2]  TOTAL SURFACE AREA \n ")
           print(Fore.CYAN+"[1:3]  LATERAL SURFACE AREA \n ")
elif USERINPUT==2 : 
           print("___________________________________CUBOID___________________________")
           print(Fore.BLUE+" \n CHOOSE THE TYPE OF AREA YOU WANT TO FIND :  \n ")      
           print(Fore.GREEN+"[2:1]  VOLUME \n ")
           print(Fore.RED+"[2:2]  TOTAL SURFACE AREA \n ")
           print(Fore.CYAN+"[2:3]  LATERAL SURFACE AREA \n ")
elif USERINPUT == 3 : 
           print("___________________________________CYLINDER ___________________________")
           print(Fore.BLUE+" \n CHOOSE THE TYPE OF AREA YOU WANT TO FIND :  \n ")      
           print(Fore.GREEN+"[3:1]  VOLUME \n ")
           print(Fore.RED+"[3:2]  TOTAL SURFACE AREA \n ")
           print(Fore.CYAN+"[3:3]  LATERAL SURFACE AREA \n ")
else : 
          while True :
                    print(" SORRY WRONG NUMBER ");


USERINPUT2=str(input(Fore.GREEN+" ENTER THE PATH OF THE THING YOU WANT TO FIND AREA FOR :  "))
if USERINPUT2== "1:1":
    cube1()  
elif USERINPUT2=="1:2":
    cube2()
elif USERINPUT2=="1:3":
    cube3()
elif USERINPUT2=="2:1":
    cubo1()
elif USERINPUT2=="2:2":
    cubo2()
elif USERINPUT2=="2:3":
    cubo3()
elif USERINPUT2=="3:1":
    cyl1()           
elif USERINPUT2=="3:2":
    cyl2()
elif USERINPUT2=="3:3":
    cyl3()           
else:
        while True:
            print("SORRY WRONG INPUT ")

 
     