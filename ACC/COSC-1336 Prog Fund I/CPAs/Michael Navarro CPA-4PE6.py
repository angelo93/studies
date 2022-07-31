degree_C = int()
degree_F = float

print(format(' Centigrade'), '', format(' Fahrenheit'))

for degree_C in range(0, 21):
    degree_F = ((9 / 5) * degree_C) + 32
    # print(f'{degree_C:2}° celsius is {degree_F:.2f}° fahrenheit.')
    print(f'{degree_C:10.1f}°', '',  f'{degree_F:10.1f}°')
# end for