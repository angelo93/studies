# Michael Navarro - Program #8

#--------------- Helper Functions ------------------#

def validate_ans(response):
    while response != 'y' and response != 'n':
        response = input('\nPlease enter (y)es or (n)o: ').lower()
    # end while

    return response

#--------------- Classes ------------------#

#--------------- Requirement #3 ------------------#
'''Most of the Pokémon class is provided. Complete the missing parts of the
Pokémon class. For instance, add lines 6, 7, and the definitions for the
get_name() and get_ability() methods.'''
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
    print('This is Program08 - Michael Navarro')

#--------------- Requirement #2 ------------------#
'''Print “This program keeps track of Pokémon characters.”'''
def print_program_info():
    print('\nRequirement #2\n')
    print('This program keeps track of Pokemon Characters.')

def add_pokemon():
    print('############### In add_pokemon() ###############')
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

#--------------- Requirement #4 ------------------#
'''Complete the ‘display_pokemon()’ function. My version required six lines
(including the ‘def’ line) but you can use more.'''
def display_pokemon(pokemon_list):
    pokemon_num = 1
    for pokemon in pokemon_list:
        print(f'\nName of Pokemon #{pokemon_num}: {pokemon.get_name().title()}')
        print(f'\nAbility of Pokemon #{pokemon_num}: {pokemon.get_ability().title()}')
        pokemon_num += 1

#--------------- Requirement #6 ------------------#
'''Print a statement explaining your experiences with Program08. Make this
authentic (minimum of 2-3 sentences).'''
def personal_thoughts():
    print('\nRequirement #6\n')
    print('''I love all things Pokemon, so I loved this assignment :)
In all seriousness this was a fun little assignment on classes and functions.
It's also a great introduction into OOP and shows what is possible with this programming paradigm.
I can't wait for the future assignments now that we are getting into the nitty gritty of things.''')

def main():
    print('\n############### In main() ###############')

    print_student_info()    # Req. 1
    print_program_info()    # Req. 2
    
    #--------------- Requirement #3 ------------------#
    print('\nRequirement #3\n')
    print('Pokemon class finalized.')
    
    #--------------- Requirement #4 ------------------#
    print('\nRequirement #4\n')
    print('Display Pokemon function finalized.')
    
    #--------------- Requirement #5 ------------------#
    '''Produce output like that shown below (your version must include
       Requirement statements):'''
    print('\nRequirement #5\n')

    pokemon_list = add_pokemon()
    display_pokemon(pokemon_list)

    personal_thoughts() # Req. 6

if __name__ == '__main__':
    main()
else:
    pass