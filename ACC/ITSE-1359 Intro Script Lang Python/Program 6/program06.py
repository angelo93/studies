# Michael Navarro - Program #6

#--------------- Variables ------------------#
weeks = ()
days_of_week = ()

sales_reps = []
locations = []

boats_sold_thursday = []
boats_sold_friday = []
boats_sold_saturday = []

dealer_URLs = {}

#--------------- Helper Functions ------------------#

def forge_full_name(name):
    temp_name = name.split(' ')
    # Filter out the empty spaces
    temp_name = [item for item in temp_name if item != '']
    # Create fullname with required formatting
    full_name = ' '.join(temp_name).title()

    return full_name
# end function

def get_sales_reps():
    count = 0
    temp_sales_reps = []

    while count < 3:
        current_rep = input(
            'Please enter the sales rep\'s name: ').lower().strip()
        current_rep = forge_full_name(current_rep)
        temp_sales_reps.append(current_rep)

        count += 1
    # end while

    return temp_sales_reps
# end function

def get_locations():
    count = 0
    temp_locations = []

    while count < 3:
        current_location = input(
            'Please enter the location\'s name: ').lower().strip()
        current_location = forge_full_name(current_location)
        temp_locations.append(current_location)

        count += 1
    # end while

    return temp_locations
# end function

#--------------- Requirement #1 ------------------#
'''Output a header in the console: “This is Program06 - <yournamehere>”'''
print('\nRequirement #1\n')
print('This is Program 05 - Michael Navarro')

#--------------- Requirement #2 ------------------#
'''Print “This program uses lists, strings, tuples, and dictionaries.”'''
print('\nRequirement #2\n')
print('This program uses lists, strings, tuples, and dictionaries.')

#--------------- Requirement #3 ------------------#
'''Create two tuples - one for two weeks named “Week One” and “Week Two” 
and one for three days of the week (Thursday, Friday, Saturday).'''
print('\nRequirement #3\n')
print('Tuples "weeks" and "days_of_week" assigned their values.')

weeks = 'Week One', 'Week Two'
days_of_week = 'Thursday', 'Friday', 'Saturday'

#--------------- Requirement #4 ------------------#
'''Use nested loops to Enter Sales Results (as shown in the output). 
Rep names must be entered with a space between names 
and the first letters of first and last names capitalized.'''
print('\nRequirement #4\n')

sales_reps = get_sales_reps()
print('')
locations = get_locations()

print('\n########## Enter Sales Results ##########')
for week in weeks:
    print(f'\n----- Entering boats sold for {week} -----')
    for rep in sales_reps:
        boats_sold_thursday.append(int(input(
            f'\nThursday boats sold by {rep}: ')))
        boats_sold_friday.append(int(input(
            f'\nFriday boats sold by {rep}: ')))
        boats_sold_saturday.append(int(input(
            f'\nSaturday boats sold by {rep}: ')))
    # end for
#end for

#--------------- Requirement #5 ------------------#
'''Use nested loops to Print Sales Results (as shown in the output).'''
print('\nRequirement #5\n')

print('########## Print Sales Results ##########')
index = 0
for week in weeks:
    print(f'\n----- {week} Results -----')
    for rep in sales_reps:
        print(f'\n{rep} sold {boats_sold_thursday[index]} on Thursday.')
        print(f'\n{rep} sold {boats_sold_friday[index]} on Friday.')
        print(f'\n{rep} sold {boats_sold_saturday[index]} on Saturday.')
        index += 1
    # end for
#end for

#--------------- Requirement #6 ------------------#
'''Populate a dictionary with dealer location keys and dealer URL values.'''
print('\nRequirement #6\n')

print('########## Enter Dealership URLs ##########')
for location in locations:
    current_URL = input(f'\nEnter the URL for {location}: ')
    dealer_URLs[location] = current_URL

#--------------- Requirement #7 ------------------#
'''Use existing sales rep names and URL information to construct and output email addresses as shown (convert to all lowercase and separated by _ ).'''
print('\nRequirement #7\n')
print('----- Contact sales reps at their email addresses: -----')
index = 0
for location in dealer_URLs:
    current_rep = sales_reps[index].split(' ')
    current_rep = '_'.join(current_rep).lower()
    print(f'\n{current_rep}@{dealer_URLs[location]}')
    index += 1

#--------------- Requirement #8 ------------------#
print('\nRequirement #8\n')
print('''This was an interesting assignment to say the least.
As I began to write my own code I arrived to the conclusion that the operability of this program as laid out by the instructions, 
is contigent on the order of the items in a given list. Because of this,
I quickly realized my implementation would not suffice as I was going a completely different way.
Instead of reinventing the wheel, I conceded to using the supplied code and reverse engineering it.
I implemented the missing parts and created a couple of helper functions to help in getting the required use inputs.
In the end, this assignment helped to serve as a code reading/understanding excercise which will come in handy in the field.''')