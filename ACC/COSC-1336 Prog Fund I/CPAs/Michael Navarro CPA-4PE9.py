YEARLY_RISE = 1.6
current_rise = 0

for year in range(1, 26):
    current_rise += YEARLY_RISE
    if year == 1:
        print(f'In {year:2} year the ocean will have risen by...  {current_rise:5.2f}mm.')
    else:
        print(f'In {year:2} years the ocean will have risen by... {current_rise:5.2f}mm.')
    # end if
# end for