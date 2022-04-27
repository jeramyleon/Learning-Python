print("""
REPEATED STEPS
- Loops(repeated steps) have iteration variables that change each time 
through a loop. Often these iteration variables go through a sequence of 
numbers 

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
print(n)

Output
""")
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
print(n)
print('-----------------------------------')

print("""
AN INFINITE LOOP
n = 5 
while n > 0:
    print('Lather')
    print('Rinse')
print('Dry off!')

Ths loop will run an infinite amount of teams because n doesn't change
and n will always be evaluated as greater than 0 since it's 5

-------------------------------------------------------------
ANOTHER LOOP
n = 0
while n > 0:
    print('Lather')
    print('Rinse')
print('Dry off!')

This loop doesn't run because n is not greater than 0 so the program just 
skips the loop. The idea is called Zero-trip, where it's not guarenteed 
to even run once.
------------------------------------------------------------

BREAKING OUT OF A LOOP
- The break statement ends the current loop and jumps to the statement
immediately following the loop
- It is like a loop test that can happen anywhere in the body of the 
loop.

while True:
    line = input('> ')
    if line == 'done':
        break 
    print(line)
print('Done!')
Output
""")
while True:
    line = input('> ')
    if line == 'done':
        break 
    print(line)
print('Done!')
print('---------------------------------')

print("""
FINISHING AN ITERATION WITH CONTINUE
- The continue statement ends the current iteration and jumps to the 
top of the loop and starts the next iteration

while True:
    line = input('> ')
    if line[0] == '#':
        continue 
    if line == 'done':
        break 
    print(line)
print('Done!')
Output 
""")
while True:
    line = input('> ')
    if line[0] == '#':
        continue 
    if line == 'done':
        break 
    print(line)
print('Done!')
print('--------------------------------------')

print("""
INDEFINITE LOOPS
- While loops are called "indefinite loops" because they keep going 
until a logical conditon becomes False 
- The loops we have seen so far are pretty easy to examine to see if they
will terminate or if they will be "infinite loops"
- Sometimes it is a little harder to be sure if a loop will terminate 
------------------------------------------------------------
""")





