# Sets: unordered, mutable, no duplicates 
myset = {1, 2, 3, 1, 2}
print(myset)

myset = set("[1, 2, 3]")
print(myset)

myset = set("Hello")
print(myset)

myset = set()
print(type(myset))

myset.add(1)
myset.add(2)
myset.add(3)
myset.remove(3) # or .discard() which doesn't return error if element
# isn't found while .remove() does
# myset.clear() # clear set
print(myset.pop())
print(myset)

myset.add(1)
myset.add(2)
myset.add(3)
for i in myset:
    print(i)

if 1 in myset:
    print("yes")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
u = odds.union(evens) # combines elements from odds and evens 
# without duplication
print(u)

i = odds.intersection(primes) # looks for all similar numbers 
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setA.difference(setB) # returns all the numbers not in setB
diff = setB.symmetric_difference(setA) # returns all the numbers  
# from setA that are not in setB and vice versa
print(diff)

setA.update(setB)
print(setA)

setA.intersection_update(setB)
print(setA)

# setA.difference_update(setB)
# print(setA)

setA.symmetric_difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}
print(setA.issubset(setB))
print(setB.issuperset(setA))
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

setA = {1, 2, 3, 4, 5, 6}
setB = setA # this is a pointer to the setA variable, so any
# change done to setB will be done to setA
# setB.add(7)
# print(setB)
# print(setA)

setB = setA.copy()
setB.add(7)
print(setB)
print(setA)

a = frozenset([1, 2, 3, 4]) # cannot change it after it is created
# a.add(2) # will not work since a is immutable
# a.remove(1) # same here
print(a)