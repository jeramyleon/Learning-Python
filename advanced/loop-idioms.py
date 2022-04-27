print("""
LOOP IDIOMS: WHAT WE DO IN LOOPS
Note: Even though these examples are simple, the patterns apply to all
kinds of loops
---------------------------------------------------

MAKING "SMART" LOOPS
- The trick is "knowing" something about the whole loops when you are 
stuck writing code that only sees one entry at a time 

Set some variables to initial values 
for thing in data:
    Look for something or do something to each entry seperately,
    updating a variable 
Look at the variables 
---------------------------------------------------------
LOOPING THROUGH A SET 

print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')
Output: 
""")
print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')
print('---------------------------------------------')


print("""
FINDING THE LARGEST VALUE

- We make a variable that contains the largest value we have seen so far.
If the current number we are looking at is larger, it is the new largest
value we have seen so far.

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

Output:

""")
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)
print('-----------------------------------')


