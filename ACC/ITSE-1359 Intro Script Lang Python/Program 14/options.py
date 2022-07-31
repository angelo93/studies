#--------------- Libraries ------------------#
import modules
import menus

def get_main_option():
    menus.display_main_menu()
    msg = 'Please select an option or press "Q" to quit: '
    valid_choices = ['1', '2', '3', '4', '5', 'Q']

    main_option = modules.validate_choice(msg, valid_choices)
    
    return main_option
# End get_main_option()

def rename_file_extensions():
    # 1. Ask user to enter the directory in which the renaming process will take place.
    working_dir = input('\nPlease enter the complete path name of where the files are stored:\n')

    # 2. Create list of files
    file_list = modules.get_file_list(working_dir)

    # 3. Get old and new extensions
    old_ext = input('Please enter the file extension to be replaced (EX: rar): ')
    new_ext = input('Please enter the new file extension (EX: rar): ')

    # 4. Rename extensions
    modules.rename_extension(working_dir, file_list, old_ext, new_ext)
# End rename_file_extensions()

def org_by_extension(root_path):
    # 1. Create file dictionary
    file_dict = modules.create_file_dictionary(root_path, '1')

    # 2. Move files
    modules.move_files(root_path, file_dict)
# End org_by_extension()

def org_by_filename(root_path):
    # 1. Alphabatize, y/n?
    msg = '\nWould you like to alphabatize the directories after sorting the files? (Y/N): '
    valid_choices = ['Y', 'N']

    alphabatize = modules.validate_choice(msg, valid_choices)

    # 2. Create file dict
    if alphabatize == 'N':
        file_dict = modules.create_file_dictionary(root_path, '2')
    else:
        file_dict = modules.create_file_dictionary(root_path, '3')
    # End if

    # 3. Move files
    modules.move_files(root_path, file_dict)
# End org_by_filename()

def delete_empty_directories(root_path):
    # 1. Verify
    msg = '\nAre you sure you want to delete all empty directories? (Y/N): '
    valid_choices = ['Y', 'N']
    
    del_empty_dirs = modules.validate_choice(msg, valid_choices)

    # 2. Delete
    if del_empty_dirs == 'Y':
        modules.del_empty_dirs(root_path)
    else:
        print('Aborting... Empty directories will not be deleted.')
    # End if 
# End delete_empty_directories()

def update_root():
    root_path = input('\nPlease enter the complete path name for the new root directory:\n')

    new_root = modules.update_root_path(root_path)

    return new_root
# End update_root()