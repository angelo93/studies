# Michael Navarro - Program #10

#--------------- Libraries ------------------#
import pyperclip
import re
import pyinputplus
import random

#--------------- Helper Functions ------------------#

#--------------- Requirement #1 ------------------#
'''Output a header in the console: “This is Program10 - <yournamehere>”'''
print('\nRequirement #1\n')
print('This is Program10 - Michael Navarro')

#--------------- Requirement #2 ------------------#
'''Print “This program works with strings, uses regular expressions, 
and performs input validation tasks.”'''
print('\nRequirement #2\n')
print('This program works with strings, uses regular expressions, and performs input validation taks.')

#--------------- Requirement #3 ------------------#
'''Demonstrate the following:
• a string that includes the five Python escape characters
• a raw string that includes the five Python escape characters
• triple quotes using single and double quote examples.
• an example of multiline comments in your code.'''
print('\nRequirement #3\n')

print('I\'ve written this string using \"escape\" characters.\n\tEscape characters are created by utilizing the following format...\n\t\"\\\" +  \', \", t, n, or \\: \"\\t\".\n')
print(r'I\'m a raw string so I take everything \"literally\".\n\tSo it doesn\'t matter if you use escape characters such as \\.')
print('''
I'm a "multline triple quoted" string.
That means I take more than one line and that I'm surrounded by a set of "\'\'\'" characters.''')

'''I'm a multiline comment.
You can find other examples of me throughout this code.
I'm very helpful when used at the beginning of functions to offer a brief explanation of their functionality.'''

#--------------- Requirement #4 ------------------#
'''Assign a string to a list and print:
• a single indexed character
• the character 5 index places from the end
• the characters starting at 3 until the end
• the characters from the beginning up to but not including character 7'''
print('\nRequirement #4\n')

example_str = 'Woah! I\'m an example string.'
example_list = example_str[:]

print(example_list[4])
print(example_list[-5])
print(example_list[3:])
print(example_list[:7])

#--------------- Requirement #5 ------------------#
'''Demonstrate the in and not in operators.'''
print('\nRequirement #5\n')

print('achu "in" Pikachu:', 'achu' in 'Pikachu: ')
print('ice "not in" Noice!:', 'ice' not in 'Noice!')

#--------------- Requirement #6 ------------------#
'''Demonstrate including two strings inside another string using:
• the ‘+’ operator
• string interpolation
• f-strings'''
print('\nRequirement #6\n')

f_name = 'Michael'
l_name = 'Navarro'

print('My name is ' + f_name + ' ' + l_name + ' and I will catch \'em all!')
print('I said, My name is %s %s and I will catch \'em all!'%(f_name, l_name))
print(f'Ahem... I said, My name is {f_name.upper()} {l_name.upper()} and I will catch \'em all!')

#--------------- Requirement #7 ------------------#
'''Demonstrate: isalpha(), isalnum(), isdecimal(), isspace(), and istitle().'''
print('\nRequirement #7\n')

print('"Alpha.isalpha()": ', 'Alpha'.isalpha())
print('"Alpha1.isalpha()": ', 'Alpha1'.isalpha())

print('\n"Alpha.isalnum()": ', 'Alpha'.isalnum())
print('"Alpha1.isalnum()": ', 'Alpha1'.isalnum())

print('\n"123.isdecimal()": ', '123'.isdecimal())
print('"Alpha1.isdecimal()": ', 'Alpha1'.isdecimal())

print('\n"   .isspace()": ', '   '.isspace())
print('"Alpha1.isspace()": ', 'Alpha1'.isspace())

print('\n"This Is Title Case.istitle()": ', 'This Is Title Case'.istitle())
print('"This Is ALSO Title Case.istitle()": ', 'This Is NOT Title Case'.istitle())

#--------------- Requirement #8 ------------------#
'''Use two isX() methods in two loops (one per loop) for input validation.'''
print('\nRequirement #8\n')

valid = False
while valid == False:
    birth_year = input('Please enter the year you were born: ')
    if birth_year.isdecimal():
        print(f'So you were born in the year {birth_year}? Cool!\n')
        valid = True
    else:
        print('Uh, please follow the directions... >.>\n')

valid = False
while valid == False:
    print('Hi, I will create a password for you!')
    f_name = input('Please enter your first name: ')
    age = input('Please enter your age in numeric format: ')

    if f_name.isalpha() and age.isdecimal():
        print(f'\nThank you, your password is: {f_name.lower()}{age}, but don\'t tell anyone!')
        valid = True
    else:
        print('Uh, please follow the directions... >.>\n')

#--------------- Requirement #9 ------------------#
'''Convert a list of strings into one string.'''
print('\nRequirement #9\n')

list_o_strings = ['Pssst...', 'I have a theory about strings,', 'but I don\'t know what to call it...']
print(list_o_strings)
print(' '.join(list_o_strings))

#--------------- Requirement #10 ------------------#
'''Convert one string into a list of strings.'''
print('\nRequirement #10\n')

the_one_string = 'Oh boy, I sure hope nobody splits me up, I rather like being one long string!'
print(the_one_string)
print(the_one_string.split(','))

#--------------- Requirement #11 ------------------#
'''Demonstrate the following string methods:
• partition()
• center()
• strip()
• ord()
• chr()'''
print('\nRequirement #11\n')

print('"Mean Median Max".parition(\'Median\'):', 'Mean Median Max'.partition('Median'))
print('"I\'m the center of attention :)".center(50,\'-\'):', 'I\'m the center of attention :)'.center(50,'-'))
print('"               so many spaces!         ".strip():','               so many spaces!         '.strip())
print('"ord(\'A\') + ord(\'Z\')" =', ord('A') + ord('Z'))
print('chr(48) =', chr(48))

#--------------- Requirement #12 ------------------#
'''Demonstrate the following using pyperclip:
• copy() to the clipboard
• paste() from the clipboard'''
print('\nRequirement #12\n')

unique = 'Don\'t copy me please!'

pyperclip.copy(unique)
print(pyperclip.paste())

#--------------- Requirement #13 ------------------#
'''Ask the user to enter a user id in the following format:
• AAAA-####
• The first four characters must be a-z and/or A-Z. The next four are numbers.
• example: RWVT-7733'''
print('\nRequirement #13\n')

UID = input('Please enter a user id in the form of AAAA-####: ')

#--------------- Requirement #14 ------------------#
'''Use regular expressions to verify the user id supplied by the user meets format above. 
If not, inform the user and ask them to retry or exit.'''
print('\nRequirement #14\n')

ID_regex = re.compile(r'[a-zA-z]{4}-\d{4}')

valid_ID = False
while valid_ID == False:
    if UID.lower() == 'exit':
        valid_ID = True
    elif bool(ID_regex.match(UID)) == True:
        print('User ID entered is in accordance to the specified format.')
        valid_ID = True
    else:
        UID = input('Please enter a valid user id or type "exit" to quit: ')
    
#--------------- Requirement #15-17 ------------------#
'''After verifying the user id meets the format, 
verify that one of the following user ids has been entered.'''

'''Only accept the following user ids:
• gdrt-8493, DBTF-6253, UyHt-8326, YYrv-5329, qzrb-8264'''

'''After successful entry, display a message stating, 
“Thank you for entering your user id.”'''
print('\nRequirement #15-17\n')

acceptable_IDs = ['gdrt-8493', 'DBTF-6253', 'UyHt-8326', 'YYrv-5329', 'qzrb-8264']

while UID not in acceptable_IDs:
    UID = input('That is not an acceptable ID, please try again: ')
        
    while bool(ID_regex.match(UID)) == False:
        UID = input('Please provide an acceptable ID in the format of AAAA-####: ')
 
print('\nThank you for entering your user id.')
    
#--------------- Requirement #18 ------------------#
'''Ask the user to enter a phone number in the following format:
• ###-###-###-####
• The first three numbers are the international calling code, 
    followed by the area code, the exchange, and the number. 
    Three dashes separate the values.
• example: 506-745-223-4433 (using country code for Costa Rica)'''
print('\nRequirement #18\n')

phone_number = input('Please enter a phone number in the format of ###-###-###-####: ')

#--------------- Requirement #19 ------------------#
'''Use regular expressions to verify the phone number 
supplied by the user meets format above. 
If not, inform the user and ask them to retry or exit.'''
print('\nRequirement #19\n')

phone_regex = re.compile(r'\d{3}-\d{3}-\d{3}-\d{4}')

while bool(phone_regex.match(phone_number)) == False:
    if phone_number.lower() == "exit":
        break

    phone_number = input('Please provide a phone number with the aforementioned format or enter "exit" to quit: ')

print('Thank you for entering your number!')

#--------------- Requirement #20-22 ------------------#
'''After verifying the phone number meets the format, 
verify the call is being placed to one of the countries below.'''

'''Only accept calls to the following countries:
• Andorra – 376
• Bolivia – 591
• Djibouti – 253
• Georgia – 995
• Lithuania – 370'''

'''After successful entry, display a message stating, 
“Your call has been placed. Thank you for calling <country name>.”'''
print('\nRequirement #20-22\n')

acceptable_codes = {
    '376': 'Andorra', 
    '591': 'Bolivia', 
    '253': 'Djibuti', 
    '995': 'Georgia', 
    '370': 'Lithuania'
}

while phone_number[0:3] not in acceptable_codes:
    phone_number = input('Please enter a phone number with an acceptable country extension: ')

    while bool(phone_regex.match(phone_number)) == False:
        phone_number = input('You must adhere to the format of ###-###-###-####: ')

print(f'\nYour call has been placed. Thank you for calling {acceptable_codes[phone_number[0:3]]}')

#--------------- Requirement #23 ------------------#
'''Demonstrate five PyInputPlus functions to validate input.'''
print('\nRequirement #23\n')

choices = ['yeah no yeah', 'no yeah no']

choice = pyinputplus.inputChoice(choices)
print()
choice = pyinputplus.inputMenu(choices)
print()
my_nbr = pyinputplus.inputNum(prompt='Please enter a number: ')
print(f'What a coincidence! My lucky number is {my_nbr}!')
print()
my_email = pyinputplus.inputEmail(prompt='Please enter your email: ')
my_pwd = pyinputplus.inputPassword(prompt='Please enter your password: ')
print(f'Thank you for telling me that your email is {my_email} and your password is {my_pwd}!\nExcuse me while I go do some totally not illegal things now...')

#--------------- Requirement #24 ------------------#
'''Demonstrate the following PyInputPlus keyword arguments:
• min, max, greaterThan, and lessThan
• limit, timeout, and default
• allowRegexes and blockRegexes'''
print('\nRequirement #24\n')

my_min = pyinputplus.inputInt(prompt = 'Please enter the minimum possible number to guess less than 100: ', min = 0, lessThan = 100)
my_max = pyinputplus.inputInt(prompt = 'Please enter the maximum possible number to guess at max 100: ', greaterThan = my_min, max = 100)

answer = random.randint(my_min, my_max)
guess = -1

while guess != answer:
    guess = pyinputplus.inputInt(prompt = 'Please enter your guess: ', greaterThan = my_min, lessThan = my_max + 1)

    if guess > answer:
        print('Too high!')
    elif guess < answer: 
        print('Too low!')
    else:
        print(f'Congrats!! You finally guessed that {answer} was the answer!')
user_bool = pyinputplus.inputBool(prompt = 'Please enter true/1 or false/0: ', allowRegexes = [r'[10]'])
print(user_bool + '\n')

options = ['apples', 'oranges', 'banana']

print(options)
blocked = pyinputplus.inputChoice(prompt = 'Choose the option that is NOT plural: ', choices = options, blockRegexes = [r'[s]$']).lower()

#--------------- Requirement #25 ------------------#
'''Print a statement explaining your experiences with Program10. Make this authentic'''
print('\nRequirement #25\n')
print('''While I did enjoy learning a few new things through this assignment I found myself bored through most of it.
It was a bit tedious and repetitive resulting in me kind of tuning out on the keyboard and just wanting to get through this.
I tried having fun with some of the implementations, but found it taking too much time.
Not to sound rude or anything, but this was definitely my least like assignment thus far and definitely not my cup of tea.''')
