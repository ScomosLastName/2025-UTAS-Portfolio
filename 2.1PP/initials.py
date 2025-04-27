"""
KIT101 2.1PP Turtle Graphics

Turtle Graphics task to draw the author's initials.
Some of the code below has been _over_ commented to help
you understand what is happening.
"""

__author__ = "Samuel Morriss"

import turtle as painter

def main():
    
    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    painter.shape('turtle')
    painter.speed(0)
    painter.Screen().bgcolor("black")
    
    #changing line width
    painter.width(5)
    painter.color("Green")
    
    # Draw your initials below, remembering to use painter.penup() to
    # move without drawing a line...
    
    # Draw S
    painter.penup()
    painter.left(90)
    painter.forward(30)
    painter.left(90)
    painter.forward(50)
    painter.right(90)
    painter.pendown()
    painter.circle(50, 180, 20)
    painter.left(40)
    painter.forward(150)
    painter.penup()
    painter.right(40)
    painter.right(90)
    painter.forward(100)
    painter.left(90)
    painter.pendown()
    painter.circle(50, 180, 20)
    
    # Draw M
    painter.penup()
    painter.right(180)
    painter.forward(50)
    painter.left(90)
    painter.forward(20)
    painter.left(90)
    painter.pendown()
    painter.forward(211)
    painter.right(150)
    painter.forward(106)
    painter.left(120)
    painter.forward(106)
    painter.right(150)
    painter.forward(211)
    
    # Turtle moves over and does a celebratory dance
    painter.penup()
    painter.left(90)
    painter.forward(30)
    
    painter.speed(2)
    painter.right(720)


    # Avoid closing the window automatically
    painter.mainloop()


if __name__ == "__main__":
    main()
