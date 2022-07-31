# Program Basic function
# Description: 
#   Calls a simple function
# Author: Michael Navarro
# Date: 11/10/2020
# Revised: 
#   <revision date> 

# list libraries used
import random
# Declare global constants (name in ALL_CAPS)

def main():
    
    # Declare Variable types (EVERY variable used in this main program)
    current_results = list()
    human_choice = str()
    computer_choice = str()

    current_results = ['tie.']

    while current_results[0] == 'tie.':
        human_choice = human_play()
        computer_choice = computer_play()
        
        current_results = winner(human = human_choice, computer = computer_choice)
    # end while

    print(f'\n{current_results[0]}')
    print(f'{current_results[1].title()} wins!')

# End Program

# Function computer_play()
# Description:
#   generate a random # 1-3
#   assign rock, paper or scissors
# Calls:
# Parameters:
# Returns:      rock/paper/scissors

# Function human_play()
# Description:
#   show menu with items # 1-3
#   choose rock, paper or scissors
# Calls:
# Parameters:
# Returns:      choice

# Function winner(computer, human)
# Description:
#   determine winner or tie
# Calls:
# Parameters:
# Returns:      match_result

def computer_play ():
    # Declare Local Variable types (NOT parameters)
    computer_choice = str()
    generator = int()

    generator = random.randint(1,3)

    if generator == 1:
        computer_choice = 'rock'
    elif generator == 2:
        computer_choice = 'paper'
    else:
        computer_choice = 'scissors'
    # end if

    # Return the return variable, if any
    return computer_choice

def human_play ():
    # Declare Local Variable types (NOT parameters)
    human_choice = str()
    option = str()
    options = list()

    options = ['1', '2', '3']
    option = 'choosing'

    while option not in options:
        print('\n1. rock')
        print('2. paper')
        print('3. scissors')
        option = input('Please input the number of your choice: ')
    # end while

    if option == '1':
        human_choice = 'rock'
    elif option == '2':
        human_choice = 'paper'
    else:
        human_choice = 'scissors'
    # end if

    # Return the return variable, if any
    return human_choice

def winner (computer, human):
    # Declare Local Variable types (NOT parameters)
    choices = list()
    results = list()
    match_result = str()
    winning_choice = str()
    winner = str()

    results = []
    choices = [computer, human]

    if 'rock' in choices and 'scissors' in choices:
        match_result = 'Rock smashes scissors.'
        winning_choice = 'rock'
    elif 'scissors' in choices and 'paper' in choices:
        match_result = 'Scissors cuts paper.'
        winning_choice = 'scissors'
    elif 'paper' in choices and 'rock' in choices:
        match_result = 'Paper wraps rock.'
        winning_choice = 'paper'
    else:
        match_result = 'tie.'
        print('\nTie!! Play again!')
    # end if

    if computer == winning_choice:
        winner = 'computer'
    else:
        winner = 'human'
    # end if

    results.append(match_result)
    results.append(winner)

    # Return the return variable, if any
    return results

# End Function computer_play(computer, human)


main()
