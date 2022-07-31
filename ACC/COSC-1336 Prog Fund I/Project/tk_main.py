# Program tk_main
# Description: 
#   Allows the user to...
#       1. Rename file extensions
#       2. Organize by...
#           2a. Extensions
#           2b. Filename
#       3. Delete empty directores.
# Author: Michael Navarro 
# Date: 11/01/20
# Revised:
    # Functionality finished.
    # 11/09/2020
    # 11/13/2020
    # 11/28/2020

    # Gui implemented.
    # 12/08/2020
    # 12/09/2020

# list libraries used
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import tk_options
import os
# End libraries

# Class Name: popupExtWindow
# Description: 
# 	Pops up a little window to get required info to execute renaming extensions option.
# Author: Michael Navarro
#
# Data Attributes:
#  old_lbl     Tkinter.Label  Public
#  new_lbl     Tkinter.Label  Public
# 
#  old_ext     Tkinter.Entry  Public
#  new_ext     Tkinter.Entry  Public
# 
#  select_dir_button    Tkinter.Button Public
#  done                 Tkinter.Button Public
#
# Methods:
#  select_dir   Public
#  cleanup      Public

class popupExtWindow():
    # *********************** Data Attributes *********************
    # self.dir = dict()
    # self.value = list()
    
    # self.old_lbl = tk.Label()
    # self.new_lbl = tk.Label()
    # self.old_ext = tk.Entry()
    # self.new_ext = tk.Entry()
    # self.select_dir_button = tk.Button()
    # self.done = tk.Button()

    # *********************** Methods ****************************
    # Method __init__()
    # Description:
    #  Constructor/Initializer
    # Calls:
    #	os.getcwd()
    #	tk.Button()
    #	tk.Label()
    #	tk.Entry()
    #	tk.grid()
    # Parameters:
    #   master     tk.Tk()
    # Returns:
    #	none
    def __init__(self, master):
        top = self.top = tk.Toplevel(master)

        self.old_lbl = tk.Label(top, text='Old Ext:')
        self.old_lbl.grid(row=0, column=0, pady=2)

        self.old_ext = tk.Entry(top)
        self.old_ext.grid(row=0, column=1, pady=2)

        self.new_lbl = tk.Label(top, text='New Ext:')
        self.new_lbl.grid(row=1, column=0, pady=2)

        self.new_ext = tk.Entry(top)
        self.new_ext.grid(row=1, column=1, pady=2)

        self.select_dir_button = tk.Button(top, text='Select Directory', padx=50, pady=15, command=self.select_dir)
        self.select_dir_button.grid(row=2, column=0, columnspan=2, pady=2)

        self.done = tk.Button(top, text='OK', padx=83, pady=15, command=self.cleanup)
        self.done.grid(row=3, column=0, columnspan=2, pady=2)
    # End __init__()

    # Method del_empty_dirs()
    # Description:
    #  Prompts user to select a directory.
    # Calls:
    #	filedialog.askdirectory()
    # Parameters:
    #   none
    # Returns:
    #	none
    def select_dir(self):
        '''Have user select the directory to rename extensions in.'''

        self.dir = filedialog.askdirectory()
    # End select_dir()

    # Method celanup()
    # Description:
    #  Celans up popup instance.
    # Calls:
    #	self.top.destroy()
    # Parameters:
    #   none
    # Returns:
    #	none
    def cleanup(self):
        '''Record values taken and destroy window instance.'''

        self.value = [self.dir, self.old_ext.get(), self.new_ext.get()]
        self.top.destroy()
    # End cleanup()

# End popupExtWindow()

# Class Name: mainWindow
# Description: 
# 	Main window in which the program runs.
# Author: Michael Navarro
#
# Data Attributes:
#  root_path                Str             Public
# 
#  rename_button            Tkinter.Button  Public
#  org_by_ext_button        Tkinter.Button  Public
#  org_by_filename_btn      Tkinter.Button  Public
#  del_empty_dirs_btn       Tkinter.Button  Public
#  update_root_path_btn     Tkinter.Button  Public
# 
#  log                      Tkinter.Text    Public
#
# Methods:
#  show_defualt_info        Public
#  disable_btns             Public
#  enable_btns              Public
#  ext_popup                Public
#  rename_extensions        Public
#  org_files                Public
#  del_empty_dirs           Public
#  update_root_path         Public
#  write_to_log             Public

class mainWindow():
    # *********************** Data Attributes *********************
    # self.root_path = str()
    
    # self.master = tk.Tk()
    # self.rename_button = tk.Button()
    # self.org_by_ext_button = tk.Button()
    # self.org_by_filename_btn = tk.Button()
    # self.del_empty_dirs_btn = tk.Button()
    # self.update_root_path_btn = tk.Button()
    # self.log = tk.Text()
    
    # self.ext_popup = popupExtWindow()

    # *********************** Methods ****************************
    # Method __init__()
    # Description:
    #  Constructor/Initializer
    # Calls:
    #	os.getcwd()
    #	tk.button()
    #	tk.text()
    #	tk.grid()
    # Parameters:
    #   master     tk.Tk()
    # Returns:
    #	none
    def __init__(self, master):
        self.master = master
        self.root_path = os.getcwd()
        
        self.rename_button = tk.Button(master, text='Rename File Extension', padx=50, pady=15, command=self.rename_extensions)
        self.rename_button.grid(row=0, column=0, sticky='nswe', padx=2, pady=1)

        self.org_by_ext_button = tk.Button(master, text='Organize Files By Extension', padx=50, pady=15, command=self.org_files)
        self.org_by_ext_button.grid(row=1, column=0, sticky='nswe', padx=2, pady=1)

        self.org_by_filename_btn = tk.Button(master, text='Organize Files By Filename', padx=50, pady=15, command=lambda: self.org_files(by_ext=False))
        self.org_by_filename_btn.grid(row=2, column=0, sticky='nswe', padx=2, pady=1)

        self.del_empty_dirs_btn = tk.Button(master, text='Delete Empty Directories', padx=50, pady=15, command=self.del_empty_dirs)
        self.del_empty_dirs_btn.grid(row=3, column=0, sticky='nswe', padx=2, pady=1)

        self.update_root_path_btn = tk.Button(master, text='Change Root Directory', padx=50, pady=15, command=self.update_root_path)
        self.update_root_path_btn.grid(row=4, column=0, sticky='nswe', padx=2, pady=1)
        
        self.log = tk.Text(root, state='disabled', height=24, width=90)
        self.log.grid(row=0, rowspan=5, column=1, sticky='nswe')
    # End __init__()
    
    # Method show_default_info()
    # Description:
    #  Displays a popup message with current root directory.
    # Calls:
    #	self.disable_btns()
    #	self.enable_btns()
    #	messagebox.showinfo()
    # Parameters:
    #   master     tk.Tk()
    # Returns:
    #	none
    def show_default_info(self):
        '''Displays default root directory. 
        User has to click ok before continuing ensuring they know which directory they are working in.'''

        self.disable_btns()
        messagebox.showinfo(message=f'Current Root Directory:\n{self.root_path}')
        self.enable_btns()
    # End show_defualt_info()

    # Method disable_btns()
    # Description:
    #  Disables buttons.
    # Calls:
    #	none
    # Parameters:
    #   none
    # Returns:
    #	none
    def disable_btns(self):
        '''Disable buttons when user is executing an option.'''

        self.rename_button["state"] = "disabled"
        self.org_by_ext_button["state"] = "disabled"
        self.update_root_path_btn["state"] = "disabled"
        self.org_by_filename_btn["state"] = "disabled"
        self.del_empty_dirs_btn["state"] = "disabled"
    # End disable_btns()

    # Method enable_btns()
    # Description:
    #  enables buttons.
    # Calls:
    #	none
    # Parameters:
    #   none
    # Returns:
    #	none
    def enable_btns(self):
        '''Enable buttons when user is done executing an option.'''

        self.rename_button["state"] = "normal"
        self.org_by_ext_button["state"] = "normal"
        self.update_root_path_btn["state"] = "normal"
        self.org_by_filename_btn["state"] = "normal"
        self.del_empty_dirs_btn["state"] = "normal"
    # End enable_btns()

    # Method enable_btns()
    # Description:
    #  enables buttons.
    # Calls:
    #	popup_extWindow()
    #	self.disable_btns()
    #	self.enable_btns()
    #	self.master.wait_window()
    # Parameters:
    #   none
    # Returns:
    #	none
    def ext_popup(self):
        '''Brings up a popup to get required info for renaming of extensions.'''

        self.ext_name_window = popupExtWindow(self.master)
        self.disable_btns()
        self.master.wait_window(self.ext_name_window.top)
        self.enable_btns()
    # End ext_popup()
    
    # Method enable_btns()
    # Description:
    #  Renames file extensions.
    # Calls:
    #	self.ext_popup()
    #	self.write_to_log()
    #	tk_options.rename_file_extensions()
    # Parameters:
    #   none
    # Returns:
    #	none
    def rename_extensions(self):
        # Variables
        working_dir = str()
        old_ext = str()
        new_ext = str()

        error_logs = list()

        # Bring up popup window
        self.ext_popup()

        # Record user specifications.
        working_dir = self.ext_name_window.value[0]
        old_ext = self.ext_name_window.value[1]
        new_ext = self.ext_name_window.value[2]

        # Execute option
        error_logs = tk_options.rename_file_extensions(working_dir, old_ext, new_ext)

        # Print out logs
        if len(error_logs) > 0:
            for error_log in error_logs:
                error_log = error_log.replace('/', '\\')
                self.write_to_log(msg=f'\n{error_log}')
            # End for
        # End if

        self.write_to_log(msg=f'\nFile extensions renamed from: .{old_ext} --> .{new_ext}')
        self.write_to_log(msg='-' * 90)
    # End rename_extensions()
        
    # Method prg_files()
    # Description:
    #  Organize files according to user constraints.
    # Calls:
    #	tk_options.organize_files()
    #	messagebox.askyesno()
    #	self.write_to_log()
    # Parameters:
    #   by_ext      bool
    # Returns:
    #	none
    def org_files(self, by_ext=True):
        '''Organize files depending on user constraints.'''

        #Variables
        error_logs = list()
        exist_errors = list()
        not_found_errors = list()

        alphabatize = bool()

        # Organize by extension
        if by_ext == True:
            error_logs = tk_options.organize_files(self.root_path)
        # Organize by filename
        else:
            alphabatize = messagebox.askyesno(message='Would you like to organize the directories alphabetically after sorting?')
            error_logs = tk_options.organize_files(self.root_path, alphabatize)
        # End if

        exist_errors = error_logs[0]
        not_found_errors = error_logs[1]

        #---------- Write logs ----------
        if len(exist_errors) > 0:
            for exist_error in exist_errors:
                exist_error = exist_error.replace('/', '\\')
                self.write_to_log(msg=f'\n{exist_error}')
            # End for
        # End if

        if len(not_found_errors) > 0:
            for not_found_error in not_found_errors:
                not_found_error = not_found_error.replace('/', '\\')
                self.write_to_log(msg=f'\n{not_found_error}')
            # End for
        # End if
        #---------- End Write Logs ----------

        self.write_to_log(msg='All files able to be organized have been organized.')
        self.write_to_log(msg='-' * 90)
    # End org_files()

    # Method del_empty_dirs()
    # Description:
    #  Delete empty directories.
    # Calls:
    #	tk_options.delete_empty_directories()
    #	messagebox.askyesno()
    #	self.write_to_log()
    # Parameters:
    #   by_ext      bool
    # Returns:
    #	none
    def del_empty_dirs(self):
        '''Delete empty directories'''

        # Variables
        del_dirs = bool()

        deletion_info = list()
        error_logs = list()

        num_deleted_dirs = int()

        del_dirs = messagebox.askyesno(message='Are you sure you want to delete all empty directories?') 

        if del_dirs == True:
            deletion_info = tk_options.delete_empty_directories(self.root_path)
            num_deleted_dirs = deletion_info[0]
            error_logs = deletion_info[1]

            if len(error_logs) > 0:
                for error_log in error_logs:
                    error_log = error_log.replace('/', '\\')
                    self.write_to_log(msg=f'\n{error_log}')
                # End for
            # End if

            if num_deleted_dirs > 0:
                self.write_to_log(msg=f'\nEmpty directories deleted: {num_deleted_dirs}')
            else:
                self.write_to_log(msg='\nThere were no empty directories to delete.')
            # End if
        else:
            self.write_to_log(msg='\nEmpty Directories Not Deleted.')
        # End if
        
        self.write_to_log(msg='-' * 90)
    # End del_empty_dirs()
    
    # Method del_empty_dirs()
    # Description:
    #  Update the root path variable.
    # Calls:
    #	filedialog.askdirectory()
    #	os.getcwd()
    #   self.write_to_log()
    # Parameters:
    #   none
    # Returns:
    #	none
    def update_root_path(self):
        '''Update current root directory'''

        # Variables
        new_root = str()

        new_root = filedialog.askdirectory()

        if new_root == '':
            new_root = os.getcwd()
        # End if
        
        self.root_path = new_root
        new_root = new_root.replace('/', '\\')

        self.write_to_log(f'\nNew Root Dir:\n{new_root}')
        self.write_to_log(msg='-' * 90)
    # End update_root_path()
    
    # Method write_to_log()
    # Description:
    #  Write to log window.
    # Calls:
    #   self.log.index()
    #   self.log.insert()
    #   self.log.see()
    # Parameters:
    #   msg     str
    # Returns:
    #	none
    def write_to_log(self, msg):
        '''Write to log window. 
        Unless writing to the log, it is disabled.'''

        self.log['state'] = 'normal'
        
        if self.log.index('end-1c')!='1.0':
            self.log.insert('end', '\n')
        # End if

        self.log.insert('end', msg)
        self.log['state'] = 'disabled' 
        self.log.see('end')
    # End write_to_log

# End mainWindow()

if __name__ == "__main__":
    root = tk.Tk()
    main = mainWindow(root)
    main.show_default_info()
    main.write_to_log(f'Current Root Dir:\n{main.root_path}')
    main.write_to_log(msg='-' * 90)
    root.mainloop()