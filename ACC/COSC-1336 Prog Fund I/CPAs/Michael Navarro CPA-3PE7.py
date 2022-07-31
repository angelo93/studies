# Declare variables
primary_color_one = str()
primary_color_two = str()
valid_colors = list()

# Setup
valid_colors = ['red', 'blue', 'yellow']

primary_color_one = input(
    'Please enter one of the three primary colors (Red, Blue, Yellow): ').lower().strip()
primary_color_two = input(
    'Please enter one of the three primary colors (Red, Blue, Yellow): ').lower().strip()

print('')

if (primary_color_one not in valid_colors or primary_color_two not in valid_colors):
    print('ERROR')
elif (primary_color_one == primary_color_two):
    print('No secondary color was created since you entered the same color twice.')
elif ((primary_color_one == 'red' and primary_color_two == 'blue') or (primary_color_two == 'red' and primary_color_one == 'blue')):
    print('When you mix red and blue, you get purple.')
elif ((primary_color_one == 'red' and primary_color_two == 'yellow') or (primary_color_two == 'red' and primary_color_one == 'yellow')):
    print('When you mix red and yellow, you get orange.')
elif ((primary_color_one == 'blue' and primary_color_two == 'yellow') or (primary_color_two == 'blue' and primary_color_one == 'yellow')):
    print('When you mix blue and yellow, you get green.')
else:
    print('Hmm, no secondary color found for that combo. Please try again.')
# end if
