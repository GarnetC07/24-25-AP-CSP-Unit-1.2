# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0

def update_score_for_box(x,y):
  global score
  score += 1
  score1.clear()
  score1.write(score, font=font_setup)

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
score1 = trtl.Turtle()
font_setup = ("Arial", 20, "normal")
score1.hideturtle()

#-----game functions--------
#Randomized the place where the turtle goes when clicked
def change_position():
    spot.penup()
    new_xpos=rand.randint(-400,400)
    new_ypos=rand.randint(-300,300)
    spot.goto(new_xpos,new_ypos)

score1.penup()
score1.goto(-470, 370)

def spot_clicked(x,y):
    change_position()
    update_score_for_box(0, 0)

#-----events----------------
spot.onclick(spot_clicked),(update_score_for_box)(0,0)
wn = trtl.Screen()
wn.mainloop()