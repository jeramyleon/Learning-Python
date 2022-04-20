# * * * * *
result = 5 * 7 # multiplication
print(result)

result = 2 ** 4 # exponentiation
print(result)

zeros = [0] * 10 # creates list with 10 0 elements
print(zeros)

zeros = "AB" * 10 # creates string with 10 AB strings together
print(zeros)

def foo(a, b, *args, **kwargs):
    print(a)
    for arg in args:
        print(arg)
    
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)

def foo(a, b, *, c): # parameters after  * sign must be kwargs 
    print(a, b, c)
foo(1, 2, c=3)
# ------------------------------

def foo(a, b, c):
    print(a, b, c)
my_list = [0, 1, 2]
foo(*my_list) # works for both tuples and lists

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict) # does the same, use double stars for dictionaries
# note: dictionary key names must match parameter names 
#------------------------------------

numbers = [1, 2, 3, 4, 5, 6]
*beginning, last = numbers # unpacks all numbers not including the last
# last elemen is assinged to 
beginning, *middle, last = numbers # unpacks only numbers in between
# first and last elements without including them
print(beginning)
print(middle)
print(last)
#---------------------------------
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]

new_list = [*my_tuple, *my_list]
print(new_list)

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)
