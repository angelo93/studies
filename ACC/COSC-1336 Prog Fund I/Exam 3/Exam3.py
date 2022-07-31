# Program Exam3
# Description: 
#   Simulates an RPG with two warriors fighting. 
# Author: Michael Navarro
# Date: 12/10/20
# Revised: 
# 
# list libraries used
import warrior

# Declare global constants (name in ALL_CAPS)
NAME = 0
ENERGY = 1
STRENGTH = 2
SPEED = 3
LOCATION = 4
DIRECTION = 5
WARRIOR_RECORD_SIZE = 6

FILENAME = 'warriors.txt'

def main():
    # Declare Variable types (EVERY variable used in this main program)
    warrior1 = list()
    warrior2 = list()
    buffer = list()

    both_alive = bool()

    game_time = int()

    # 1. Build warriors
    buffer = warrior.get_warrior_profiles(FILENAME)

    warrior1 = warrior.build_warrior_profile(buffer, 1)
    warrior2 = warrior.build_warrior_profile(buffer, 2)

    # 2. Display starting stats
    game_time = 0 
    print(f'\nGame Time: {game_time}')

    warrior.display_warrior_status(warrior1)
    warrior.display_warrior_status(warrior2)

    # 3. -------------------- PLAY GAME--------------------
    both_alive = True
    while (both_alive == True):
        # Update time and warrior stats
        game_time += 1

        warrior1 = warrior.move_warrior(warrior1, warrior2)
        warrior2 = warrior.move_warrior(warrior2, warrior1)

        # Display current game stats
        print(f'\nGame Time: {game_time}')
        warrior.display_warrior_status(warrior1)
        warrior.display_warrior_status(warrior2)

        # Check for deaths
        if (warrior1[ENERGY] <= 0 or warrior2[ENERGY] <= 0):
            both_alive = False
        # End if
    # End while

    # 4. Death report
    if(warrior1[ENERGY] <= 0 and warrior2[ENERGY] <= 0):
        print(f'\nBoth {warrior1[NAME].title()} and {warrior2[NAME].title()} have perished.')
    elif(warrior1[ENERGY] <= 0):
        print(f'\n{warrior1[NAME].title()} has been defeated.')
    elif(warrior2[ENERGY] <= 0):
        print(f'\n{warrior2[NAME].title()} has been defeated.')
    else:
        print('\nERROR')
    # end if

# End Program
main()
