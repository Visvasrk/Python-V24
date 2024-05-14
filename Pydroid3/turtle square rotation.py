import turtle 
i=0

pen = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle")
def ring(col, rad):
       pen.fillcolor(col)
       pen.begin_fill()
       pen.circle(rad)
       pen.end_fill()
pen.up()
pen. color("green")
pen.setpos(0, 0)
pen.down()    
pen. pensize(3)
pen. speed(1000)
while (i <= 1000000):
          i+=3
          
          pen. forward(i)
          pen. right(90)
            
          
