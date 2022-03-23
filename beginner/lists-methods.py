numbers = [5, 2, 1, 7, 7, 4]
numbers.append(20)
print(numbers)

numbers.insert(0, 10)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(7))

print(10 in numbers)

print(numbers.count(7))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)

numbers.clear()
print(numbers)

# Write a program to remove the duplicates in a list 
# My solution
list1 = [2, 2, 4, 6, 3, 4, 6, 1]
for num in list1:
    if list1.count(num) > 1:
        list1.remove(num)
print(list1)

# Video solution
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)



