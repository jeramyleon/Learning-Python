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


def foo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
foo(*my_list)
