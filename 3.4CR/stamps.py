"""
3.4CR Stamp Function

Implements a reusable 'stamp' that can draw the author's initials at
any location on the Turtle Graphics window.
"""

__author__ = "YOUR NAME"

from turtle import Turtle


def place_stamp(stamper: Turtle):
    """
    Draws the author's initials
    """
    # You will create the body of this function
    # and in Stage 2 change the header, too


def main():
    t = Turtle() # The turtle graphics object

    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    # t.speed(5)

    # You will call your function (eventually several times) here
    # For example, place_stamp(t) during Stage 1 of the task

    # Avoid closing the window automatically
    t.screen.mainloop()


if __name__ == "__main__":
    main()
