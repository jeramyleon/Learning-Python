print("""
DEFINITE LOOPS
- Quite often we have a list of items of the lines in a file -
effectively a finite set of things 
- We can write a loop to run the loop once for each of the items in 
a set using the python for construct 
- These loops are called "definite loops" because they execute an exact 
number of times 
- We say that "definite loops iterate through the members of a set"
-----------------------------------------------------------------------
A SIMPLE DEFINITE LOOP

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')
Output
""")
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')
print('---------------------------------------')

print("""
A DEFINITE LOOP WITH STRINGS 

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
Output
""")
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
print('-------------------------')

print("""
A SIMPLE DEFINITE LOOP
- Definite loops (for loops) have explicit iteration variables that change
each time through a loop. These iteration variables move through the 
sequence or set

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')
Output
""")
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')
print('----------------------------')

print("""
LOOKING AT IN....
- The iteration variable iterates through the sequence(ordered set)
- The block(body) of code is executed once for each value in the 
sequence
- The iteration variable moves through all of the values in the 
sequence 

i is the iteration variable 
the list is a five-element sequence 

for i in [5, 4, 3, 2, 1]:
    print(i)
Output
""")
for i in [5, 4, 3, 2, 1]:
    print(i)
print('-----------------------------------')

