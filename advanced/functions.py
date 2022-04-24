print('*Stored (and reused) Steps*')
print('*code')
def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()
print('code*')
print('------------')

print('*Python Functions*')
print("""
- There are two kinds of functions in Python.
    - Built-in functions that are provided as part of Python - print(),
    input(), type(), float(), int()...
    - Functions that we define ourselves and then use 
- We treat the built-in function names as 'new' reserved words (i.e., we
avoid them as variable names)
""")
print('-------------')

print('*Function Definition*')
print("""
- In Python a function is some reusable code that takes argument(s) as 
input, does some computation, and then returns a result or results
- We define a function using the def reserved word 
- We call/invoke the function by using the function name, parentheses, and
arguments in an expression
""")
print('*code')
big = max('Hello world')
print(big)
tiny = min('Hello world')
print(tiny)
print('code*')
print('----------')

print('*Max Function*')
print("""
- A function is some stored code that we use. A function takes some 
input and produces an output.

                         -------------------------
                         | def max(inp):         |
                         |     blah blah         |
'Hello world'----------> |     for x in y:       |-------> 'w'
(a string)               |         blah blah     |          (a string)
                         -------------------------
""")
print('-------------')

print('*Type conversions*')
print("""
- When you put an integer and floating point in an expression, the integer
is implicitly converted to a float 
- You can control this with the built-in functions int() and float()
""")
print('----------')

print('*String Conversions*')
print("""
- You can also use int() and float() to convert between strings and 
integers
- You will get an error if the string does not contain numeric
characters 
""")
print('----------')

print('*Building our Own Functions*')
print("""
- We create new functions using the def keyword followed by optional
parameters in parentheses
- We indent the body of the function
- This defines the function but does not execute the body of the 
function

def print_lyrics():
    print("I'm a lumberjackm and I'm okay.")
    print('I sleep all night and I work all day.')
""")

print('----------')


print('*Definitions and Uses*')
print("""
- Once we have defined a function, we can call (or invoke) it as many 
times as we like
-This is the store and reuse pattern 
""")
print('*code')
x = 5 
print('Hello')

def print_lyrics():
    print("I'm a lumberjack and I'm okay.")
    print("I sleep all night and I work all day.")

print('Yo')
print_lyrics()
x = x + 2
print(x)
print('code*')
print('----------')


print("""
ARGUMENTS 
- An argument is a value we pass into the function as its input 
when we call the function
- We use arguments so we can direct the function to do different kinds
of work when we call it at different times 
- We put the arguments in parentheses after the name of the function

big = max('Hello world')
                |
                ------- Argument 
""")
print('----------')


print("""
PARAMETERS 
- A parameter is a variable which we use in the function definition.
It is a "handle" that allows the code in the function to access the 
arguments for a particular function invocation 
""")
print('----------')

print("""
""")
print('----------')


