names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[0])
print(names[2])
print(names[-1])
print(names[-2])
print(names[2:])
print(names[2:4])
print(names[2:])
print(names)

names[0] = 'Jon'
print(names)

numbers = [3, 6, 2, 10, 8, 4]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number 
print(max)

