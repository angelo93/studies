# Program 2

#--------------- Variables ------------------#
total_sales = 0
sales = []

#--------------- Helper Functions ------------------#
def sales_to_add():
    sales_to_enter = input('Do you have sales to enter? (y/n): ').lower()

    while sales_to_enter != 'y' and sales_to_enter != 'n':
        sales_to_enter = input('Please enter either (y)es or (n)o: ')

    return sales_to_enter

#--------------- Requirement 1 ------------------#
print('\nRequirement #1\n')
print('This is Program02 - Michael Navarro\n')

#--------------- Requirement 2 ------------------#
print('\nRequirement #2\n')
print('This program calculates strawberry sales for the month.\n')

#--------------- Requirement 3 ------------------#
print('\nRequirement #3\n')

adding = sales_to_add()

#--------------- Requirement 4 & 6------------------#
print('\nRequirement #4')
print('\nRequirement #6 fulfilled within while loop.\n')

while adding == 'y':
    temp_sales = input('Please enter amount: ')
    
    try:
        temp_sales = int(temp_sales)    # Convert input to int for arithmetic
        sales.append(temp_sales)
    except:
        print('Can only add numbers.')
    
    adding = sales_to_add() #Requirement #6

#--------------- Requirement 5 ------------------#
print('\nRequirement #5\n')

if sales:
    print('Adding entered sales for the month.')
    for sale in sales:
        print(f'Adding ${sale} to previous total of ${total_sales}.')
        total_sales += sale
else:
    print('No sales to add this month.')

#--------------- Requirement 7 ------------------#
print('\nRequirement #7\n')
print(f'Total Strawberry sales for the month are: ${total_sales}')

#--------------- Requirement 8 ------------------#
print('\nRequirement #8\n')
print('''At first glance this program seemed like it would be straight forward. 
However, as I progressed I began to see that there would need to be some additional logic implemented
to safeguard against possible errors. While I coded my solution to realize the given task, I know I didn't account for
all the errors that could occur. It also helped me remember a fundamental rule,
that functions in Python must be defined before use if not within a class object.''')
