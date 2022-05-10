print("""
PROGRAMMING 

- Algorithms 
    - A set of rules or steps used to solve a problem 
- Data Structures 
    - A particular way of organizing data in a computer
-------------------------------------------------------- 
WHAT IS NOT A "COLLECTION"

- Most of our variables have one value in them - when we put a new 
value in the variable, the old value is overwritten

x = 2 
x = 4
Output:
""")
x = 2
x = 4 
print(x)
print("""
-------------------------------------------------------------
A LISTS IS A KIND OF COLLECTION

- A collection allows us to put many values in a single "variable"
- A collectio is nice because we can carry many values around in one 
convenient package.
Ex.
friends = ['Joseph', 'Glenn', 'Sally]
carryon = ['socks', 'shirt', 'perfume']
-------------------------------------------------------------
LIST CONSTANTS 

- List constants are surrounded by square brackets and the elements in
the list are seperated by commas 
- A list elemnet can be any Pythonn object - even another list 
- A list can be empty 

print([1, 24, 76])
Output:
""")
print([1, 24, 76])
print("""
print(['red', 'yellow', 'blue'])
Output:
""")
print(['red', 'yellow', 'blue'])
print("""
print(['red', 24, 98.6])
Output:
""")
print(['red', 24, 98.6])
print("""
print([1, [5, 6], 7])
Output:
""")
print([1, [5, 6], 7])
print("""
print([])
Output:
""")
print([])
print("""
LISTS AND DEFINITE LOOPS - BEST PALS

Ex.
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

z = ['Joseph', 'Glenn', 'Sally']
for x in z:
    print('Happy New Year:', x)
print('Done!')
----------------------------------------------------------
LOOKING INSIDE LISTS 

- Just like strings, we can get at any single element in a list using
an index specified in square brackets
John  Glenn  Sally
0     1      2

friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])
Output:
""")
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])
print("""
LISTS ARE MUTABLE

- Strings are 'immutable' - we cannot change the contents of a string -
we must make a new string to make any change 
- Lists are "mutable" - we can change an element of a list using the 
index operator 

fruit = 'Banana'
fruit[0] = 'b'
Output:
""")
try: 
    fruit = 'Banana'
    fruit[0] = 'b'
except:
    print("""
    Traceback
    TypeError: 'str' object does not support item assigment 
    """)
print("""
x = fruit.lower()
print(x)
Output:
""")
x = fruit.lower()
print(x)
print("""
lotto = [2, 14, 26, 41, 63]
print(lotto)
Output:
""")
lotto = [2, 14, 26, 41, 63]
print(lotto)
print("""
lotto[2] = 28
print(lotto)
Output:
""")
lotto[2] = 28
print(lotto)

print("""
------------------------------------------------------------
HOW LONG IS A LIST?

- The len() function takes a list as a parameter and returns the 
number of elements in the list 
- Actually left() tells us the number of elements of any set or 
sequence(such as a string....)

greet = 'Hello Bob'
print(len(greet))
Output:
""")
greet = 'Hello Bob'
print(len(greet))
print("""
x = [1, 2, 'joe', 99]
print(len(x))
Output:
""")
x = [1, 2, 'joe', 99]
print(len(x))
print('------------------------------------')

print("""
USING THE RANGE FUNCTION

- The range function returns a list of numbers that range from
zero to one less than the parameter 
- We can construct an index loop for and an integer iterator 

print(range(4))
Output:
""")
print(range(4))
print("""
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends)) 
Output:
""")
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends)) 
print("""
print(range(len(friends)))
Output: 
""")
print(range(len(friends)))
print('----------------------------------------')

print("""
A TALE OF TWO LOOPS... 

Ex.
friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends:
    print('Happy New Year:', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)
------------------------------------------------
CONCATENATING LISTS USING +

- We can create a new list by adding two existing lists together 

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
Output:
""")
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print("""
print(a)
Output: 
""")
print(a)
print("""
----------------------------------------------------------------
LISTS CAN BE SLICED USING:

- Remember: Just like in strings, the second number is "up to but 
not including"

t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
Output:
""")
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print("""
print(t[:4])
Output: 
""")
print(t[:4])
print("""
print(t[3:])
Output: 
""")
print(t[3:])
print("""
print(t[:])
Output: 
""")
print(t[:])
print("""
BUILDING A LIST FROM SCRATCH

- We can create an empty list and then add elements using the
append method 
- The list stays in order and new elements are added at the end of
the list 

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
Output:
""")
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
print("""
stuff.append('cookie')
print(stuff)
Output: 
""")
stuff.append('cookie')
print(stuff)
print("""
-------------------------------------------------------------------
IS SOMETHING IN A LIST?

- Python provides two operators that let you check if an item is 
in a list
- These are logical operators that return True or False 
- They do not modify the list 

some = [1, 9, 21, 10, 16]
print(9 in some)
Output:
""")
some = [1, 9, 21, 10, 16]
print(9 in some)
print("""
print(15 in some)
Output: 
""")
print(15 in some)
print("""
print(20 not in some)
Output: 
""")
print(20 not in some)

print("""
--------------------------------------------------------------
LISTS ARE IN ORDER 

- A list can hold many items and keeps those items in the order
until we do something to change the order 
- A list can be sorted(i.e, change its order)
- The sort method (unlike in strings) means "sort yourself"

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
Output:
""")
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print("""
print(friends[1])
Output: 
""")
print(friends[1])
print("""
-----------------------------------------------------------------
BUILT-IN FUNCTIONS AND LISTS 

- There are a number of functions built into Python that take lists 
as parameters
- Remember the loops we built? These are much simpler. 

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
Output:
""")
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print("""
print(max(nums))
Output: 
""")
print(max(nums))
print("""
print(min(nums))
Output: 
""")
print(min(nums))
print("""
print(sum(nums))
Output: 
""")
print(sum(nums))
print("""
print(sum(nums)/len(nums))
Output: 
""")
print(sum(nums)/len(nums))
print("""
----------------------------------------------------------
CALCULATING AVERAGE 

total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)
Output:
""")
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)
print("""
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
Output:
""")
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
print('----------------------------------------------------')










































