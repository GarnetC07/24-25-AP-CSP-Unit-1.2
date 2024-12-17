import turtle as trtl
import random as rand

# Screen setup
screen = trtl.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=1000, height=600)
painter = trtl.Turtle()

# Painter for middle line
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

# Left Paddle Setup
left_paddle = trtl.Turtle()
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-450, 0)
left_paddle.right(180)

# Right Paddle Setup
right_paddle = trtl.Turtle()
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(450, 0)

# Ball Setup and gives the ball a random speed on x and y as well as starts it off always in the middle
ball = trtl.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.x_direction = rand.choice([1, -1]) * 2
ball.y_direction = rand.choice([1, -1]) * 2

# Set score to start at 0
left_score = 0
right_score = 0

# Score font and display
score_display = trtl.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Left Player: 0  Right Player: 0", align="center", font=("Arial", 24, "bold"))

# for moving and locking paddle to the screen as well as how far it moves per key press
def move_left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        left_paddle.sety(y + 30)

def move_left_paddle_down():
    y = left_paddle.ycor()
    if y > -250:
        left_paddle.sety(y - 30)

def move_right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        right_paddle.sety(y + 30)

def move_right_paddle_down():
    y = right_paddle.ycor()
    if y > -250:
        right_paddle.sety(y - 30)

# Key movement to move left and right paddle
screen.listen()
screen.onkeypress(move_left_paddle_up, "w")
screen.onkeypress(move_left_paddle_down, "s")
screen.onkeypress(move_right_paddle_up, "Up")
screen.onkeypress(move_right_paddle_down, "Down")

# Updates the score being shown
def update_score():
    score_display.clear()
    score_display.write(f"Left Player: {left_score}  Right Player: {right_score}", align="center", font=("Arial", 24, "bold"))

# Main Game Loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.x_direction)
    ball.sety(ball.ycor() + ball.y_direction)

    # Bounce off top and bottom walls of the screen
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.y_direction = -ball.y_direction

    # Left Paddle bounce the ball
    if (-440 < ball.xcor() < -430) and (left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.x_direction = -ball.x_direction

    # Right paddle bounce the ball
    if (430 < ball.xcor() < 440) and (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.x_direction = -ball.x_direction

    # If the ball goes out then it starts in middle and goes in random direction whilst updating score
    if ball.xcor() < -500:
        right_score += 1
        update_score()
        ball.goto(0, 0)
        ball.x_direction = rand.choice([1, -1]) * 4
        ball.y_direction = rand.choice([1, -1]) * 4

    # Ball goes out on the right resets it in middle and updates the score
    if ball.xcor() > 500:
        left_score += 1
        update_score()
        ball.goto(0, 0)
        ball.x_direction = rand.choice([1, -1]) * 4
        ball.y_direction = rand.choice([1, -1]) * 4

wn.listen()
wn.mainloop()