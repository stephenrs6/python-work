import turtle

t = turtle.Turtle()

def DCircle(x,y,radius,color):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.color(color)
    t.circle(radius)
    t.end_fill()
  
def Mickey():
    r = 50
    DCircle(0,0,2*r,'blue')
    DCircle(-135,115,r,'red')
    DCircle(135,115,r,'red')

def Main():
    Mickey()
    t.done()
    t.bye()
    t.getscreen()._root.mainloop()

Main()