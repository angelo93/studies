# Michael Navarro - Program #4

#--------------- Variables ------------------#

# list of valid choices for input variables.
mem_lvls = ['composer', 'conductor', 'musician']
seat_prefs = ['orchestra', 'main', 'balcony']
meal_types = ['chicken', 'fish', 'vegan']
sentiment_lvls = ['1', '2', '3', '4', '5']

total_score = 0

#--------------- Helper Functions ------------------#

def validate_input(choice, options, sentimental = False):
    while choice not in options:
        if sentimental:
            print(f'\nAcceptal input is a number from 1-5.')
        else:
            print(f'\n1. {options[0].title()}    2. {options[1].title()}   3. {options[2].title()}')
        choice = input('Previous answer was not valid, please type in one of the answers above: ').lower()
    
    return choice

#--------------- Requirement 1 ------------------#
'''Output a header in the console: “This is Program04 - <yournamehere>”'''
print('Requirement #1\n')
print('This is Program 04 - Michael Navarro')

#--------------- Requirement 2 ------------------#
'''Print “This program provides concert seat assignments.”'''
print('\nRequirement #2\n')

print('This Program provides concert seat assignments.')

#--------------- Requirement 3 ------------------#
'''Ask the user their musical preference and take the following actions based on their potential input:
• Classical – proceed with the program (i.e. move to the next requirement)
• <anythingelse> – output a message that states “We do not recognize the <anythingelse> musical genre. Sorry.” Then end the program.'''
print('\nRequirement #3\n')

music_pref = input('Please enter the type of music you prefer to listen to: ').lower()

if music_pref != "classical":
    print(f'\nWe do not recognize the {music_pref} musical genre. Sorry.')
    exit()

#--------------- Requirement 4 ------------------#
'''Ask the user to enter the following data about themselves:
• First Name
• Last Name
• Membership Level          • Seat Preference             • Meal Type
    i. Composer                 i. Orchestra                i. Chicken
    ii. Conductor               ii. Main                    ii. Fish
    iii. Musician               iii. Balcony                iii. Vegan'''
print('\nRequirement #4\n')

first_name = input('Please enter your first name: ').lower().strip()
last_name = input('\nPlease enter your last name: ').lower().strip()

mem_lvl = input('''\n1. Composer    2. Conductor    3. Musician
Please select your membership level from the list above by typing it in (EX: "Composer"): ''').lower()
mem_lvl = validate_input(mem_lvl, mem_lvls)

seat_pref = input('''\n1. Orchestra    2. Main    3. Balcony
Please select your seat preference from the list above by typing it in (EX: "Orchestra"): ''').lower()
seat_pref = validate_input(seat_pref, seat_prefs)

meal_type = input('''\n1. Chicken    2. Fish    3. Vegan
Please select your meal type from the list above by typing it in (EX: "Chicken"): ''').lower()
meal_type = validate_input(meal_type, meal_types)

#--------------- Requirement 5 ------------------#
'''Message the following based on criteria (include First and Last Name in messages to user):
• if Composer and Orchestra:
    i. “You qualify for these are exceptional seats!”
• if Composer and Main:
    i. “The seats in the main section are good seats.”
• if Composer and Balcony:
    i. “Interesting, let us know if you want closer seats.”
• if Conductor and Orchestra:
    i. “Member level of Composer required if you want to sit in the orchestra section.”
• if Conductor and Main:
    i. “The seats in the main section are good seats.”
• if Conductor and Balcony:
    i. “Interesting, let us know if you want closer seats.”
• if Musician and Orchestra:
    i. “Member level of Composer required if you want to sit in the orchestra section.”
• if Musician and Main:
    i. “Member level of Composer or Conductor required if you want to sit in the main section.”
• if Musician and Balcony:
    i. “Your balcony seats are confirmed.”'''
print('\nRequirement #5\n')

full_name = first_name.title() + ' ' + last_name.title()

# Composer variations
if mem_lvl == 'composer' and seat_pref == 'orchestra':
    print(f'Congratulations {full_name}! You qualify for these exceptional seats!')
elif mem_lvl == 'composer' and seat_pref == 'main':
    print(f'Welcome {full_name}, The seats in the main section are good seats.')
elif mem_lvl == 'composer' and seat_pref == 'balcony':
    print(f'Interesting choice {full_name}, let us know if you want closer seats.')

# Conductor variations
elif mem_lvl == 'conductor' and seat_pref == 'orchestra':
    print(f"I'm sorry {full_name}, but a Member Level of Composer is required if you want to sit in the orchestra section.")
elif mem_lvl == 'conductor' and seat_pref == 'main':
    print(f'Welcome {full_name}, The seats in the main section are good seats.')
elif mem_lvl == 'conductor' and seat_pref == 'balcony':
    print(f'Interesting choice {full_name}, let us know if you want closer seats.')

# Musician variations
elif mem_lvl == 'musician' and seat_pref == 'orchestra':
    print(f"I'm sorry {full_name}, but a Member Level of Composer is required if you want to sit in the orchestra section.")
elif mem_lvl == 'musician' and seat_pref == 'main':
    print(f"I'm sorry {full_name}, but a Member Level of Composer or Conductor is required if you want to sit in the main section.")
else:
    print(f'Congratulations {full_name}! Your balcony seats are confirmed.')

#--------------- Requirement 6 ------------------#
'''After the concert, the user completes a survey. Ask the user to input a sentiment score
1 – 5 (1 = strongly disagree; 5 = strongly agree) in response to these three statements:
• The concert was wonderful.
• The food was fantastic.
• The seats were superb.'''
print('\nRequirement #6\n')

print('Welcome to the post concert survey! Please enter a score of 1-5 (1 = strongly disagree; 5 = strongly agree) for each statement.')

concert_score = input('\nThe concert was wonderful: ')
concert_score = validate_input(concert_score, sentiment_lvls, sentimental = True)
total_score += int(concert_score)

food_score = input('\nThe food was fantastic: ')
food_score = validate_input(food_score, sentiment_lvls, sentimental = True)
total_score += int(food_score)

seat_score = input('\nThe seats were superb: ')
seat_score = validate_input(food_score, sentiment_lvls, sentimental = True)
total_score += int(seat_score)

#--------------- Requirement 7 ------------------#
'''Message to the user based on the following:
• if Composer and (total score less than 12 or any score less than 4):
    i. “Dear Composer, Your survey score of <score> was lower than we would like. Please give us another opportunity soon.”
• Else // Composer
    i. “Thank you for being a Composer member and for having a good time!”
• if Conductor and (total score less than 11 or any score less than 3):
    i. “Dear Conductor, Your survey score of <score> was lower than we would like. The next time you attend we will be nicer.
• Else //Conductor
    i. “Thank you for being a Conductor member and for having a good time!”
• if Musician and (total score less than 10 or any score less than 2):
    i. “Dear Musician, Your survey score of <score> was lower than we would like. You will have more fun next time.”
• Else // Musician
    i. “Thank you for being a Musician member and for having a good time!”'''
print('\nRequirement #7\n')

if mem_lvl == "composer":
    if total_score < 12 or int(concert_score) < 4 or int(food_score) < 4 or int(seat_score) < 4:
        print(f'Dear Composer {full_name}, Your survey score of {total_score} was lower than we would like.\nPlease give us another opportunity soon.')
    else:
        print(f'Thank you {full_name} for being a Composer member and for having a good time!')

elif mem_lvl == 'conductor':
    if total_score < 11 or int(concert_score) < 3 or int(food_score) < 3 or int(seat_score) < 3:
        print(f'Dear Conductor {full_name}, Your survey score of {total_score} was lower than we would like.\nThe next time you attend we will be nicer.')
    else:
        print(f'Thank you {full_name} for being a Conductor member and for having a good time!')

else:
    if total_score < 10 or int(concert_score) < 2 or int(food_score) < 2 or int(seat_score) < 2:
        print(f'Dear Musician {full_name}, Your survey score of {total_score} was lower than we would like.\nYou will have more fun next time.')
    else:
        print(f'Thank you {full_name} for being a Musician member and for having a good time!')

#--------------- Requirement 8 ------------------#
'''Print a statement explaining your experiences with Program04. Make this authentic (minimum of 2-3 sentences).'''
print('\nRequirement #8\n')

print('''While I still had fun doing this assignment, of all the assignments thus far, I found it to be my least favorite.
I know practice makes perfect and this assignment's purpose is to practice if/else statements.
However, It was pretty much just translating very thorough pseudocode into python code.
Again, I still had fun, but I didn't feel a sense of accomplishment once I finished the assignment.''')