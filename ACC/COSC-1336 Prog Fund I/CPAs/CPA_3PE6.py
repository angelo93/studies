# Initiate variables
month = int()
day = int()
year = int()

# Provide some user guidelines
print('This program requires that the input provided follows the structure of: "1/23/48" without the slashes.')
print('Please be sure to only enter numeric values as anything else will not work.\n')

# Get user input and conver to integers
month = int(input('Please enter a month in its numeric form. EX: January = 1: '))
day = int(input('Please enter a day of the chosen month: '))
year = int(input('Please enter the last two digits of a year: '))

if((month * day) == year):
    print('\nYou have entered a magical date!')
else:
    print('\nIt seems there is nothing magical about the entered date :(')
# end if