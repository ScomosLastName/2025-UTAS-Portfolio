"""
5.3PP Test template
"""

__author__ = "YOUR NAME"


def main():
    # TODO Paste the code here
    CAPACITY: int = 10 # warn if number of people is above this
    occupants: int # the current number of occupants

    occupants = int(input("Enter current number of occupants: "))
    if occupants > CAPACITY:
        print(f"The safe number of occupants has been exceeded!")
        print(f"The maximum number of occupants is {CAPACITY}.")
        
        
if __name__ == "__main__":
    main()