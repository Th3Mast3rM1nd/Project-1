"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
# installing the cowsay library """pip install cowsay"""
import cowsay
import random

def start_game():
    random_number = random.randrange(1,12)
    user_input = 0
    count = 1
    while ( user_input != random_number):
        try:
            user_input = int(input(("Enter your guessed Number Bettwen 1-12 ")))
            try:
                if ( user_input > 12 ):
                    raise Exception("This number is outside the range 1-12 ")
            except Exception as err:
                print(err)
            else:
                if ( random_number < user_input):
                    print("It's lower")
                    count += 1
                elif ( random_number > user_input):
                    print("It's higher")
                    count +=1
                else:
                    print("You Got it")
                    print(f"Total attempts : {count}")
                    score = count
                    break
        except ValueError:
            print("Only Integer are allowed, try Again Please ")
    return score


print(cowsay.get_output_string('tux', 'WELCOME TO THE NUMBER GUESSING GAME'))

score = start_game()
flag = 1
while (flag != 0):
    play_again = input("Would you like to play Again (yes|no) : ").lower()
    if ( play_again == "yes"):
        print(f"Last Score {score} ")
        score = start_game()
    else:
        print(f"Thanks For playing The Game , Your Final Score is {score}")
        
        flag = 0


