'''
3.4CR Turtle Stamps

Implements a reusable 'stamp' that can draw the author's initials at
any location on the Turtle Graphics window.
'''

__author__ = "Samuel Morriss"

import turtle as t
from random import randint

speed = 3

window_width = 1000
window_height = 700

def place_stamp(color: str):
    """
    Method to draw a stamp of the authors initals and date written.
    """
    
    origin = t.pos()
    
    width = 435
    height = 250
    t.penup()
    t.speed(3)
    
    t.seth(0)
    t.left(90)
    t.forward(height)
    
    t.pendown()
    
    
    #  Draw the boarder box
    t.color(color)
    t.seth(0)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.penup()
    
    #  Draw S
    t.backward(height - 50)
    t.right(90)
    t.forward(110)
    t.left(90)
    t.forward(115)
    t.pendown()
    t.circle(50, 180, 20)
    t.left(40)
    t.forward(150)
    t.penup()
    t.right(40)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.pendown()
    t.circle(50, 180, 20)
    
    # Draw M
    t.penup()
    t.right(180)
    t.forward(50)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.pendown()
    t.forward(211)
    t.right(150)
    t.forward(106)
    t.left(120)
    t.forward(106)
    t.right(150)
    t.forward(211)
    
    #  Draw Date
    t.left(90)
    t.forward(30)
    t.write("20 3 25", True, "left", font=("Verdana",
                                    30, "normal"))

    t.penup()
    t.goto(origin)
    
    t.speed(speed)
    

def random_position(width: int, height: int) -> tuple:
    """
    Find a Random position in the given area.
    """
    location = (randint(-abs(width // 2), width // 2 - 435), randint(-abs(height // 2) , height // 2 - 250))
    print(location)
    return location
    
    
def main():
    screen = t.Screen()
    screen.title('Turtle Stamp')
    screen.setup(width=window_width, height=window_height)
        
    t.penup()
    
    t.speed(speed)
    t.width(5)

    t.goto(random_position(window_width, window_height))
    place_stamp("Black")
    
    t.goto(random_position(window_width, window_height))
    place_stamp("Green")
    
    t.goto(random_position(window_width, window_height))
    place_stamp("Blue")
    
    #  Prevents the application from closing
    t.mainloop()
    

if __name__ == "__main__":
    main()