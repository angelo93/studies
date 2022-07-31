adding = str()
num1 = float()
num2 = float()
sum_nums = float()

while ( adding != '-1' ):

    num1 = input('Please enter your first number to add: ')
    num2 = input('Please enter your second number to add: ')

    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print('ERROR, INVALID INPUT')
        break
    # end try/except

    sum_nums = num1 + num2

    print(f'\nThe sum of {num1} and {num2} is... {sum_nums}')

    adding = input('\nPress any key to continue adding or "-1" to exit: ')
# end while