import turtle as trtl
import random as rand

# Variable creation and named them all
painter = trtl.Turtle()
wn = trtl.Screen()
wn.title("Pong Game")
wn.setup(width = 1000, height = 600)
painter.screen.bgcolor('black')

# This is for the creation of the middle lines of the ping game which show which side its on
def middle_lines():
    painter.color('white')
    painter.hideturtle()
    painter.penup()
    painter.setpos(0,300 )
    painter.setheading(270)
    painter.pensize(5)
    for middle_lines in range (30):
        painter.pendown()
        painter.forward(10)
        painter.penup()
        painter.forward(10)
middle_lines()

# This is for the first paddle that's used in the game just to create it
paddle_a = trtl.Turtle()
paddle_a.speed('fastest')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid = 6, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-450,0)
paddle_a.left(180)

# This is for the second paddle that's used in the game just to create it
paddle_b = trtl.Turtle()
paddle_b.speed('fastest')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid = 6, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(450,0)

# Creation of ball and used dx and dy which when I looked it up said that dx and dy are the amount of change over a specific amount of time
ball = trtl.Turtle()
ball_speed_x = 20
ball_speed_y = 20
ball.speed('fastest')
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = rand.choice([1,-1]) * 0.2 #this is the balls randomized x direction
ball.dy = rand.choice([1,-1]) * 0.2 #this is balls randomized y direction

# Score
score_a = 0
score_b = 0

# Score display
score_display = trtl.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Arial", 24, "bold"))

# Paddle movement
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        paddle_b.sety(y - 20)
# this locks the paddle within the range of the window so it cant go offscreen

# Keyboard readings and functions for moving the paddle
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Updating the scoreboard
def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Arial", 24, "bold"))

#Main game coding
while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Bounce off the top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
    # Left paddle collision
    if (-440 < ball.xcor() < -430) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.dx *= -1
    # Right paddle collision
    if (430 < ball.xcor() < 440) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.dx *= -1
    # Ball goes out on the left
    if ball.xcor() < -500:
        score_b += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1
    # Ball goes out on the right
    if ball.xcor() > 500:
        score_a += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1




wn.listen()
wn.mainloop()