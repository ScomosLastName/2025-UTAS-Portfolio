"""
Commonly Used Functions for user input
"""

__author__ = "Samuel Morriss"

def input_int(query: str, min: int | None = None, max: int | None = None) -> int:
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
      
            
def input_float(query: str, min: float | None = None, max: float | None = None) -> float:
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
    return output


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