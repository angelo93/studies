# Program Basic function
# Description: 
#   Calls a simple function
# Author: Michael Navarro
# Date: 11/09/2020
# Revised: 
#   <revision date> 

# list libraries used
import random
# Declare global constants (name in ALL_CAPS)

def main():
    # Declare Variable types (EVERY variable used in this main program)
    num_loops = int()
    correct_ans = int()
    do_math = str()

    do_math = input('Enter "Y" to solve some math problems or anything else pass: ').lower()

    num_loops = 0
    correct_ans = 0
    while do_math == 'y':
        num_loops += 1
        correct_ans += problem()
        do_math = input('\nEnter "Y" to solve some more problems or anything else to quit: ').lower()

    print(f'\nQuestions asked: {num_loops}')
    print(f'Questions correctly answered: {correct_ans}')
# End Program

# Function problem()
# Description:
#   prints a simple string
# Calls:
# Parameters:
#   phrase     string
# Returns:
#   phrase

def problem ():
    # Declare Local Variable types (NOT parameters)
    point = int()
    num1 = int()
    num2 = int()
    ans = int()
    user_ans = int()

    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999)
    ans = num1 + num2

    print(f'   {num1}')
    print(f'+  {num2}')
    print('--------')

    user_ans = int(input(f'\nWhat is {num1} + {num2}? '))

    if user_ans == ans:
        print('Correct!')
        point = 1
    else:
        print('So close!')
        point = 0

    # Return the return variable, if any
    return point
# End Function problem()

main()
