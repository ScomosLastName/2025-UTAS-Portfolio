"""
5.2PP Collection of Strings
"""

__author__ = "Samuel Morriss"

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

def check_list_contents(input_list: list[str], input: str) -> bool:
    """
    Check if a list contains a string
    """
    for i in input_list:
        if i == input:
            return True
    return False
        
    
    
def add_word(word_list: list[str], word: str):
    """
    Adds a new word to the word list if there is capacity and
    the word is not empty.
    """
    
    word = word.strip()
    
    if word != "":
        if check_list_contents(word_list, word) == True:
            print("Word is already in list")
        else:
            word_list.append(word)
    else:
        print("Empty words cannot be added!")


def display_entries(word_list: list[str]):
    """
    Displays all words in the word list, separated by a comma.
    """
    output = ""
    line = ""
    try:
        for i in range(len(word_list) - 1):
            output += word_list[i] + ", "
        output += word_list[len(word_list)- 1]
        for i in output:
            line += '*'
        print(line)
        print(output)
        print(line)
    except IndexError:
        print("List is empty")
        

def average_len(word_list: list[str]) -> str | float:
    """
    Calculates the average length of a list of words and returns the resualt as a float
    """

    word_lengths: list[int] = []
    average: float = 0
    
    for word in word_list:
        word_lengths.append(len(word))
        
    for i in word_lengths:
        average += i
    try:
        average = average / len(word_lengths)
        return average
    
    except ZeroDivisionError:
        return "No words in list!"

    
def main():   
    words: list[str] = []
    choice: int = 0
    new_word: str 
    
    print("Words!")
    while True:
        print()
        print("1. Add a word")
        print("2. Display entries")
        print("3. Display average word length")
        print("4. Clear words")
        print("5. Quit")
        
        choice = input_int("Action: ", 1, 5)      
        match choice:
            case 1:
                print()
                new_word = str(input("What word would you like to add? "))
                add_word(words, new_word)
            case 2:
                print()
                display_entries(words)
            case 3:
                print()
                print(average_len(words))
            case 4:
                print()
                for i in range(len(words)):
                    words.pop()
            case _:
                break

if __name__ == "__main__":
    main()
