"""
- The difference between arguments and parameters
- Positional and keyword arguments 
- Default arguments
- Variable-length argumnets (*args and **kwargs)
- Container unpacking into function arguments 
- Local vs global arguments 
- Parameter passing (by value or by reference)
"""

def print_name(name): # name here is a parameter
    print(name)

print_name('Jeramy') # 'Jeramy' is an arguments given

def foo(a, b, c, d=4): # d is a default argument 
    print(a, b, c, d)

foo(1, 2, 3, 7) #  arguments 
foo(a=1, b=2, c=3) # keyword arguments, you can write in any order
# as you are specifying which is which
foo(1, b=2, c=3) # you can use both together but you can't use
# another positional argument after a keyword argument, you'll get 
# an error

def foo(a, b, *args, **kwargs): # args is a tuple and kwargs is a
# dictionary 
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)

def foo(a, b, *, c, d): 
    # every argument after the star must be a keyword argument
    print(a, b, c, d)

foo(1, 2, c=3, d=4)


def foo(*args, last): # last should be a keyword argument as 
    # args take any numbers of arguments 
    for arg in args:
        print(arg)
    print(last)
foo(1, 2, 3, last=100)


def foo(a, b, c):
    print(a, b, c)

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict) # this will unpack all elements in list to function
# works for tuples as well 
# use two stars for dictionaries and one star for lists and tuples
# for dictionaries keys must match parameter names or else you get 
# an error

def foo():
    global number
    number = 3
number = 0
foo()
print(number)


def foo(a_list):
    a_list = [200, 300, 400]
    a_list.append(4)
    a_list[0] = 100

my_list = [1, 2, 3]
foo(my_list)
print(my_list)










