# Michael Navarro - Program #5

#--------------- Variables ------------------#
num_authors = 0
iteration = 0
num_books = 0
count = 0 

author_name = ''
author_url = ''
adding = ''

book_name_list = []
book_isbn_list = []
book_order_quantity_list = []

#--------------- Helper Functions ------------------#

def is_num(num):
    '''Check if input is a numerical character, 
    if it is convert to int and return the value.
    else, keep asking for a numerical character.'''

    not_int = True

    while not_int:
        try:
            int(num)
            not_int = False
        except:
            num = input('Please provide a number: ')
    
    return int(num)

#--------------- Requirement #1 ------------------#
'''Output a header in the console: “This is Program05 - <yournamehere>”'''
print('\nRequirement #1\n')

print('This is Program 05 - Michael Navarro')

#--------------- Requirement #2 ------------------#
'''Print “This program records Book People product data.”'''
print('\nRequirement #2\n')

print('This program records Book People product data.')

#--------------- Requirement #3 ------------------#
'''Ask user to enter the number of authors to process. Store the number in a variable.'''
print('\nRequirement #3\n')

num_authors = input('Please enter the number of authors you wish to process: ')
num_authors = is_num(num_authors)

#--------------- Requirement #4 ------------------#
'''Use the number the user entered to process the number of authors in an outer loop. Use the outer loop to ask the user to enter the following data :
• Author Name
• Author Website URL'''
print('\nRequirement #4, #5, #6, #7')

while iteration < num_authors:
    author_name = input('\nPlease provide the name of the author: ').lower().strip()
    author_url = input('Please provide the URL of the author\'s website: ').lower().strip()

    #--------------- Requirement #5 ------------------#
    '''Use an inner loop to process the books.
    Store each of the three items below in appropriate lists named: book_name_list, book_isbn_list, book_order_quantity_list. Ask the user to enter a ‘-1’ to end. Ask the user to enter the following data:
    • Book Title
    • Book ISBN
    • Amount to Order – this just needs to be a number (e.g. 3, 41, 17)'''

    while adding != '-1':
        book_title = input('\nPlease enter the title of the book: ').strip()
        book_name_list.append(book_title)

        book_isbn = input('\nPlease provide the book\'s ISBN number: ').strip()
        book_isbn_list.append(book_isbn)

        num_to_order = input('\nPlease provide the number of copies to order: ').strip()
        num_to_order = is_num(num_to_order)
        book_order_quantity_list.append(num_to_order)

        num_books += 1

        adding = input('\nPress enter to continue adding books. If you are finished enter "-1": ').strip()

    #--------------- Requirement #6 ------------------#
    ''' After the first inner loop, output the following that was entered by the user in requirement #4:
    • Author Name
    • Author Website URL'''

    author_name = author_name.split(' ')
    author_name = ' '.join(author_name).title()

    print("\n" + author_name.title())
    print(author_url)

    #--------------- Requirement #7 ------------------#
    '''Then, still after the first inner loop, use a second inner loop to output the following from the list data that was entered above:
    • Book Title i - _____
    • Book ISBN i - ______
    • Amount to Order i - ______'''

    while count < num_books:
        print(f'\nBook Title {count + 1} - {book_name_list[count]}')
        print(f'Book ISBN {count + 1} - {book_isbn_list[count]}')
        print(f'Amount to Order {count + 1} - {book_order_quantity_list[count]}')

        count += 1

    # Reset all variables for next iteration use.
    num_books = 0
    count = 0

    author_name = ''
    author_url = ''
    adding = ''

    book_name_list = []
    book_isbn_list = []
    book_order_quantity_list = []

    # Increments iteration count for main while loop use
    iteration += 1

#--------------- Requirement #8 ------------------#
print('\nRequirement #8')
print('''This was a pretty fun program for me for a couple of different reasons.
The first is that I was allowed to be a bit creative in my implementation of the requested features.
The second is a bit more abstract and subjective of a reason, but I like how the code looks and turned out.
The code itself is very simplistic in nature, but it's the simplicity of it that lets it flow smoothly when reading it.
I think the hardest thing about the program was deciding between the tradeoff of being strict are not so strict with the user input.
Ultimately I decided to make numerical values be strict and allowed the user the freedom to input whatever input they wanted for the rest.
My reasoning behind this was that some authors can have peculiar names as well as the title of their works.''')
