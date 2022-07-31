# Program combat
# Description:
#   Simple role playing game
# Author: Michael Navarro
# Date: 28 September 2020
# Revised:
#   29 September 2020
#   13 October 2020
# list libraries used

# Declare constants (name in ALL_CAPS)

# Declare Variable types (EVERY variable used)
red_strength = int()
red_energy = int()
red_speed = int()

blue_strength = int()
blue_energy = int()
blue_speed = int()

field_red = int()
field_blue = int()

temp_field_red = int()
temp_field_blue = int()

red_direction = str()
blue_direction = str()

time = int()
both_energized = bool()

# -------------------- Setup --------------------
red_strength = 45
red_energy = 100
red_speed = 5

blue_strength = 80
blue_energy = 150
blue_speed = 3

time = 0
both_energized = True

field_red = 0
field_blue = 15

temp_field_red = 0
temp_field_blue = 15

red_direction = 'right'
blue_direction = 'left'

# -------------------- Play --------------------
print(f'Time is {time}.')
print(
    f'Red strength is {red_strength}, energy is {red_energy}, speed is {red_speed}, location is {field_red}.')
print(
    f'Blue strength is {blue_strength}, energy is {blue_energy}, speed is {blue_speed}, location is {field_blue}.')

# Ensure loop is entered
both_energized = True
while(both_energized == True):
    # Equalize the variables to avoid discrepency
    temp_field_red = field_red
    temp_field_blue = field_blue

    # Move warriors
    if(red_direction == 'right'):
        temp_field_red += red_speed
    else:
        temp_field_red -= red_speed
    # end if

    if(blue_direction == 'right'):
        temp_field_blue += blue_speed
    else:
        temp_field_blue -= blue_speed
    # end if

    # Check to see if warriors collide
    if(temp_field_red == temp_field_blue):
        # Change direction and then move
        if(red_direction == 'right'):
            red_direction = 'left'
            field_red -= red_speed
        else:
            red_direction = 'right'
            field_red += red_speed
        # end if

        if(blue_direction == 'right'):
            blue_direction = 'left'
            field_blue -= blue_speed
        else:
            blue_direction = 'right'
            field_blue += blue_speed
        # end if
    else:
        field_red = temp_field_red
        field_blue = temp_field_blue
    # end if

    # Update both warrior's conditions
    time += 1
    red_energy -= red_speed ** 2
    blue_energy -= blue_speed ** 2
    red_strength -= red_speed * 2
    blue_strength -= blue_speed * 2

    # Print current game state
    print(f'\nTime is {time}.')
    print(
        f'Red strength is {red_strength}, energy is {red_energy}, speed is {red_speed}, location is {field_red}.')
    print(
        f'Blue strength is {blue_strength}, energy is {blue_energy}, speed is {blue_speed}, location is {field_blue}.')

    # Check the energy status
    if(red_energy <= 0 or blue_energy <= 0):
        both_energized = False
    # end if

# end while

if(red_energy <= 0 and blue_energy <= 0):
    print('\nBoth died.')
elif(red_energy <= 0):
    print('\nRed Warrior died.')
elif(blue_energy <= 0):
    print('\nBlue Warrior died.')
else:
    print('\nERROR')
# end if

# End Program
