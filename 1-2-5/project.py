import turtle as trtl
import random as rand

#variable creation and named them all
painter = trtl.Turtle()
wn = trtl.Screen()
painter.screen.bgcolor('black')
painter.speed('fastest')

painter.color('white')
painter.hideturtle()
painter.penup()
painter.goto(0,400 )
painter.pendown()
painter.right(90)
painter.forward(30)





wn.listen()
wn.mainloop()