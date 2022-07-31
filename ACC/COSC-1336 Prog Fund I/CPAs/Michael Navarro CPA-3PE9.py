pocket_num = str()

pocket_num = input('Please enter a pocket number from 0-36: ').strip()
pocket_num = int(pocket_num)
pocket_num = round(pocket_num)

if (pocket_num > 36):
    print('ERROR NUMBER OUTSIDE OF BOUNDS')
elif (pocket_num == 0):
    print('The pocket color for the number 0 is GREEN!')

elif ((pocket_num <=10) and (pocket_num % 2 == 0)):
    print('The pocket color for even numbers between 1-10 is BLACK!')
elif ((pocket_num <=10) and (pocket_num % 2 != 0)):
    print('The pocket color for odd numbers between 1-10 is RED!')

elif ((pocket_num <=18) and (pocket_num % 2 == 0)):
    print('The pocket color for even numbers between 11-18 is RED!')
elif ((pocket_num <=18) and (pocket_num % 2 != 0)):
    print('The pocket color for odd numbers between 11-18 is BLACK!')

elif ((pocket_num <=28) and (pocket_num % 2 == 0)):
    print('The pocket color for even numbers between 19-28 is BLACK!')
elif ((pocket_num <=28) and (pocket_num % 2 != 0)):
    print('The pocket color for odd numbers between 19-28 is RED!')

elif ((pocket_num <=36) and (pocket_num % 2 == 0)):
    print('The pocket color for even numbers between 29-36 is RED!')
elif ((pocket_num <=36) and (pocket_num % 2 != 0)):
    print('The pocket color for odd numbers between 29-36 is BLACK!')
# end if