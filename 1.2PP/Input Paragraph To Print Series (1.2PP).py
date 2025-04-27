"""
Input Paragraph To Print Series
1.2PP
"""

__author__ = "Samuel Morriss"

def main():
    x = input()
    inp = []
    while x != '': # Convert Lines into seperate list elements 
        inp.append(x)
        x = input()

    for i in inp: # Add Print() to each line and output them to the terminal to be Copyed
        print('print("' + i +'")')

if __name__ == "__main__":
    main()