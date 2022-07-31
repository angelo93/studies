# Program Program independence
# Description:
#   starts a revolution
# Author: Michael Navarro
# Date: 4 July 1776
# Revised:
#
# list libraries used

# Declare constants (name in ALL_CAPS)
F_TO_C = 5 / 9
C_TO_F = 9 / 5

# Declare Variable types (EVERY variable used)
not_float = bool()
degree_num = str()
degree_in_F = float()
degree_in_C = float()

not_float = True

degree_num = input('Please enter a decimal number: ').strip()

while (not_float == True):
    # Convert input to float for later arithmetic use and end loop
    try:
        degree_num = float(degree_num)
        not_float = False
    # Keep asking for input util a numerical value is entered
    except:
        degree_num = input('Please enter a decimal number: ').strip()
# End while

# Convert input to celsius and fahrenheit
degree_in_F = (degree_num * C_TO_F) + 32
degree_in_C = (degree_num - 32) * F_TO_C

print(f'If {degree_num} is Fahrenheit, it is ' +
      str(format(degree_in_C, '.1f')) + ' degrees Celsius.')
print(f'If {degree_num} is Celsius, it is ' +
      str(format(degree_in_F, '.1f')) + ' degrees Fahrenheit.')
# End Program
