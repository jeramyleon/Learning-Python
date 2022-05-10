print("""
---------------------------------------------
WHAT IS A COLLECTION? 
- A collection is nice because we can put more than one value in it 
and carry them all around in one convenient package 
- We have a bunch of values in a single 'variable'
- We do this by having more than one place "in" the variable 
- We have ways of finding the different places in the variable 
----------------------------------------------------
WHAT IS NOT A "COLLECTION"?
- Most of our variables have one value in them - when we put a new 
value in the variable - the old value is overwritten 

Ex:
x = 2
x = 4
print(x)
Output:

4
---------------------------------------------------------
A STORY OF TWO COLLECTIONS 
- List
    - A linear collection of values that stay in order 
- Dictionary
    - A "bag" of values, each with its own label 
----------------------------------------------------------
DICTIONARIES 
- Dictionaries are Python's most powerful data collection
- Dictionaries allow us to do fast database-like operations in Python
- Dictionaries have different names in different languages 
    - Associative Arrays - Perl/PHP
    - Properties or Map or HashMap - Java 
    - Property Bag - C# / .Net 
- Lists index their entries based on the position in the list 
- Dictionaries are like bags - no order 
- So we index the things we put in the dictionary with a "lookup tag:

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
Output:

{'money': 12, 'tissues': 75, 'candy': 3}

print(purse['candy'])
Output: 

3

purse['candy'] = purse['candy'] + 2
print(purse)
Output:

{'money': 12, 'tissues': 75, 'candy': 5}
--------------------------------------------------
COMPARING LISTS AND DICTIONARIES 
- Dictionaries are like lists except that they use keys instead of 
numbers to look up values 

>>> lst = list()                 >>> ddd = dict()
>>> lst.append(21)               >>> ddd['age'] = 21
>>> lst.append(183)              >>> ddd['course'] = 182
>>> print(lst)                   >>> print(ddd)
[21, 183]                        {'course': 182, 'age': 21}
>>> lst[0] = 23                  >>> ddd['age'] = 23
>>> print(lst)                   >>> print(ddd)
[23, 183]                        {'course': 182, 'age': 23}
--------------------------------------------------------------
DICTIONARY LITERALS(CONSTANTS)
- Dictionary literals use curly braces and have a list of key:value 
pairs 
- You can make an empty dictionary using empty curly braces 

>>> jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
>>> print(jjj)
{'jan': 100, 'chuck': 1, 'fred': 42}
>>> ooo = { }
>>> print(ooo)
{ }
---------------------------------------------------------------
MANY COUNTERS WITH A DICTIONARY 
- One common use of dictionaries is counting how often we "see"
something
>>> ccc = dict()
>>> ccc['csev'] = 1
>>> ccc['cwen'] = 1 
>>> print(ccc)
{'csev': 1, 'owen': 1}
>>> ccc['cwen'] = ccc['cwen'] + 1
>>> print(ccc)
{'csev': 1, 'cwen': 2}
----------------------------------------------------------------
DICTIONARY TRACEBACKS 
- It is an error to reference a key which is not in the dictionary
- We can use the in operator to see if a key is in the dictionary

>>> ccc = dict()
>>> print(ccc['csev'])
KeyError: 'csev'
>>> 'csev' in ccc
False
-----------------------------------------------------------------
WHEN WE SEE A NEW NAME 
- When we encounter a new name, we need to add a new entry in the 
dictionary and if this is the second or later time we have seen the 
name, we simply add one to the count in the dictionary under that name 

>>> counts = dict()
>>> names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
>>> for name in names:
>>>    if name not in counts:
>>>        counts[name] = 1
>>>    else:
>>>        counts[name] = counts[name] + 1
>>> print(counts)
""")
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
print("""
---------------------------------------------------------------
THE GET METHOD FOR DICTIONARIES 
- The pattern of checking to see if a key is already in a dictionary
and assuming a default value if the key is not there is so common
that there is a method called get() that does this for us 
- Default value if key does not exist (and no Traceback)

>>> if name in counts:
>>>    x = counts[name]
>>> else:
>>>    x = 0

>>> x = counts.get(name, 0)
{'csev': 2, 'zqian': 1, 'cwen': 2}
----------------------------------------------------------------
SIMPLIFIED COUNTING WITH GET()
- We can use get() and provide a default value of zero when the key
is not yet in the dictionary - and then just add one 

>>> counts = dict()
>>> names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
>>> for name in names:
>>>    counts[name] = counts.get(name, 0) + 1
>>> print(counts)
""")
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
print("""
---------------------------------------------------------------
COUNTING WORDS IN A TEXT 
---------------------------------------------------------------
COUNTING PATTERN
- The general pattrn to count the words in a line of text is to 
split the line into words, then loop through the words and use a 
dictionary to track the count of each word indepedently.

>>> counts = dict()
>>> print('Enter a line of text: ')
>>> line = input('')
 
>>> words = line.split()

>>> print('Words:', words)

>>> print('Counting....')
>>> for word in words:
>>>     counts[word] = counts.get(word, 0) + 1
>>> print('Counts', counts)
""")
counts = dict()
print('Enter a line of text: ')
line = input('')
 
words = line.split()

print('Words:', words)

print('Counting....')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)
print("""
-----------------------------------------------------------------
DEFINITE LOOPS AND DICTIONARIES 
- Even though dictionaries are not stored in order, we can write a for
loop that goes through all the entries in a dictionary - actually it 
goes through all of the keys in the dictionary and looks up the values 

>>> counts = {'chuck': 1, 'fred': 42, 'jan': 100}
>>> for key in counts:
>>>     print(key, counts[key])
""")
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])
print("""
--------------------------------------------------------------------
RETRIEVING LISTS OF KEYS AND VALUES 
- You can get a list of keys, valyes or items (both) from a dictionary

>>> jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
>>> print(list(jjj))
['jan', 'chuck', fred]
>>> print(jjj.keys())
['jan', 'chuck', 'fred']
>>> print(jjj.values())
[100, 1, 42]
>>> print(jjj.items())
[('jan', 100), ('chuck', 1), ('fred', 42)]
-------------------------------------------------------------------
BONUS: TWO ITERATION VARIABLE!
- We loop through the key-value pairs in a dictionary using *two*
iteration variables 
- Each iteration, the first variable is the key and the second variable 
is the corresponding value for the key

>>> jjj = {'chuck': 1, 'fred': 41, 'jan': 100}
>>> for aaa, bbb in jjj.items():
>>>     print(aaa, bbb)
""")
jjj = {'chuck': 1, 'fred': 41, 'jan': 100}
for aaa, bbb in jjj.items():
    print(aaa, bbb)
print("""
>>> name = input('Enter file: ')
>>> handle = open(name)

>>> counts = dict()
>>> for line in handle:
>>>     words = line.split()
>>>     for word in words:
>>>         counts[word] = counts.get(word, 0) + 1 

>>> bigcount = None 
>>> bigword = None 
>>> for word, count in counts.items():
>>>     if bigcount is None or counts > bigcount:
>>>         bigword = word 
>>>         bigcount = count 
>>> print(bigword, bigcount)

""")
name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 

bigcount = None 
bigword = None 
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word 
        bigcount = count 
print(bigword, bigcount)
