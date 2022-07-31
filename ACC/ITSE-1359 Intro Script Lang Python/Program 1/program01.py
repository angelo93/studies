# program01.py

print('\nRequirement #1\n')
print('This is Program 1 - Michael Navarro\n')

print('Requirement #2\n')
print('Please enter the information requested.\n')
name = input('Last Name: ')
hometown = input('Hometown: ')
occupation = input('Occupation: ')
hobby = input('Hobby: ')

print('\nRequirement #3\n')
print('Hello {}!'.format(name))
print('From {}.'.format(hometown))
print('I hope you like being a(n) {}.'.format(occupation))
print('{} sounds like an interesting hobby.'.format(hobby))

print('\nRequirement #4\n')
print('Alternative Output\n')
print('Hello', name, '!')
print('From ' + hometown + '.')
print('I hope you like being a(n)', occupation)
print(hobby + ' sounds like an interesting hobby.')

print('\nRequirement #5\n')
print('More Options\n')
print('Hello1 ', name, '!')
print('Hello2 ', name, '!', sep='')
print('Hello3 ', name, '!', end='', sep='')
print('Hello4 ', name, '!', end='', sep='')
print('Hello5 ', name, '!', end='', sep='')

print('\n\nRequirement #6\n')
print('''This was a fun little program.
I learned about the "end" and "sep" variables for print statements.
It made for a lovely little refresher and I can't wait to continue these assignment!''')