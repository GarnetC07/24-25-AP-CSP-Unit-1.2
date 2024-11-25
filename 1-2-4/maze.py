import turtle

# Initialize the screen and the turtle
wn = turtle.Screen()
wn.bgcolor("white")

# Create the turtle
maze_painter = turtle.Turtle()
maze_painter.shape("turtle")
maze_painter.speed(10)  # Set the speed of the turtle

# Configuration variables
size = 20  # Starting size of the square
path_width = 10  # Width between the squares
iterations = 20  # Number of iterations (squares)

# Draw the spiral of squares
for i in range(iterations):
    # Draw the square
    for _ in range(4):
        maze_painter.forward(size)
        maze_painter.right(90)

    # Increase the size of the square for the next iteration
    size += path_width

# Hide the turtle after drawing
maze_painter.hideturtle()

# Keep the window open
wn.mainloop()
