n = 39
remainders = []
while n > 0:
 n, remainder = divmod(n, 2)
 remainders.append(remainder)
remainders.reverse()
print(remainders)

people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
position = 0
while position < len(people):
 person = people[position]
 age = ages[position]
 print(person, age)
 position += 1