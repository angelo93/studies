# Michael Navarro - Program #12

#--------------- Libraries ------------------#
import pyperclip
import time
import webbrowser
import bs4
import requests
import openpyxl

#--------------- Helper Functions ------------------#

#--------------- Requirement #1 ------------------#
'''Output a header in the console: “This is Program12 - <yournamehere>”'''
print('\nRequirement #1\n')
print('This is Program12 - Michael Navarro')

#--------------- Requirement #2 ------------------#
'''Print “This program demonstrates using Python to perform web scraping 
and working with Excel spreadsheets.”'''
print('\nRequirement #2\n')
print('This program demonstrates using Python to perform web scraping and working with Excel spreadsheets.')

#--------------- Requirement #3 ------------------#
'''Ask the user to copy a U.S. street address to the clipboard. 
Programmatically open a web browser with Google maps 
pointing to the address supplied by the user.'''
print('\nRequirement #3\n')

print('Please highlight and copy a US Address to your clipboard.\n')

limit = 10
map_URL = 'https://www.google.com/maps/place/'

while limit > -1: 
    mins, secs = divmod(limit, 60) 
    timer = '{:02d}:{:02d}'.format(mins, secs) 
    print(timer, end="\r") 
    time.sleep(1) 
    limit -= 1

user_address = pyperclip.paste()
full_URL = map_URL + user_address

print(f'\n Thank you, the provided address will now be shown in your browser.')

webbrowser.open(full_URL)

#--------------- Requirement #4 ------------------#
'''Ask the user to enter the URL of a web page. 
Programmatically select the <p> elements on the page and display the text of each <p>.'''
print('\nRequirement #4\n')

user_URL = input('Please enter the URL of a web page you would like to scrape:\n')

# Grab HTML from given URL and grab only the <p> elements
req_URL = requests.get(user_URL)
user_soup = bs4.BeautifulSoup(req_URL.text, 'html.parser')
user_ps = user_soup.select('p')
# End <p> selection

for paragraph in user_ps:
    print(f'\n{paragraph.getText()}')

#--------------- Requirement #5 ------------------#
'''Create a class named ExcelProcessing. 
Use that class and any other functions you may need to organize the operations of this program. 
Include the data and functions in the class to perform the requirements below.'''
print('\nRequirement #5\n')

print('ExcelProcessing class defined.')

class ExcelProcessing:
    '''Class for processing excel files
    Every instance should pass in a filename for a workbook as an argument'''

    def __init__(self, workbook_name):
        self.wb_name = workbook_name
        self.workbook = openpyxl.load_workbook(workbook_name)
        self.wb_sheets = self.workbook.sheetnames

    def display_wb_sheets(self):
        print(f'\nThe workbook {wb_name} contains the following sheets...\n') 

        count = 1
        for sheet in self.wb_sheets:
            print(f'{count}. {sheet}')
            count += 1

    def display_active_cells(self):
        for sheet in self.workbook:
            print(f'\n---------- Showing active cells in {sheet.title} ----------')
            for cell in sheet:
                print(cell)

    def display_cell_data(self, sheet_name, cell_name):
        cell_name = cell_name.upper()
        active_sheet = self.workbook[sheet_name]

        print(f'\nThe value of cell {cell_name} in {sheet_name} is: {active_sheet[cell_name].value}')

    def display_selection(self, sheet_name, start_cell, end_cell):
        start_cell = start_cell.upper()
        end_cell = end_cell.upper()

        active_sheet = self.workbook[sheet_name]
        selection = active_sheet[start_cell:end_cell]

        print('\nShowing value of cells for the specified selection.\n')

        for row in selection:
            for cell in row:
                print(cell.coordinate, cell.value)
            print('--- END OF ROW---\n')
# End ExcelProcessing Definition

wb_name = input('\nPlease enter the name of the excel file you wish to process: ')
ex_process = ExcelProcessing(wb_name)

print(f'\nNew instance of ExcelProcessing initialized with the file "{wb_name}".')

#--------------- Requirement #6 ------------------#
'''Display the list of sheets in example.xlsx.'''
print('\nRequirement #6\n')

ex_process.display_wb_sheets()

#--------------- Requirement #7 ------------------#
'''Inform the user of cells that can be read from example.xlsx 
and ask the user to enter a cell (e.g. B7). 
Display the value located in that cell (e.g. Strawberries).'''
print('\nRequirement #7')
show_cell_data = True
sheet_choice = ''
cell_choice = ''

while show_cell_data == True:
    choice = input('\nWould you like to see the data from a particular cell? (Y/N): ').upper()

    if choice == 'Y':
        ex_process.display_active_cells()
        sheet_choice = input('\nPlease enter the name of the sheet you wish to process: ')

        cell_choice = input('\nPlease enter the cell name to view: ')
        ex_process.display_cell_data(sheet_choice, cell_choice)
    else:
        show_cell_data = False
# End showing data of a chosen cell
    
#--------------- Requirement #8 ------------------#
'''Ask the user to enter a rectangular section from example.xlsx (e.g. A3:C7).
Display the values in the cells of that rectangular section.'''
print('\nRequirement #8')
show_selection_data = True
selection_start = ''
selection_end = ''
sheet_choice = ''

while show_selection_data == True:
    choice = input('\nWould you like to see the data from a specified rectangular selection? (Y/N): ').upper()

    if choice == 'Y':
        ex_process.display_active_cells()
        sheet_choice = input('\nPlease enter the name of the sheet you wish to process: ')

        selection_start = input('\nPlease enter the starting cell: ')
        selection_end = input('\nPlease enter the ending cell: ')

        ex_process.display_selection(sheet_choice, selection_start, selection_end)
    else:
        show_selection_data = False
# End showing data of a chosen selection

#--------------- Requirement #9 ------------------#
'''Print a statement explaining your experiences with Program12. Make this
authentic (minimum of 2-3 sentences).'''
print('\nRequirement #9')

print('''I learned a lot doing this assignment. To this point I had never processed an Excel Sheet with Python.
During the course of the assignment I couldn't help but see where I could implement previous assignment requirements into this assignment.
For example, to ensure the user only enters an applicable cell name (E.G. "A1") you could implement a regular expression validation.
This was not my first time web scraping with beautiful soup, however I still had fun using BS again as web scrapping is a fun activity to me.''')

