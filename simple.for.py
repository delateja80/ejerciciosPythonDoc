print('for simple')
for number in [0, 1, 2, 3, 4]:
 print(number) 
print('for range')
for number in range(5):
 print(number) 
print('for sequence')
surnames = ['Rivest', 'Shamir', 'Adleman']
for position in range(len(surnames)):
 print(position, surnames[position]) 
print('---------')
surnames = ['Rivest', 'Shamir', 'Adleman']
for surname in surnames:
 print(surname) 
print('---------')
surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames):
 print(position, surname) 