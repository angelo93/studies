males = int(input('Enter number of males:'))
females = int(input('Enter number of females:'))

total = males + females

percent_males = round((males / total) * 100)
percent_females = round((females / total) * 100)

print(f'Percent males: {percent_males}%')
print(f'Percent females: {percent_females}%')