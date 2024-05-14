import turtle 
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
pen. color("purple")
pen.setpos(0, 0)
pen.down()    
pen. speed(11230)
for i in range(50000):
      pen. forward(i)
      pen. left(91)
      