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
