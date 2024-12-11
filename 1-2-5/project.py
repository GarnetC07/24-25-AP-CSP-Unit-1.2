import turtle as trtl
import random as rand

#variable creation and named them all
painter = trtl.Turtle()
wn = trtl.Screen()
painter.screen.bgcolor('black')
painter.speed('fastest')

def middle_lines():
    painter.color('white')
    painter.hideturtle()
    painter.penup()
    painter.setpos(0,500 )
    painter.pendown()
    painter.pensize(20)
    painter.right(90)
    painter.forward(30)





wn.listen()
wn.mainloop()