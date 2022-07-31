# Program CPA-5PE20
# Description: 
#   Number guessing game
# Author: Michael Navarro
# Date: 11/04/2020
# Revised: 
#   <revision date> 

# list libraries used
import random

# Declare global constants (name in ALL_CAPS)

def main():

    # Declare Variable types (EVERY variable used in this main program)
    play = str()
    answer = int()
    total_guesses = int()

    play = 'y'
    while play == 'y':
        answer = random.randint(0, 100)
        total_guesses = guess_nbr(answer)

        print(f'\nCongratulations!!, you guessed the number in {total_guesses} tries!')
        play = input('Enter "Y" to play again or anything else to quit: ').lower()
    # end while
# End Program

def guess_nbr(ans):
    # Declare Local Variable types (NOT parameters)
    guess = int()
    num_guesses = int()

    num_guesses = 0
    guess = -1
    while guess != ans:
        guess = int(input('\nPlease enter your guess as an integer: '))

        if guess > ans:
            print('Too high, try again.')
        else:
            print('Too low, try again.')
        
        num_guesses += 1

    return num_guesses
    # end while

# End Function guess_nbr()
main()