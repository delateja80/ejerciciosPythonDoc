# switch.py
day_number = 3
if 1 <= day_number <= 5:
 day = 'Weekday'
elif day_number == 6:
 day = 'Saturday'
elif day_number == 0:
 day = 'Sunday'
else:
 day = ''
 raise ValueError(
 str(day_number) + ' is not a valid day number.')
print (day)