# Strings: ordered, immutable, text representation
my_string = "Hello World"
my_string = 'I\'m a programmer'
my_string = "I'm a programmer"
my_string = """Hello \
World"""
print(my_string)

my_string = "Hello World"
char = my_string[0]
print(char)

# my_string[0] = "h" # strings do not support item assignment
substring = my_string[1:5]
print(substring)
substring = my_string[::2] # takes every n character in string
print(substring)

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

for i in greeting:
    print(i)

if 'ell' in greeting:
    print('yes')
else:
    print('no')

my_string = '      Hello World     '
my_string = my_string.strip()
print(my_string)

my_string = 'Hello World'
print(my_string.upper())
print(my_string.startswith('H'))
print(my_string.endswith('World'))
print(my_string.find('o'))
print(my_string.count('o'))
print(my_string.replace('World', 'Universe'))

my_string = 'how are you doing'
my_list = my_string.split() # you can enter any parameter and it will
# split where n is found 
print(my_list)
new_string = ' '.join(my_list) # will join a list with the first
# part acting as the space between the elements when joined
print(new_string)

from timeit import default_timer as timer
my_list = ["a"] * 1000000
# below is bad code, avoid doing this 
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop-start)
# good code, this runs much faster
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop-start)


# %, .format(), f-strings
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 3
my_string = "the variable is %d" % var
print(my_string)

var = 3.1234567
my_string = "the variable is %.2f" % var # the .2f, the number 
# tells the computer how many decimal places you'd prefer
print(my_string)

var = 3.1234567
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2) 
# :.2f does the same as .2f above
print(my_string)

var = 3.1234567
var2 = 6
my_string = f"the variable is {var*2} and {var2}"
print(my_string)







