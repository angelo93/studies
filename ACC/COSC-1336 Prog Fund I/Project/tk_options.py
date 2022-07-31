# Library tk_options 
# Functions Included in Library: 
#   rename_file_extensions()
#   organize_files()
#   delete_empty_directories()
# Author: Michael Navarro
# Date: 12/08/2020
# Revised: 
#   Date: 12/09/2020

# list libraries used
import tk_modules

# Function rename_file_extensions()
# Description:
#   Takes in necessary parameters and executes the renaming module
# Calls:
#   tk_modules.get_file_list()
#   tk_modules.rename_extension()
# Parameters:
#   working_dir     str
#   old_ext         str
#   new_ext         str
# Returns:
#   error_logs
def rename_file_extensions(working_dir, old_ext, new_ext):
    # Declare Local Variable types (NOT parameters)
    error_logs = list()
    file_list = list()

    # 1. Create list of files
    file_list = tk_modules.get_file_list(working_dir)

    # 2. Rename extensions
    error_logs = tk_modules.rename_extension(working_dir, file_list, old_ext, new_ext)

    return error_logs
# End rename_file_extensions()

# Function rename_file_extensions()
# Description:
#   Takes in necessary parameters and executes the renaming module
# Calls:
#   tk_modules.get_file_list()
#   tk_modules.rename_extension()
# Parameters:
#   alphabatize     str/bool
#   root_path       str
# Returns:
#   error_logs
def organize_files(root_path, alphabatize='by_ext'):
    # Declare Local Variable types (NOT parameters)
    file_dict = dict()
    error_logs = list()

    # 1. Create file dict
    if alphabatize == True:
        file_dict = tk_modules.create_file_dictionary(root_path, '3')
    elif alphabatize == False:
        file_dict = tk_modules.create_file_dictionary(root_path, '2')
    else:
        file_dict = tk_modules.create_file_dictionary(root_path, '1')
    # End if

    # 2. Move files
    error_logs = tk_modules.move_files(root_path, file_dict)

    return error_logs
# End organize_files()

# Function delete_empty_directories()
# Description:
#   Delete all empty directories.
# Calls:
#   tk_modules.del_empty_dirs()
#   tk_modules.rename_extension()
# Parameters:
#   root_path     str
# Returns:
#   deletion_info
def delete_empty_directories(root_path):
    # Declare Local Variable types (NOT parameters)
    deletion_info = list()

    deletion_info = tk_modules.del_empty_dirs(root_path)

    return deletion_info
# End delete_empty_directories()

# End Module tk_options
