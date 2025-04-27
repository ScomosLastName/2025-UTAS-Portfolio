"""
4.3CR User Input Functions
"""

__author__ = "Samuel Morriss"


def input_int(query: str, min = None, max = None) -> int:
    """
    Take user input for a value within the range of a 64-bit interger system.
    Ensures the user input is valid, if not asking for an input again.
    """
    
    output: int
    
    while True:
        try:
            output = int(input(query).strip())
            if min != None and max != None:
                if output < min or output > max:
                    print("Thats not a valid Number!")
                else:
                    break #  Break the loop to prevent program from looping forever
            elif min != None:
                if output < min:
                    print("Thats not a valid Number!")
                else:
                    break #  Break the loop to prevent program from looping forever
            elif max != None:
                if output > max:
                    print("Thats not a valid Number!")
                else:
                    break #  Break the loop to prevent program from looping forever
            else:
                break
                
        except:
            print("Thats not a valid Number!")
    
    return output
      
            
def input_float(query: str, min = None, max = None) -> float:
    """
    Take user input for a value within the range of a 64-bit float system.
    Ensures the user input is valid, if not asking for an input again.
    """
    
    output: float
    
    while True:
        try:
            output = float(input(query).strip())
            if min != None and max != None:
                if output < min or output > max:
                    print("Thats not a valid Number!")
                else:
                    break #  Break the loop to prevent program from looping forever
            elif min != None:
                if output < min:
                    print("Thats not a valid Number!")
                else:
                    break #  Break the loop to prevent program from looping forever
            elif max != None:
                if output > max:
                    print("Thats not a valid Number!")
                else:
                    break #  Break the loop to prevent program from looping forever
            else:
                break
                
        except:
            print("Thats not a valid Number!")


def input_bool(query: str) -> bool:
    """
    Take a boolean user input
    If input is not valid ask again
    """
    output: bool
    
    while True:
        user_input = str(input(query).lower().strip())
        
        if user_input in ["y", "yes", "true"]:
            output = True
            break #  Break the loop to prevent program from looping forever
        elif user_input in ["n", "no", "false"]:
            output = False
            break #  Break the loop to prevent program from looping forever
        else:
            print("That is not a valid input!")
            
    return output


if __name__ == "__main__":
    #All variables are initialised so code will run without error before all functions are implemented and called
    stars = -1     #user's star (between 0 and 5)
    volume = -1.0  #continuously variable speaker volume (as a value between 0 and 11)
    again = False  #do they want to try some action again?

    print("Testing input_int... the number should be saved in stars.")
    print(" - Enter '6' (should loop with error)")
    print(" - Enter '-1' (should loop with error")
    print(" - Enter '2' and it should work")
    stars = input_int("Rate the last movie you saw", 0, 5)
    print(f"Star rating: {stars}");
    print()

    print("Testing input_float... the number should be saved in volume.")
    print(" - Enter '20' (should loop with error)")
    print(" - Enter '-1' (should loop with error)")
    print(" - Enter '9.5' and it should work")
    volume = input_float("Enter amplifier volume", 0.0, 11.0)
    print(f"Volume: {volume}")
    print()

    print("Testing input_bool... the result is saved in again.")
    print(" - Extend these boolean tests by adding more messages to verify your solution!")
    print(" - Enter 'nah' and it should loop with error")
    print(" - Enter 'yes' and it should succeed")
    again = input_bool("Try again?")
    print(f"Again: {again}")
    print()
    print(" - Verify that it can also read in False...")
    again = input_bool("Try again?")
    print(f"Again: {again}")
    print()

    print("Tests complete...")
