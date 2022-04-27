print("""
STRING DATA TYPE

- A string is a sequence of characters 
- A string literal uses quotes 'Hello' or "Hello"
- For strings, + means 'concatenate'
- When a string contains numbers, it is still a string
- We can convert numbers in a string into a number using int()
---------------------------------------------------------------
READING AND CONVERTING

- We prefer to read data in using strings and then parse and convert the 
data as we need 
- This gives us more control over error situations and/or bad user input
- Raw input numbers must be converted from strings 
------------------------------------------------------------------
LOOKING INSIDE STRINGS 

- We can get at any single character in a string using an index specified 
in square brackets 
- The index value must be an integer and starts at zero
- The index value can be an expression that is computed

fruit = 'banana'
letter = fruit[1]
print(letter)
Output: 
""")
fruit = 'banana'
letter = fruit[1]
print(letter)
print("""
x = 3 
w = fruit[x - 1]
print(w)
Output:
""")
x = 3 
w = fruit[x - 1]
print(w)
print('---------------------')

print("""
A CHARACTER TOO FAR

- You will get a python error if you attempt to index beyond the end of a
string 
- So be careful when constructing index values and slices

zot = 'abc'
print(zot[5])
Output:

IndexError: string index out of range 
-------------------------------------------------------------
""")

print("""
STRINGS HAVE LENGTH

- The built-in function len gives us the length of a string 

fruit = 'banana'
print(len(fruit))
Output:
""")
fruit = 'banana'
print(len(fruit))
print('-----------------------------------------')

print("""
LOOPING THROUGH STRINGS

- Using a while statement and an iteration variable, and the len function,
we can construct a loop to look at each of the letters in a string 
individually

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit(index)
    print(index, letter)
    index = index + 1
Output:
""")
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
print("""
- A definite loop using a for statement is much more elegant 
- The iteration variable is completely taken care of by the for loop

fruit = 'banana'
for letter in fruit:
    print(letter)
Output:
""")
fruit = 'banana'
for letter in fruit:
    print(letter)
print('------------------------------------')

print("""
LOOPING AND COUNTING 

- This is a simple loop that loops through each letter in a string
and counts the number of times the loop encounters the 'a' character

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
Output:
""")
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
print('--------------------------------------')

print("""
LOOKING DEEPER INTO IN

- The iteration variable 'iterates' through the sequence (ordered set)
- The block (body) of code is executed once for each value in the 
sequence 
- The iteration variable moves through all of the values in the 
sequence

# letter is the iteration variable 
# six-character string 
for letter in 'banana':
    print(letter)
Output:
""")
for letter in 'banana':
    print(letter)
print('----------------------------------------')

print("""
SLICING STRINGS

- We can also look at any continous section of a string using a colon
operator 
- The second number is one beyond the end of the slice - "up to but not
including"
- If the second number is beyond the end of the string, it stops at the 
end 
- If we leave off the first number or the last number of the slice, it is
assumed to be the beginning or end of the string respectively

s = 'Monty Python'
print(s[0:4])
Output:
""")
s = 'Monty Python'
print(s[0:4])
print('--------------------------------------')

print("""
STRING CONCATENATION

- When the + operator is applied to strings, it means "concatenation"

a = 'Hello'
b = a + 'There'
print(b)
Output:
""")
a = 'Hello'
b = a + 'There'
print(b)
print('-------------------------------------------')

print("""
USING IN AS A LOGICAL OPERATOR

- The in keyword can also be used to check to see if one string is "in"
another string 
- The in expression is a logical expression that returns True or False and
can be used in an if statement 

fruit = 'banana'
print('n' in fruit)
Output:
""")
fruit = 'banana'
print('n' in fruit)
print('------------------------')

print("""
STRING LIBRARY

- Python has a number of string functions which are in the string library
- These functions are already built into every string - we invoke them by 
appending the function to the string variable 
- These functions do not modify the original string, instead they return
a new string that has been altered

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
Output:
""")
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print("""
print(greet)
Output:
""")
print(greet)
print("""
print('Hi There'.lower())
Output:
""")
print('Hi There'.lower())
print('-----------------------------------------------')


print("""
SEARCHING A STRING

- We use the find() function to search for a substring within another
string 
- find() finds the first occurence of the substring
- If the substring is not found, find() returns -1
- Remember that string position starts at zero

fruit = 'banana'
pos = fruit.find('na')
print(pos)
Output:
""")
fruit = 'banana'
pos = fruit.find('na')
print(pos)
print("""
aa = fruit.find('z')
print(aa)
Output:
""")
aa = fruit.find('z')
print(aa)
print('-----------------------------------------------------------')

print("""
MAKING EVERYTHING UPPER CASE

- You can make a copy of a string in lower case or upper case 
- Often when we are searching for a string using find() we first convert
the string to lowercase so we can search a string regardless of case

greet = 'Hello Bob'
nnn = greet.upper()
Output:
""")
greet = 'Hello Bob'
nnn = greet.upper()
print("""
www = greet.lower()
print(www)
Output:
""")
www = greet.lower()
print(www)
print('-----------------------------------------------------')

print("""
SEARCH AND REPLACE

- The replace() function is like a "search and replace" operation in a 
word processor
- It replaces all occurrences of the search string with the replacement 
string

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
Output:
""")
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
print("""
nstr = greet.replace('o', 'X')
print(nstr)
Output:
""")
nstr = greet.replace('o', 'X')
print(nstr)
print('------------------------------------------------------')


print("""
STRIPPING WHITESPACE

- Sometimes we want to take a string and remove whitespace at the beginning
and/or end
- lstrip() and rstrip() remove whitespace at the left or right 
- strip() removes both beginning and ending whitespace

greet = '               Hello Bob    '
print(greet.lstrip())
Output:
""")
greet = '               Hello Bob    '
print(greet.lstrip())
print("""
print(greet.rstrip())
Output:
""")
print(greet.rstrip())
print("""
print(greet.strip())
Output:
""")
print(greet.strip())
print('------------------------------------------------')

print("""
PREFIXES

line = 'Please have a nice day'
print(line.startswith('Please'))
Output:
""")
line = 'Please have a nice day'
print(line.startswith('Please'))
print("""
print(line.startswith('p'))
Output:
""")
print(line.startswith('p'))
print('---------------------------------------')

print("""
PARSING AND EXTRACTING 

- From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
Output:
""")
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
print("""
sppos = data.find(' ', atpos)
print(sppos)
Output:
""")
sppos = data.find(' ', atpos)
print(sppos)
print("""
host = data[atpos+1:sppos]
print(host)
Output:
""")
host = data[atpos+1:sppos]
print(host)
print('---------------------------------')









































