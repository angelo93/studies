# Library tk_modules
# Functions Included in Library: 
#   del_empty_dirs()
#   move_files()
#   get_alpha_dir()
#   create_file_dictionary()
#   rename_extension()
#   get_file_list()
# Author: Michael Navarro
# Date: 12/08/2020
# Revised: 
#   Date: 12/09/2020

# list libraries used
import os
import string
import shutil

# Function del_empty_dirs()
# Description:
#   Deletes empty directories in the directory tree.
# Calls:
#   tk_modules.get_file_list()
#   tk_modules.rename_extension()
#   os.walk()
#   os.rmdir()
#   error_logs.append()
# Parameters:
#   root_path        str
# Returns:
#   [num_deleted_dirs, error_logs]
def del_empty_dirs(root_path):
    '''Delete all empty directories and subdirectories
        root_path = path of root folder passed in from menu instance.'''

    # Declare Local Variable types (NOT parameters)
    num_deleted_dirs = int()
    error_logs = list()

    num_deleted_dirs = 0
    error_logs = []

    for dirpath, dirnames, _ in os.walk(root_path, topdown=False):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        try:
            os.rmdir(dirpath)
            num_deleted_dirs += 1
        except:
            error_logs.append(f'Dir Not Empty:\n{dirpath}')
        # End try/except
    # End for

    return [num_deleted_dirs, error_logs]
# End del_empty_dirs()

# Function move_files()
# Description:
#   Move files in a supplied dictionary.
# Calls:
#   exist_errors.append()
#   not_found_errors.append()
#   os.makedirs()
#   shutil.move()
# Parameters:
#   root_path              str
#   file_dictionary        dict
# Returns:
#   [exist_errors, not_found_errors]
def move_files(root_path, file_dictionary):
    '''Move files from one directory to another using a given dictionary of files.'''

    # Declare Local Variable types (NOT parameters)
    exist_errors = list()
    not_found_errors = list()

    exist_errors = []
    not_found_errors = []

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
            exist_errors.append(f'File Exists: "{file_info["destination"]}"')
        except FileNotFoundError:
            not_found_errors.append(f'File Not Found: "{file_info["source"]}"')
        # End try/except

    return [exist_errors, not_found_errors]
# End move_files()

# Function get_alpha_dir()
# Description:
#   Get the first character of a filename
# Calls:
#   isdigit()
#   isalpha()
#   upper()
# Parameters:
#   filename              str
# Returns:
#   alpha_dir
def get_alpha_dir(filename):
    '''Determine the alphabetical folder for a file.'''
    # Declare Local Variable types (NOT parameters)
    alpha_dir = str()

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

# Function create_file_dictionary()
# Description:
#   Creates a dictionary of all files and their source and destination paths.
# Calls:
#   os.walk()
#   os.path.join()
#   split()
#   startswith()
# Parameters:
#   option              str
#   root_path           str
# Returns:
#   file_dictionary
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
    # Declare Local Variable types (NOT parameters)
    file_dictionary = dict()
    parent_dir = str()
    destination =str()
    source = str()

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

# Function rename_extension()
# Description:
#   Renames a supplied extension with another extension also supplied.
# Calls:
#   startswith()
#   split()
#   join()
#   append()
#   os.path.join()
# Parameters:
#   root_path            str
#   file_list            str
#   old_ext              str
#   new_ext              str
# Returns:
#   error_logs
def rename_extension(root_path, file_list, old_ext, new_ext):
    '''Batch rename one file extension at a time in a given directory'''

    # Declare Local Variable types (NOT parameters)
    error_logs = list()
    new_filename = str()
    temp_filename = str()

    error_logs = []

    for filename in file_list:
        #Skip hidden files.
        if filename.startswith('.'):
            continue
        # End if

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
                error_logs.append(f"Unable To Rename: {filename}.")
        # End if
    # End for
    
    return error_logs
# End rename_extension()

# Function get_file_list()
# Description:
#   Creates a list of files in a given directory
# Calls:
#   os.listdir()
#   os.path.isfile()
#   append()
# Parameters:
#   root_path            str
# Returns:
#   file_list
def get_file_list(root_path):
    '''Create a list of files in a given directory'''

    # Declare Local Variable types (NOT parameters)
    file_list = list()

    file_list = []

    for filename in os.listdir(root_path):
        if os.path.isfile(os.path.join(root_path, filename)):
            file_list.append(filename)
        # End if
    # End for

    return file_list
# End get_file_list()

# End Module tk_modules