mytuple = ("Max", 28, "Boston") # you can leave out parentheses and
# it'll still be a tuple
mytuple = ("Max",) # do this if you want a tuple with one element,
# python recognizes only one element with no comma as whatever type
# the element is 
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

item = mytuple[0]
print(item)

# mytuple[0] = "Tin" # This won't work because a tuple is immutable

for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("yes")
else:
    print("no")

my_tuple = ["a", "p", "p", "l", "e"]
print(len(my_tuple))
print(my_tuple.count('p')) # number of occurences 
print(my_tuple.index('p')) # returns index of first occurence of 
# value given

my_list = list(my_tuple)
print(my_list)
my_tuple2 = tuple(my_list)
print(my_tuple2)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
b = a[::2] # every other element 
print(b)
b = a[::-1] # reverses list
print(b)

my_tuple = "Max", 28, "Boston"
name, age, city = my_tuple # num of vars must match num
# of values in tuple for this to work.
print(name)
print(age)
print(city)

my_tuple = [0, 1, 2, 3, 4]
i1, *i2, i3 = my_tuple 
print(i1)
print(i3)
print(i2)

import sys
my_list  = [0, 1, 2, 'hello', True]
my_tuple = (0, 1, 2, 'hello', True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")
# a list is larger than a tuple even with the same elements 
# tuples are more efficient for certain tasks

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
# takes much longer to create a list than it takes to create 
# a tuple 
# tuples are usually more efficient 







