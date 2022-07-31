# Michael Navarro - Program #11

#--------------- Libraries ------------------#
from pathlib import Path
import os
import pyperclip
import time
import shutil
#--------------- Helper Functions ------------------#

#--------------- Requirement #1 ------------------#
'''Output a header in the console: “This is Program11 - <yournamehere>”'''
print('\nRequirement #1\n')
print('This is Program11 - Michael Navarro')

#--------------- Requirement #2 ------------------#
'''Print “This program demonstrates reading, writing, and organizing files.”'''
print('\nRequirement #2\n')
print('This program demonstrates reading, writing, and organizing files.')

#--------------- Requirement #3 ------------------#
'''Output the current working directory of the program.'''
print('\nRequirement #3\n')
print(os.getcwd())

#--------------- Requirement #4 ------------------#
'''Ask the user to enter the directory where they would like files to be stored, 
create that directory, and store files used below in that directory.'''
print('\nRequirement #4\n')

root_dir = os.getcwd()

user_dir = input('Please enter the directory where you would like future files to be stored: ')
user_dir = '\\' + user_dir

working_dir = root_dir + user_dir

try:
    os.mkdir(working_dir)
except:
    print('directory already exists.')


#--------------- Requirement #5 ------------------#
'''Write the following three lines to file_one.txt (without bullet points):
• Line 1 from file_one wrong_text
• Line 2 from file_ one wrong_text
• Line 3 from file_ one wrong_text'''
print('\nRequirement #5\n')

test_file1 = 'file_one.txt'
line_num = 1

with open(working_dir + '\\' + test_file1, 'w') as file1:
    for num in range(0, 3):
        file1.write(f'Line {line_num} from file_one wrong_text.\n')
        line_num += 1

print('Data written to file_one.txt')

#--------------- Requirement #6 ------------------#
'''Read and display the contents of file_one.txt.'''
print('\nRequirement #6\n')

with open(working_dir + '\\' + test_file1, 'r') as file1:
    for line in file1.readlines():
        print(line)

#--------------- Requirement #7 ------------------#
'''Replace the substring ‘file_one wrong_text’ in data read from file_one.txt 
with ‘file_two correct_text’ and write the corrected lines to file_two.txt.'''
print('\nRequirement #7\n')

file1_dataset = []
file1_corrected_dataset = []

test_file2 = 'file_two.txt'

with open(working_dir + '\\' + test_file1, 'r') as file1:
    file1_dataset = file1.readlines()

for data in file1_dataset:
    file1_corrected_dataset.append(data.replace('file_one wrong_text', 'file_two correct_text'))

with open(working_dir + '\\' + test_file2, 'w') as file2:
    for data in file1_corrected_dataset:
        file2.write(data)

print('Corrected data written to file_two.txt')

#--------------- Requirement #8 ------------------#
'''Ask the user to type the following lines (without bullet points) 
into a text editor and copy the lines to the clipboard (using Ctrl-c):
• Line 1 from the clipboard
• Line 2 from the clipboard
• Line 3 from the clipboard'''
print('\nRequirement #8\n')

print('''Please create an empty text file with the following three lines...
Line 1 from the clipboard
Line 2 from the clipboard
Line 3 from the clipboard
Then press "Ctrl + A" followed by "Ctrl + C" to copy the lines to your clipboard.
You will have 15 seconds to do this...
''')

limit = 10

while limit > -1: 
    mins, secs = divmod(limit, 60) 
    timer = '{:02d}:{:02d}'.format(mins, secs) 
    print(timer, end="\r") 
    time.sleep(1) 
    limit -= 1

#--------------- Requirement #9 ------------------#
'''Display the contents of the clipboard 
which should contain the three lines from Requirement 8.'''
print('\nRequirement #9\n')

print('The following has been found on your clipboard:\n')
print(pyperclip.paste())

#--------------- Requirement #10-12 ------------------#
'''10. Read the contents of file_two.txt and read the contents of the clipboard.

11. Append the contents of the clipboard onto the contents of file_two.txt line-by-line to produce the following:
• Line 1 from file_two correct_text followed by Line 1 from the clipboard
• Line 2 from file_two correct_text followed by Line 2 from the clipboard
• Line 3 from file_two correct_text followed by Line 2 from the clipboard

12. While performing Requirement 11, write the lines out to file_three.txt.'''
print('\nRequirement #10-12\n')

clipboard_data = pyperclip.paste().split('\n')
clipboard_corrected_data = []

test_file3 = 'file_three.txt'

file2_dataset = []
file2_formatted_dataset = []
file3_dataset = []

line_num = 0

for data in clipboard_data:
    clipboard_corrected_data.append(data.replace('\r', ''))

with open(working_dir + '\\' + test_file2, 'r') as file2:
    file2_dataset = file2.readlines()

for data in file2_dataset:
    file2_formatted_dataset.append(data.replace('.\n', ''))

with open(working_dir + '\\' + test_file3, 'w') as test3:
    for data in file2_formatted_dataset:
        file3_dataset.append(data + ' followed by ' + clipboard_corrected_data[line_num] + '.\n')
        test3.write(file3_dataset[line_num])
        line_num += 1

print('Data written to file_three.txt')

#--------------- Requirement #13 ------------------#
'''Display the contents of the file_three.txt.'''
print('\nRequirement #13\n')

with open(working_dir + '\\' + test_file3, 'r') as file3:
    for line in file3.readlines():
        print(line)

#--------------- Requirement #14 ------------------#
'''Ask the user for a new directory name. Create that directory and 
programmatically copy the files created earlier in the program to the new directory. 
Programmatically compress the files in the new directory.'''
print('\nRequirement #14\n')

new_dir = input('Please enter a new directory name to copy the files to: ')

new_working_dir = root_dir + '\\' + new_dir

try:
    os.mkdir(new_working_dir)
except:
    print('directory already exists.')

original_files = os.listdir(working_dir)

for filename in original_files:
    full_filename = os.path.join(working_dir, filename)
    shutil.copy(full_filename, new_working_dir)

print(f'\nFiles from {working_dir} moved to \n{new_working_dir}.')

#--------------- Requirement #15 ------------------#
'''Print a statement explaining your experiences with Program11. Make this authentic'''
print('\nRequirement #15\n')
print('''The part I liked most about this assignment was how to appraoch the manipulation of data.
It was fun figuring out how to encase it in a variable and then format it correctly to write it later.
I definitely enjoyed having a more overarching goal to work towards to than lots of little requirements to fulfill like in the last assignment.
Lastly, I learned a fun new way to create a countdown timer which I am excited to use in my other programs!''')