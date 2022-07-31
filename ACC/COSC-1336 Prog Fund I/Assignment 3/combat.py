# Program Combat 
# Description: 
#   Simulates the battle between two warriors and announces the one(s) who perished.
# Author: Michael Navarro 
# Date: 11/25/20
# Revised:     
    # 12/03/2020
# list libraries used
import warrior

# Declare global constants (name in ALL_CAPS)
FILENAME = 'warriors.txt'

def main():

    # Declare Variable types (EVERY variable used in this main program)
    both_energized = bool()
    game_time = int()

    # Warrior 1 stats
    warrior1_strength = int()
    warrior1_energy = int()
    warrior1_speed = int()
    warrior1_location = int()
    field_warrior1 = int()

    warrior1_direction = str()
    warrior1_name = str()

    # Warrior 2 stats
    warrior2_strength = int()
    warrior2_energy = int()
    warrior2_speed = int()
    warrior2_location = int()
    field_warrior2 = int()

    warrior2_direction = str()
    warrior2_name = str()

    # Open file with the status values
    with open(FILENAME, 'r') as warriors:
        # Assign values to warrior 1's stats
        warrior1_name = warriors.readline().title().strip()
        warrior1_energy = int(warriors.readline())
        warrior1_strength = int(warriors.readline())
        warrior1_speed = int(warriors.readline())
        warrior1_location = int(warriors.readline())
        warrior1_direction = warriors.readline().strip()

        # Assign values to warrior 2's stats
        warrior2_name = warriors.readline().title().strip()
        warrior2_energy = int(warriors.readline())
        warrior2_strength = int(warriors.readline())
        warrior2_speed = int(warriors.readline())
        warrior2_location = int(warriors.readline())
        warrior2_direction = warriors.readline().strip()
    # end with block

    # -------------------- Play --------------------

    game_time = 0

    # Sync location variables
    field_warrior1 = warrior1_location
    field_warrior2 = warrior2_location

    # Display initial game state
    print(f'\nTimes is: {game_time}')    
    warrior.display_warrior_status(warrior1_name, warrior1_energy, warrior1_strength, warrior1_speed, warrior1_direction, warrior1_location)
    warrior.display_warrior_status(warrior2_name, warrior2_energy, warrior2_strength, warrior2_speed, warrior2_direction, warrior2_location)

    # Realize loop condition
    both_energized = True
    while (both_energized == True):
        
        # 1. Move Warriors
        warrior1_location = warrior.move_warrior(warrior1_speed, warrior1_direction, warrior1_location, warrior2_location)
        # Check to see if direction was reversed (location returend will be negative)
        if (warrior1_location < 0):
            if (warrior1_direction == 'left'):
                warrior1_direction = 'right'
            else:
                warrior1_direction = 'left'
            # End if
            warrior1_location = abs(warrior1_location) 
        #End if

        warrior2_location = warrior.move_warrior(warrior2_speed, warrior2_direction, warrior2_location, warrior1_location)
        # Check to see if direction was reversed (location returend will be negative)
        if (warrior2_location < 0):
            if (warrior2_direction == 'left'):
                warrior2_direction = 'right'
            else:
                warrior2_direction = 'left'
            #End if
            warrior2_location = abs(warrior2_location) 
        #End if

        # 2. Update/Sync game variables
        field_warrior1 = warrior1_location
        field_warrior2 = warrior2_location

        game_time += 1

        warrior1_energy -= warrior1_speed ** 2
        warrior2_energy -= warrior2_speed ** 2
        warrior1_strength -= warrior1_speed * 2
        warrior2_strength -= warrior2_speed * 2

        # 3. Display current game state
        print(f'\nTimes is: {game_time}')    
        warrior.display_warrior_status(warrior1_name, warrior1_energy, warrior1_strength, warrior1_speed, warrior1_direction, warrior1_location)
        warrior.display_warrior_status(warrior2_name, warrior2_energy, warrior2_strength, warrior2_speed, warrior2_direction, warrior2_location)

        # 4. Check the energy status
        if(warrior1_energy <= 0 or warrior2_energy <= 0):
            both_energized = False
        # End if

    # Final Report
    if(warrior1_energy <= 0 and warrior2_energy <= 0):
        print(f'\nBoth {warrior1_name} and {warrior2_name} have perished.')
    elif(warrior1_energy <= 0):
        print(f'\n{warrior1_name} has been defeated.')
    elif(warrior2_energy <= 0):
        print(f'\n{warrior2_name} has been defeated.')
    else:
        print('\nERROR')
    # end if

# End Program

main()
