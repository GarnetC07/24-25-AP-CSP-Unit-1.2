#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
Drawer = trtl.Turtle()
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
ground_height = -200
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple():
  apple.goto(apple.xcor(), ground_height)

def draw_an_A():
  Drawer.color("blue")
  Drawer.write("A", font=("Arial", 74, "bold"))

#-----function calls-----
draw_apple(apple)

wn.onkeypress(drop_apple, "a")




wn.listen()
wn.mainloop()