# Michael Navarro - Program #7

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
def print_student_info():
    print('\nRequirement #1\n')
    print('This is Program 07 - Michael Navarro')

#--------------- Requirement #2 ------------------#
'''Print “This program provides practice working with lists, strings, tuples, and
dictionaries.”'''
def print_program_info():
    print('\nRequirement #2\n')
    print('This program provides practice working with lists, strings, tuples, and dictionaries.')

#--------------- Requirement #3 ------------------#
'''Create two tuples - one for two weeks named “Week One” and “Week Two” 
and one for three days of the week (Thursday, Friday, Saturday).'''
def define_weeks_days():
    print('\nRequirement #3\n')
    print('Tuples "weeks" and "days_of_week" assigned their values.')

    temp_weeks = 'Week One', 'Week Two'
    temp_days_of_week = 'Thursday', 'Friday', 'Saturday'

    return temp_weeks, temp_days_of_week

#--------------- Requirement #4 ------------------#
'''Use nested loops to Enter Sales Results (as shown in the output). 
Rep names must be entered with a space between names 
and the first letters of first and last names capitalized.'''
def get_sales_results(week_list, reps_list):
    print('\nRequirement #4\n')

    thursday_sales = []
    friday_sales = []
    saturday_sales = []

    print('########## Enter Sales Results ##########')
    for week in week_list:
        print(f'\n----- Entering boats sold for {week} -----')
        for rep in reps_list:
            thursday_sales.append(int(input(
                f'\nThursday boats sold by {rep}: ')))
            friday_sales.append(int(input(
                f'\nFriday boats sold by {rep}: ')))
            saturday_sales.append(int(input(
                f'\nSaturday boats sold by {rep}: ')))
        # end for
    #end for

    return thursday_sales, friday_sales, saturday_sales

#--------------- Requirement #5 ------------------#
'''Use nested loops to Print Sales Results (as shown in the output).'''
def print_sales_results(week_list, reps_list, thursday_sales, friday_sales, saturday_sales):
    print('\nRequirement #5\n')

    print('########## Print Sales Results ##########')
    index = 0
    for week in week_list:
        print(f'\n----- {week} Results -----')
        for rep in reps_list:
            print(f'\n{rep} sold {thursday_sales[index]} boats on Thursday.')
            print(f'\n{rep} sold {friday_sales[index]} boats on Friday.')
            print(f'\n{rep} sold {saturday_sales[index]} boats on Saturday.')
            index += 1
        # end for
    #end for

#--------------- Requirement #6 ------------------#
'''Populate a dictionary with dealer location keys and dealer URL values.'''
def create_dealer_dict(location_list):
    print('\nRequirement #6\n')

    temp_dealer_URLs = {}

    print('########## Enter Dealership URLs ##########')
    for location in location_list:
        current_URL = input(f'\nEnter the URL for {location}: ')
        temp_dealer_URLs[location] = current_URL

    return temp_dealer_URLs

#--------------- Requirement #7 ------------------#
'''Use existing sales rep names and URL information to construct and output email addresses as shown (convert to all lowercase and separated by _ ).'''
def print_URLs(dealer_dict, rep_list):
    print('\nRequirement #7\n')
    print('----- Contact sales reps at their email addresses: -----')
    index = 0
    for location in dealer_dict:
        current_rep = rep_list[index].split(' ')
        current_rep = '_'.join(current_rep).lower()
        print(f'\n{current_rep}@{dealer_dict[location]}')
        index += 1

#--------------- Requirement #8 ------------------#
def print_thoughts():
    print('\nRequirement #8\n')
    print('''This assignment was a fun little excercise in refactoring code and a nice way to introduce functions.
It allows one to see how concise previous code can get and begins to introduce OOP topics in a bite size way.
For example, we can begin to see abstraction at play.
For me the most difficult part was making sure I got all the variables needed in the correct place.
I did however run into, not exactly an issue, but an anomoly where I realized I don't use the variable days_of_week.
Seeing as that it is a requirement to have the variable, I have left it in.
I imagine it would've been used if the data for the variable wasn't required to be hard coded.''')

def main():
    print_student_info()                        # Req #1
    print_program_info()                        # Req #2
    weeks, days_of_week = define_weeks_days()   # Req #3
    
    # Req #4
    print('')                                   
    sales_reps = get_sales_reps()               
    print('')
    locations = get_locations()
    boats_sold_thursday, boats_sold_friday, boats_sold_saturday = get_sales_results(weeks, sales_reps)   
    # End Req #4

    # Req #5
    print_sales_results(weeks, sales_reps, boats_sold_thursday, boats_sold_friday, boats_sold_saturday)                         # End Req #5

    dealer_URLs = create_dealer_dict(locations) # Req #6
    print_URLs(dealer_URLs, sales_reps)         # Req #7
    print_thoughts()                            # Req #8

if __name__ == "__main__":
    main()
else:
    print('¯\_(ツ)_/¯')
    pass