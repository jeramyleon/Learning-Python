print("""
COUNTING IN A LOOP

- To count how many times we execute a loop, we introduce a counter 
variable that starts at 0 and we add one to it each time through the loop.

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)
Output:
""")
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)
print('----------------------')

print("""
SUMMING IN A LOOP

- To add up a value we encounter in a loop, we introduce a sum variable 
that starts at 0 and we add the value to the sum each time through the 
loop

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)
Output:
""")
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)
print('-------------------------')

print("""
FINDING THE AVERAGE IN A LOOP

- An average just combines the counting and sum patterns and divides when
the loop is done.

count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value 
    print(count, sum, value)
print('After', count, sum, sum/count)
Output:
""")
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value 
    print(count, sum, value)
print('After', count, sum, sum/count)
print('------------------------')

print("""
SEARCH USING A BOOLEAN VARIABLE 

- If we just want to search and know if a value was found, we use a 
variable that starts at False and is set to True as soon as we find what
we are looking for.

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)
Output:
""")
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)
print('-----------------------------')

print("""
FINDING THE SMALLEST VALUE 

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value 
    elif value < smallest:
        smallest = value 
    print(smallest, value)
print('After', smallest)
""")
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value 
    elif value < smallest:
        smallest = value 
    print(smallest, value)
print('After', smallest)
print('--------------------------')

print("""
THE "IS" AND "IS NOT" OPERATORS 

- Python has an is operator that can be used in logical expressions
- Implies "is the same as"
- Similar to, but stronger than ==
- is not also is a logical operator
""")






