# Program combat
# Description: 
#   Creates game characters 
# Author: Michael Navarro 
# Date: 09 Sepetember 2020
# Revised: 

# list libraries used

# Declare and INITIALZE Variables (EVERY variable used)
#-------------------- Step 1 --------------------
'''Declare three variables for the strength, energy, and speed of two warriors.  
The names begin with red_ or blue_ for the two warriors, so they are red_strength, red_energy, and so forth.  
The two variables for the field are field_red and field_blue. 
Declare all eight variables by assigning them the value 0.  
Declare another variable, time, to be 0 also.'''

red_strength = 0
red_energy = 0
red_speed = 0

blue_strength = 0
blue_energy = 0
blue_speed = 0

field_red = 0
field_blue = 0

time = 0

#-------------------- Step 2 --------------------
'''Next, assign each variable it’s setup value.  
The red values are strength 45, energy 100, and speed 3.  
The blue values are 80, 150, and 5, respectively.  
The two location variables and time also start at 0.'''

red_strength = 45
red_energy = 100
red_speed = 3

blue_strength = 80
blue_energy = 150
blue_speed = 5

field_red = 0
field_blue = 0

time = 0

#-------------------- Step 3 --------------------
'''To play the game, do this seven times:
• print the time, then print all values for each warrior in this format:
Time is 0
Red strength is 45, energy is 100, speed is 3, location is 0.
Blue strength is 80, energy is 150, speed is 5, location is 0.

• add one to time
• add the speed of each warrior to its location
• subtract the square of each warrior’s speed from its energy
• subtract twice the warrior’s speed from its strength
'''

# Iteration 1
print(f'Time is {time}')
print(f'Red strength is {red_strength}, energy is {red_energy}, speed is {red_speed}, location is {field_red}.')
print(f'Blue strength is {blue_strength}, energy is {blue_energy}, speed is {blue_speed}, location is {field_blue}.')

# Add one to time
time += 1
# Add speed of each warrior to their location
field_red += red_speed  
field_blue += blue_speed
# Subtract the square of each warrior's speed from its energy
red_energy -= red_speed ** 2
blue_energy -= blue_speed ** 2
# Subtract twice the warrior's speed from its strength
red_strength -= red_speed * 2
blue_strength -= blue_speed * 2

# Iteration 2
print(f'\nTime is {time}')
print(f'Red strength is {red_strength}, energy is {red_energy}, speed is {red_speed}, location is {field_red}.')
print(f'Blue strength is {blue_strength}, energy is {blue_energy}, speed is {blue_speed}, location is {field_blue}.')

time += 1
field_red += red_speed
field_blue += blue_speed
red_energy -= red_speed ** 2
blue_energy -= blue_speed ** 2
red_strength -= red_speed * 2
blue_strength -= blue_speed * 2

# Iteration 3
print(f'\nTime is {time}')
print(f'Red strength is {red_strength}, energy is {red_energy}, speed is {red_speed}, location is {field_red}.')
print(f'Blue strength is {blue_strength}, energy is {blue_energy}, speed is {blue_speed}, location is {field_blue}.')

time += 1
field_red += red_speed
field_blue += blue_speed
red_energy -= red_speed ** 2
blue_energy -= blue_speed ** 2
red_strength -= red_speed * 2
blue_strength -= blue_speed * 2

# Iteration 4
print(f'\nTime is {time}')
print(f'Red strength is {red_strength}, energy is {red_energy}, speed is {red_speed}, location is {field_red}.')
print(f'Blue strength is {blue_strength}, energy is {blue_energy}, speed is {blue_speed}, location is {field_blue}.')

time += 1
field_red += red_speed
field_blue += blue_speed
red_energy -= red_speed ** 2
blue_energy -= blue_speed ** 2
red_strength -= red_speed * 2
blue_strength -= blue_speed * 2

# Iteration 5
print(f'\nTime is {time}')
print(f'Red strength is {red_strength}, energy is {red_energy}, speed is {red_speed}, location is {field_red}.')
print(f'Blue strength is {blue_strength}, energy is {blue_energy}, speed is {blue_speed}, location is {field_blue}.')

time += 1
field_red += red_speed
field_blue += blue_speed
red_energy -= red_speed ** 2
blue_energy -= blue_speed ** 2
red_strength -= red_speed * 2
blue_strength -= blue_speed * 2

# Iteration 6
print(f'\nTime is {time}')
print(f'Red strength is {red_strength}, energy is {red_energy}, speed is {red_speed}, location is {field_red}.')
print(f'Blue strength is {blue_strength}, energy is {blue_energy}, speed is {blue_speed}, location is {field_blue}.')

time += 1
field_red += red_speed
field_blue += blue_speed
red_energy -= red_speed ** 2
blue_energy -= blue_speed ** 2
red_strength -= red_speed * 2
blue_strength -= blue_speed * 2

# Iteration 7
print(f'\nTime is {time}')
print(f'Red strength is {red_strength}, energy is {red_energy}, speed is {red_speed}, location is {field_red}.')
print(f'Blue strength is {blue_strength}, energy is {blue_energy}, speed is {blue_speed}, location is {field_blue}.')

time += 1
field_red += red_speed
field_blue += blue_speed
red_energy -= red_speed ** 2
blue_energy -= blue_speed ** 2
red_strength -= red_speed * 2
blue_strength -= blue_speed * 2

#-------------------- Step 4 --------------------
'''Finally, print “Whew.”'''

print('\nWhew.')

# End Program
