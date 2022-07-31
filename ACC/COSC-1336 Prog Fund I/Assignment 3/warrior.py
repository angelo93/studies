# Function display_warrior_status()
# Description:
#   Displays the current status of a given warrior
# Calls:
#   N/A
# Parameters:
#   name        str
#   energy      int
#   strength    int
#   speed       int
#   direction   str
#   location    int
# Returns:
#   N/A

def display_warrior_status (name, energy, strength, speed, direction, location):
    
    print(f'{name}: (Energy {energy}, Strength {strength}, Speed {speed}, Direction {direction}) at location {location}.')
# End Function display_warrior_status ()

# Function move_warrior ()
# Description:
#   Moves a given warrior and checks if there is a collision
# Calls:
#   N/A
# Parameters:
#   speed             int
#   direction         str
#   location          int
#   other_location    int
# Returns:
#   new_location      int

def move_warrior (speed, direction, location, other_location):
    new_location = int()
    loc_reversed = bool()

    new_location = location
    loc_reversed = False
    for step in range(speed):
        # Move current warrior
        if (direction == 'left'):
            new_location -= 1
        else:
            new_location += 1
        # End if

        # Check to see if there is a collision
        if (new_location == other_location):
            loc_reversed = True
            # A value of two is used to reverse the previous arithmetic and take a step in the corrected direction
            if (direction == 'left'):
                direction = 'right'
                new_location += 2
            else:
                direction = 'left'
                new_location -= 2
            # End if
        # End if

    if (loc_reversed == True):
        new_location = -new_location

    return new_location
# End Function move_warrior ()