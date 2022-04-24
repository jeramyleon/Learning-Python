print('*CONDITIONAL STEPS*') 
# Program: 
x = 5 
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finish')
# Output: 
# Smaller 
# Finish
 
"""
x = 5
  |
x < 10 ?-------Yes 
  |             |
  |             print('Smaller')
  |             |
  |--------------
x > 20 ?--------
    |           |
No  |           print('Biggger')
    |           |
    |------------
print('Finish')
"""


"""
*COMPARISON OPERATORS*
- Boolean expressions ask a question and produce a Yes or No result
which we use to control program flow 
- Boolean expressions using comparison evaluate to True/False or Yes/No
- Comparison operators look at variables but do not change the variables

Python      Meaning 
<           Less than
<=          Less than or Equal to
==          Equal to ? 
>=          Greater than or Equal to
>           Greater than
!=          Not equal
Remember: '=' is used for assignment 
"""
print('*COMPARISON OPERATORS*')
x = 5 
if x == 5:
    print('Equals 5')
if x > 4:
    print('Greater than 4')
if x >= 5:
    print('Greater than or Equals 5')
if x < 6: print('Less than 6')
if x <= 5:
    print('Less than or equals 5')
if x != 6:
    print('Not equal 6')

print("*One-Way Decision*")
x = 5
print('Before 5')
if x == 5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6:
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')



print('*Indentation*')
print("""
- Increase indent indent after an if statement or for statement
(after: )
- Maintain indent to indicate the scope of the block (which lines are
affected by the it/for)
- Reduce indent back to the level of the if statement or for statement 
to indicate the end of the block
- Blank lines are ignored - they do not affect indentation
- Comments on a line by themselves are igored with regard to 
indentation.
""")

print("*Nested Decisions*")
print('code')
x = 42 
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All done')
print('-----')

print('*Two-way decisions*')
print("""
- Sometimes we want to do one thing if a logical expressions is true and
something else if the expressions is false 
- It is like a fork in the road - we must choose oen or the other path
but not both
""")
print('----------')

print('*Two-way decisions with else:*')
print('*code')
x = 4 
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All Done')
print('----------')

print('*Multi-way*')
print('*code')
# No else 
x = 5
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
print('All Done')

if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
elif x < 20:
    print('Big')
elif x < 40:
    print('Large')
elif x < 100:
    print('Huge')
else:
    print('Ginormous')
print('-----')

print('*The try / except structure*')
print("""
- You surround a dangerous section of code with try and except 
- If the code in the try works - the except is skipped
- If the code in the try fails - it jumps to the except section
""")
print('*code')
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1 
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)  
print("-------")

print('*Sample try/except*')
print('*code')
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work')
else:
    print('Not a number')
print('---------')





