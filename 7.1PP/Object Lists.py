"""
7.1PP Recording Directions
"""

__author__ = "Samuel Morriss"
from dataclasses import dataclass
from enum import Enum
from user_input_functions import * #Custom input functons

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
    landmark: str | None = None
      
    def __str__(self) -> str:
        Output: str
            
        if self.landmark == None:
            Output = f"{self.direction.value}, {self.distance} meters, you will climb {self.elevation} meters and will finish at {self.landmark}."
        else:
            Output = f"{self.direction.value}, {self.distance} meters, you will climb {self.elevation} meters."
        return Output

    

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
    landmark = input('What should they see then they arrive? (Leave blank if not applicable) ').strip().lower()
    
    output = Direction(direction, distance, elevation, landmark)
    
    return output


def shortest_distance(directions: list[Direction], direction: Compass) -> float:
    """
    Calculate the shortest distance of a list of directions
    """
    
    shortest: float = 0.0
    
    for i in directions:
        if i.direction == direction:
            if shortest == 0.0 or i.distance < shortest:
                shortest = i.distance
            
    return shortest


def total_distance(directions: list[Direction], direction: Compass) -> float:
    """
    Calculate the total distance of a list of directions
    """
    
    total: float = 0.0
    
    for i in directions:
        if i.direction == direction:
            total += i.distance
        
    return total


def display_all(directions: list[Direction]) -> None:
    """
    Display all directions in a list of directions
    """
    print()
                
    index = 1
    for i in directions:
        print(f"{index}. {i}")
        index += 1
        
def add_many(directions: list[Direction]) -> None:
    """
    Add many directions to a list of directions
    """
    amount: int = input_int("How many directions do you want to add? ", 0)
    
    for i in range(amount):
        if i != 0:
            if input_bool("Would you like to stop early? "):
                break
            else:
                directions.append(input_direction())
        else:
            directions.append(input_direction())
    
    
def main():
    choice = 0
    directions: list[Direction] = []
    
    while choice < 6:
        print()
        print("1. Add Directions")
        print("2. Display All Directions")
        print("3. Clear Directions")
        print("4. Total Distance in any direction")
        print("5. Shortest Distance in any direction")
        print("6. Quit")
        
        choice = input_int("Action: ", 1, 6)      
        match choice:
            case 1:
                add_many(directions)
            case 2:
                display_all(directions)
            case 3:
                if input_bool("Are you sure? "):
                    for i in range(len(directions)):
                        directions.pop()
            case 4:
                print(f"Total Distance: {total_distance(directions, input_compass())}")
            case 5:
                print(f"Shortest Distance: {shortest_distance(directions, input_compass())}")
            case _:
                break
    
if __name__ == '__main__':
    main()