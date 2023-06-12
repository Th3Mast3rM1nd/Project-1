"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

def start_game():
    # making a random number using the random.randrange function 
    random_number = random.randrange(1,12)
    user_input = 0
    count = 1
    while ( user_input != random_number):
        try:
            # Asking The User to Enter a number 
            user_input = int(input(("Enter your guessed Number Bettwen 1-12 ")))
            try:
                if ( user_input > 12 or user_input <= 0 ):
                    # rasing an Exception if The User Enter a Number not on the Range
                    raise Exception("This number is outside the range 1-12 ")
            except Exception as err:
                print(err)
            else:
                # checking if random number is lower than the input number 
                if ( random_number < user_input):
                    print("It's lower")
                    # we add 1 to the count var to keep track of attempts 
                    count += 1
                # checking if the random number is higher than the input number 
                elif ( random_number > user_input):
                    print("It's higher")
                    # we add q to the count var to keep track of attempts
                    count +=1
                else:
                    # if the random number equal the input number we let the User know 
                    print("You Got it")
                    print(f"Total attempts : {count}")
                    # safe the value of count which is the number of attempts to the var score 
                    score = count
                    break
        # we add an exception if the Value of the Input number not a Intger and we let the user try again 
        except ValueError:
            print("Only Integer are allowed, try Again Please ")
    # Return the Score Value when the function ends to keep track of the score if the user want to play again 
    return score

# we print a message welcoming the User to the Game 
print('WELCOME TO THE NUMBER GUESSING GAME')

# we set the Value of attempts Var to the return value of the Function start_game
attempts = start_game()
flag = 1
# we start a while loop as long as the flag Value dosent equal 0
while (flag != 0):
    high_score = attempts
    # we ask the User if want to play again and we convert the valeu to lower case 
    play_again = input("Would you like to play Again (yes|no) : ").lower()
    if ( play_again == "yes"):
        # we display the last number of attempts the user
        if (attempts <= high_score):
            print(f"High Score is : {attempts} ")
            attempts = start_game()
        else:
            print(f"High Score is : {high_score} ")
            attempts = start_game()
    else:
        # otherwise we thank the user and display his last Score
        print(f"Thanks For playing The Game , Your Final Score is {attempts}")
        # set the value of flag to 0 and end the Loop
        flag = 0


