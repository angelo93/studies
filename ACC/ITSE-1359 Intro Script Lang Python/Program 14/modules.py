#--------------- Libraries ------------------#
import os
import string
import shutil

def validate_choice(msg, valid_choices):
    choice = input(msg).upper()

    while choice not in valid_choices:
        choice = input(msg).upper()
    # End while

    return choice
# End validate_choice()

def del_empty_dirs(root_path):
    '''Delete all empty directories and subdirectories
        root_path = path of root folder passed in from menu instance.'''
    num_deleted_dirs = 0

    for dirpath, dirnames, _ in os.walk(root_path, topdown=False):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        try:
            os.rmdir(dirpath)
            num_deleted_dirs += 1
        except:
            print(f'Dir Not Empty: {dirpath}')
        # End try/except
    # End for

    if num_deleted_dirs > 0:
        print(f'\nEmpty directories deleted: {num_deleted_dirs}')
    else:
        print('\nThere were no empty directories to delete')
    # End if
# End del_empty_dirs()

def move_files(root_path, file_dictionary):
    '''Move files from one directory to another using a given dictionary of files.'''

    for _, file_info in file_dictionary.items():
        # Check to see if the file needs to be moved, if not continue to next file.
        if file_info['source'] == file_info['destination']:
            continue
        # End if

        try:
            # Create the parent dir
            os.makedirs(os.path.join(
                root_path, file_info['parent_dir']), exist_ok=True)
            
            shutil.move(file_info['source'], file_info['destination'])
        except FileExistsError:
            print(f'File Exists: "{file_info["destination"]}"')
        except FileNotFoundError:
            print(f'File Not Found: "{file_info["source"]}"')
        # End try/except
# End move_files()

def get_alpha_dir(filename):
    '''Determine the alphabetical folder for a file.'''
    alpha_dir = ''

    # Check to see if file name starts with a number.
    if filename[0].isdigit():
        alpha_dir = '#'
    # Check to see if file name starts with a letter.
    elif filename[0].isalpha():
        alpha_dir = filename[0].upper()
    # If file name doesn't start with a number or a letter.
    else:  
        alpha_dir = 'Other'
    # End if

    return alpha_dir
# End get_alpha_dir()

def create_file_dictionary(root_path, option):
    '''Create a file dictionary of files in a directory tree with a structure of...
        file_dictionary[filename] = {
            'parent_dir': parent_dir,
            'source': source,
            'destination': destination,
        }
        parent_dir will serve as the new direct parent directory of the file.
        source is the full pathname of the file.
        destination is the full pathname of the new location for the file.'''

    file_dictionary = {}

    # Construct dictionary entry
    for dirpath, _, filenames in os.walk(root_path):
        # Skip hidden directories
        if dirpath.split('\\')[-1].startswith('.'):
            continue
        # End if

        for filename in filenames:
            # Skip hidden files.
            if filename.startswith('.'):
                continue
            # End if

            # Organize by file extension
            if option == '1':
                # Parent dir is the extension
                parent_dir = filename.split('.')[-1].upper()
                destination = os.path.join(root_path, parent_dir, filename)
            # Organize by filename
            elif option == '2':
                # Parent dir is the first part of the filename.
                # If filename contains multiple '.' then parent dir is up to the first '.'.
                parent_dir = filename.split('.')[0].title()
                destination = os.path.join(root_path, parent_dir, filename)
            # Organize by filename and alphabatize
            else:
                alpha_dir = get_alpha_dir(filename)
                parent_dir = alpha_dir + '/' + filename.split('.')[0].title()
                destination = os.path.join(root_path, parent_dir, filename)
            # End if

            source = os.path.join(dirpath, filename)
            
            file_dictionary[filename] = {
                'parent_dir': parent_dir,
                'source': source,
                'destination': destination,
            }
        # End for
    # End for

    return file_dictionary
# End create_file_dictionary()

def update_root_path(root_path):    
    # Check to see if directory exists
    if os.path.isdir(root_path) == False:
        print(f'Unable To Find:\n{root_path}')
        root_path = os.getcwd()
        print(f'Working directory set to current location.\n{root_path}')
    # End if

    return root_path
# End get_root_path()

def rename_extension(root_path, file_list, old_ext, new_ext):
    '''Batch rename one file extension at a time in a given directory'''
    if os.path.isdir(root_path) == False:
        print(f"Unable To Find:\n{root_path}")
    else:
        for filename in file_list:
            if filename.split(".")[-1] == old_ext:
                # Replace old extension with new extension
                new_filename = filename
                temp_filename = new_filename.split(".")
                temp_filename[-1] = new_ext
                new_filename = ".".join(temp_filename)

                try:
                    os.rename(os.path.join(root_path, filename),
                            os.path.join(root_path, new_filename))
                except:
                    print(f"Unable To Rename: {filename}.")
            # End if
        # End for
    # End if
# End rename_extension()

def get_file_list(root_path):
    '''Create a list of files in a given directory'''
    file_list = []

    for filename in os.listdir(root_path):
        if os.path.isfile(os.path.join(root_path, filename)):
            file_list.append(filename)
        # End if
    # End for

    return file_list
# End get_file_list()