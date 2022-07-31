import options
import os

sorting = True
root_path = os.getcwd()

while sorting == True:

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