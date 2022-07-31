# Library warrior
# Functions Included in Library: 
#   get_warrior_profile
#   build_warrior_profile
#   displa_warrior_status()
# Author: Michael Navarro
# Date: 12/10/20
# Revised: 

# list libraries used

# Declare global constants (name in ALL_CAPS)
NAME = 0
ENERGY = 1
STRENGTH = 2
SPEED = 3
LOCATION = 4
DIRECTION = 5

WARRIOR_RECORD_SIZE = 6

# Function get_warrior_profiles()
# Description:
#   Reads data from file and returns a list of said data.
# Calls:
#   range()
#   isdigit()
#   append()
#   len()
#   open()
#   readlines()
# Parameters:
#   filename     str
# Returns:
#   buffer
def get_warrior_profiles(filename):
    # Declare Local Variable types (NOT parameters)
    buffer = list()
    file_lines = list()

    # Open and read from file
    try:
        with open(filename, 'r') as stat_file:
            file_lines = stat_file.readlines()
            # Remove newline character from stats.
            for line in file_lines:
                buffer.append(line.replace('\n', ''))
            # End for
        # End with    
    except:
        buffer.append('Error')
    # End try

    # Return the return variable, if any
    return buffer
# End Function get_warrior_profiles()

# Function build_warrior_profile()
# Description:
#   Takes in a list of stats and a warrior number
#      and assigns stas accordingly.
# Calls:
#   none
# Parameters:
#   buffer          list
#   warrior_num     int
# Returns:
#   <return variable>
def build_warrior_profile(buffer, warrior_num): 
    # Declare Local Variable types (NOT parameters)
    warrior_profile = list()

    if warrior_num == 1:
        warrior_profile = buffer[:WARRIOR_RECORD_SIZE]
    else:
        warrior_profile = buffer[WARRIOR_RECORD_SIZE:]
    # End if

    # Convert numeric values into integers using CONSTANTS
    warrior_profile[ENERGY] = int(warrior_profile[ENERGY])
    warrior_profile[STRENGTH] = int(warrior_profile[STRENGTH])
    warrior_profile[SPEED] = int(warrior_profile[SPEED])
    warrior_profile[LOCATION] = int(warrior_profile[LOCATION])

    # Return the return variable, if any
    return warrior_profile
# End Function build_warrior_profile()

# Function display_warrior_status()
# Description:
#   Displays the stats of a warrior
# Calls:
#   title()
# Parameters:
#   warrior_profile     list
# Returns:
#   none
def display_warrior_status(warrior_profile):
    # Declare Local Variable types (NOT parameters)

    print(f'{warrior_profile[NAME].title()}: Energy {warrior_profile[ENERGY]}, Strength {warrior_profile[STRENGTH]}, Speed {warrior_profile[SPEED]}, Direction {warrior_profile[DIRECTION]}, Location {warrior_profile[LOCATION]}.')

    # Return the return variable, if any

# End Function display_warrior_status()

# Function move_warrior()
# Description:
#   Moves a warrior and adjusts their energy and strength
# Calls:
#   none
# Parameters:
#   moving_warrior     list
#   other_warrior      list
# Returns:
#   moving_warrior
def move_warrior(moving_warrior, other_warrior):
    # Declare Local Variable types (NOT parameters)

    # Change location and, if need be, direction.
    for step in range(moving_warrior[SPEED]):
        if moving_warrior[DIRECTION] == 'right':
            moving_warrior[LOCATION] += 1
        else:
            moving_warrior[LOCATION] -= 1
        # End if

        # Check for collision
        if moving_warrior[LOCATION] == other_warrior[LOCATION]:
            if moving_warrior[DIRECTION] == 'right':
                moving_warrior[DIRECTION] = 'left'
                moving_warrior[LOCATION] -= 2
            else:
                moving_warrior[DIRECTION] = 'right'
                moving_warrior[LOCATION] += 2
            # End if
        # End if
    # End for

    # Adjust warrior's stats
    moving_warrior[ENERGY] -= moving_warrior[SPEED] ** 2
    moving_warrior[STRENGTH] -= moving_warrior[SPEED] * 2

    # Return the return variable, if any
    return moving_warrior
# End Function move_warrior()

# End Module warrior

