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
if mem_lvl == 'composer':
    if seat_pref == 'orchestra':
        print(f'Congratulations {full_name}! You qualify for these exceptional seats!')
    elif mem_lvl == 'main':
        print(f'Welcome {full_name}, The seats in the main section are good seats.')
    else:
        print(f'Interesting choice {full_name}, let us know if you want closer seats.')

# Conductor variations
if mem_lvl == 'conductor':
    if seat_pref == 'orchestra':
        print(f"I'm sorry {full_name}, but a Member Level of Composer is required if you want to sit in the orchestra section.")
    elif seat_pref == 'main':
        print(f'Welcome {full_name}, The seats in the main section are good seats.')
    else:
        print(f'Interesting choice {full_name}, let us know if you want closer seats.')

# Musician variations
if mem_lvl == 'musician':
    if seat_pref == 'orchestra':
        print(f"I'm sorry {full_name}, but a Member Level of Composer is required if you want to sit in the orchestra section.")
    elif seat_pref == 'main':
        print(f"I'm sorry {full_name}, but a Member Level of Composer or Conductor is required if you want to sit in the main section.")
    else:
        print(f'Congratulations {full_name}! Your balcony seats are confirmed.')