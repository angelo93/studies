numerator = 1
denominator = 30
total = 0
result = 0

for iteration in range(1, 31):
    result = (numerator / denominator)
    # print(f'{result:5.2f}')

    # Update variables
    numerator += 1
    denominator -= 1
    total += result

    iteration += 1
# end for

# print(total)
print(f'{total:.3f}')