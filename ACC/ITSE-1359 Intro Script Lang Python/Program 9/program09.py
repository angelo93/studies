# Michael Navarro - Program #9

#--------------- Libraries ------------------#
import os

#--------------- Helper Functions ------------------#

def validate_ans(response):
    while response != 'y' and response != 'n':
        response = input('\nPlease enter (y)es or (n)o: ').lower()
    # end while

    return response

#--------------- Classes ------------------#

class Pokemon:
    def __init__(self, name, ability):
        self.__name = name
        self.__ability = ability
    
    def get_name(self):
        return self.__name

    def get_ability(self):
        return self.__ability

#--------------- Core Functions ------------------#

#--------------- Requirement #1 ------------------#
'''Output a header in the console: “This is Program08 - <yournamehere>”'''
def print_student_info():
    print('\nRequirement #1\n')
    print('This is Program09 - Michael Navarro')

#--------------- Requirement #2 ------------------#
'''Print “This program keeps track of Pokémon characters.”'''
def print_program_info():
    print('\nRequirement #2\n')
    print('This program keeps track of Pokemon Characters, saves the data to a file, and displays the data from a file.')

def add_pokemon():
    print('\n############### In add_pokemon() ###############')
    pokemon_list = []
    pokemon_num = 1

    more_pokemon = input('\nDo you have a Pokemon to add? (y/n): ').lower()
    more_pokemon = validate_ans(more_pokemon)

    while more_pokemon == 'y':
        # Get name and ability of Pokemon from user
        pokemon_name = input(f'\nEnter name for Pokemon #{pokemon_num}: ').lower()
        pokemon_ability = input(f'\nEnter ability for Pokemon #{pokemon_num}: ').lower()
        # Create new instance of Pokemon
        new_pokemon = Pokemon(pokemon_name, pokemon_ability)
        # Add new instance to list
        pokemon_list.append(new_pokemon)

        pokemon_num += 1

        # Ask user for more Pokemon
        more_pokemon = input('\nDo you have another Pokemon to add? (y/n): ').lower()
        more_pokemon = validate_ans(more_pokemon)
    # end while

    return pokemon_list

#--------------- Requirement #3 ------------------#
'''Write and call the function ‘save_data()’ that saves Pokémon data to a file.'''

def save_data(pokemon_record, filename):
    pokemon_num = 1
    with open(filename, "w", encoding='utf-8') as save_file:
        for pokemon in pokemon_record:
            save_file.write(f'Name of Pokemon #{pokemon_num}: {pokemon.get_name().title()}')
            save_file.write(f'\nAbility of Pokemon #{pokemon_num}: {pokemon.get_ability().title()}\n')
            pokemon_num += 1

#--------------- Requirement #4 ------------------#
'''Call the function ‘display_data()’ that reads the data from a file 
and displays the output just like requirement #5 in Program08.'''
def display_data(filename):
    with open(filename) as saved_data:
        for entry in saved_data:
            print(entry)
    

#--------------- Requirement #5 ------------------#
'''Print a statement explaining your experiences with Program08. Make this
authentic (minimum of 2-3 sentences).'''
def personal_thoughts():
    print('Requirement #5\n')
    print('''It was fun refactoring the program to utilize the writing to a file functionality of Python.
Again, being something related to Pokemon I enjoyed working on this program.
I also realized that while I have experience writing to files using Python,
it is a good idea to practice old skills to stay up to par, per say.''')


#--------------- Main ------------------#
def main():
    filename = 'pokemon_bank.txt'

    print('\n############### In main() ###############')

    print_student_info()    # Req. 1
    print_program_info()    # Req. 2
    
    pokemon_list = add_pokemon()
    
    #--------------- Requirement #3 ------------------#
    print('\nRequirement #3\n')
    print('Pokemon succesfully saved to Bank.')
    save_data(pokemon_list, filename)
    
    #--------------- Requirement #4 ------------------#
    print('\nRequirement #4\n')
    display_data(filename)

    personal_thoughts() # Req. 5

if __name__ == '__main__':
    main()
else:
    pass