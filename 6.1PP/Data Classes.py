"""
6.1PP Recording a Direction
"""

__author__ = "Samuel Morriss"
from dataclasses import dataclass
from enum import Enum

class Compass(Enum):
    """
    Directions on a compass
    """
    
    N = "North"
    E = "East"
    S = "South"
    W = "West"
    

@dataclass
class Direction:
    """
    A instruction in a list of directions
    """
    direction: Compass
    distance: float
    elevation: float
    landmark: str
      
    def __str__(self) -> str:
        Output: str
            
        if self.elevation >= 20.0:
            Output = f"{self.direction.value}, {self.distance} meters, you will climb {self.elevation} meters and will finish at {self.landmark}"
        else:
            Output = f"{self.direction.value}, {self.distance} meters, and will finish at {self.landmark}"
        return Output
    
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
            
    return output
            
                
def input_int(query: str, min: int = None, max: int = None) -> int:
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
    

def input_compass() -> Compass:
    """
    Take user imput for a Compass attribute
    """
    
    output: Compass
    
    print("Input Direction")
    print(f"1. North")
    print(f"2. East")
    print(f"3. South")
    print(f"4. West")
    
    match  input_int("Choose a direction (1-4): ", 1, 4):
        case 1:
            output = Compass.N
        case 2:
            output = Compass.E
        case 3: 
            output = Compass.S
        case 4:
            output = Compass.W
        
    return output
        
    
def input_direction() -> Direction:
    """
    Take user input for a Direction
    """
    direction: Compass
    distance: float
    elevation: float
    landmark: str
    
    print("What way should they go?")
    direction = input_compass()
    distance = input_float("How far should they walk? ")
    elevation = input_float("How far up us it? ")
    landmark = input('What should they see then they arrive? ')
    
    output = Direction(direction, distance, elevation, landmark)
    
    return output
    
def main():
    print(input_direction())
    
if __name__ == '__main__':
    main()