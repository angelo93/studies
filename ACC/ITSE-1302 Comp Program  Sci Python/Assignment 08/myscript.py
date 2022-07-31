def cube(num):
    '''Return the cube of num'''
    num_cubed = num ** 3
    return num_cubed
# end cube()

for num in range(1, 5):
    print(f'The cube of {num} is : {cube(num)}')
# end for