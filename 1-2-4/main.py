import turtle as trtl

# Intialize Variables
wn = trtl.Screen()
maze_painter = trtl.Turtle()
length = 20
path_width = 20
# Setup Turtle
maze_painter.left(90)
maze_painter.pensize(5)
maze_painter.speed(0)

# Draw Maze
# Process:
# Draw a line
# Turn Left
# increment Length
# Repeat
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)

for i in range(21):
    maze_painter.forward(length/3)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    draw_barrier()
    maze_painter.forward(length - path_width - length/3)
    maze_painter.left(90)
    length += 15
























wn.listen()
wn.mainloop()