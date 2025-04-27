"""
4.1PP Selection and Repetition
"""

__author__ = "Samuel Morriss"

import timeit  # Used for timing the execution of code
from random import randint  # Used for generating random values


def display_title(title: str):

    """
    Displays the given title in ALL CAPS, underlined by plus (*) symbols,
    and followed by a blank line.
    """
    
    underline: str = ""
    
    for i in title:
        underline += "+"
    print(title.upper())
    print(underline)
    print()


def check_answer(num1: int, num2: int) -> bool:
    """
    Tests the user's ability to answer a given subtraction problem.
    Provides feedback and returns True if correct, False otherwise.
    """
    user_input: int  # The user's typed answer
    
    user_input = int(input(f"What is {num1} - {num2}? "))

    if num1 - num2 == user_input:  # Return true if the users answer is correct
        print("Correct!")
        print()
        return True
    else:
        print(f"Incorrect. The correct answer was {num1 - num2}")
        print()
        return False


def start_quiz(max_value: int, target_correct: int) -> int:
    """
    Runs the math tutorial where the user must answer subtraction problems
    correctly until reaching the required number of correct answers.
    Returns the total number of attempts.
    """
    attempts = 0  # Total number of attempts
    correct = 0  # Total number of correct answers
    
    while correct < target_correct:
        first_number = randint(0, max_value) #get first random number to ensure second is less than
        if check_answer(first_number, randint(0, first_number)) == True:
            correct += 1
        attempts += 1

    return attempts


def main():
    MAX_VALUE = 20  # Maximum operand value of random numbers
    REQUIRED_CORRECT = 5  # Number of correct answers required
    start_time: float  # Start time of quiz
    end_time: float  # End time of quiz
    total_attempts: int  # Total number of attempts made

    display_title("Math Quiz")
    print("Solve the subtraction problems as quickly as possible!")
    print(f"You must answer {REQUIRED_CORRECT} problems correctly to finish.")
    print(f"The numbers will be between 1 and {MAX_VALUE}.")
    print()

    # Start the quiz
    input("Press Enter to begin the timed test...")
    start_time = timeit.default_timer()
    total_attempts = start_quiz(MAX_VALUE, REQUIRED_CORRECT)
    end_time = timeit.default_timer()

    # Display performance results
    print()
    print("Total Attempts:", total_attempts)
    print(f"Accuracy: {(100 * REQUIRED_CORRECT / total_attempts):.1f}%")
    print(f"Total Time: {(end_time - start_time):.1f} seconds")
    print()
    display_title("Keep Practicing!")


if __name__ == "__main__":
    main()