# Michael Navarro - Program #14

#--------------- Libraries ------------------#
import options
import os

#--------------- Requirement #1 ------------------#
'''Output a header in the console: “This is Program14 - <yournamehere>”'''
print('\nRequirement #1\n')
print('This is Program14 - Michael Navarro')

#--------------- Program Info ------------------#
print('\nProgram Info\n')
print('This program lets a user batch rename file extensions, and organize a directory.')

sorting = True
root_path = os.getcwd()

while sorting == True:
    
    print("-" * 80)
    print(f'\nCurrent Root Path Is:\n{root_path}')
    
    main_option = options.get_main_option()

    if main_option == 'Q':
        sorting = False
    elif main_option == '1':
        options.rename_file_extensions()
    elif main_option == '2':
        options.org_by_extension(root_path)
    elif main_option == '3':
        options.org_by_filename(root_path)
    elif main_option == '4':
        options.delete_empty_directories(root_path)
    else:
        root_path = options.update_root()
    # End if

# End while

print('\nProgram Terminating.')

#--------------- Requirement #3 ------------------#
'''Print a statement explaining the grade you would award yourself for Program14 and why.'''
print('\nRequirement #3\n')
print('''To put it bluntly, I would award myself a low A at the least and here's why...
1. The size of the program is substantially bigger than what we have done thus far.
2. The complexity of the program is more complex than anything thus far.
3. Adhesion to DRY was maintained as much as possible.
4. It is not perfect, I know I missed some things.
5. I know the code can be refactored to be more efficient and adhere to the DRY standards better.
6. Overall the code has few bugs, perhaps the scale of it isn't as big as it should have been too,
    but it accomplishes what it sets out to do.''')

#--------------- Requirement #4 ------------------#
'''Print a statement explaining your experiences with Program14. 
Make this authentic (minimum of 2-3 sentences).'''
print('\nRequirement #4\n')
print('''I had lots of fun making this program. 
I chose this because it is a tool I have been wanting to make for myself.
What better program to make than to automate a boring procedure?
I did learn a couple of knew things along the way and revisited a lot of old things as well.
If anything I would incorporate more OOP standards and create a class to have the variables be consistent.
I believe their consistency may lead to more complex and streamlined operatins and increase the efficiency.''')