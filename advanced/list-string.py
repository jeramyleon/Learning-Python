print("""
BEST FRIENDS: STRINGS AND LISTS 

abc = 'With three words'
stuff = abc.split()
print(stuff)
Output:
""")
abc = 'With three words'
stuff = abc.split()
print(stuff)
print("""
print(len(stuff))
Output: 
""")
print(len(stuff))
print(""" 
print(stuff[0])
Output:
""")
print(stuff[0])
print("""
- When you do not specify a delimeter, multiple spaces are treated like
one delimiter
- You can specify what delimeter character to use in the splitting

line = 'A lot                        of spaces
etc = line.split()
print(etc)
Output:
""")
line = 'A lot                        of spaces'
etc = line.split()
print(etc)
print(""" 
line = 'first;second;third'
thing = line.split()
print(thing)
Output:
""")
line = 'first;second;third'
thing = line.split()
print(thing)
print(""" 
print(len(thing))
Output:
""")
print(len(thing))
print("""
thing = line.split(';')
print(thing)
Output:
""")
thing = line.split(';')
print(thing)
print("""
print(len(thing))
Output:
""")
print(len(thing))
print(""" 
Ex.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(word[2])

Output:
Sat
Fri
Fri
Fri

line = 'From stephen.marquaz@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)
Output:
""")
line = 'From stephen.marquaz@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)
print(""" 
-----------------------------------------------------------
THE DOUBLE SPLIT PATTERN

- Sometimes we split a line one way, and then grab one of the 
pieces of the line and split that piece again

From stephen.marquaz@uct.ac.za Sat Jan  5 09:14:16 2008

words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
Output:
""")
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
