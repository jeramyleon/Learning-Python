"""
*SENTENCES OR LINES*
x = 2 <-- Assignment statement
x = x + 2 <-- Assignment with expression
print(x) <-- Print statement


*ASSIGNMENT STATEMENTS*
- We assing a value to a variable using the assignment statement (=)
- An assignment statemenr consists of an expression on the right-hand 
side and a variable to store the result 
- A variable is a memory location used to store a value. The value stored
can be updated by replacing the old value with a new value 


*EXPRESSIONS*
- Because of the lack of mathematical symbols on computer keyboard-
we use "computer-speak" to express the classic math operations
- Asterisk is multiplication
- Exponentiation (raise to a power) looks different than in math
Operator       Operation
    +           Addition
    -           Subtraction
    *           Multiplication
    /           Division
    **          Power
    %           Remainder

>>> xx = 2          
>>> xx = xx + 2
>>> print(xx) 
4

>>> yy = 440 * 12
>>> print(yy)
5280

>>> zz = yy / 100
>>> print(zz)
5.28

>>> jj = 23
>>> kk = jj % 5
>>> print(kk)
3

>>> print(4 ** 3)
64


*ORDER OF EVALUATION*
- When we string together operators together - Python must know which
one to do first 
- This is called "operator precedence"
- Which operator "takes precedence" over the others?
x = 1 + 2 * 3 - 4 / 5 ** 6

*OPERATOR PRECEDENCE RULES*
- Highest precedence rule to lowest precedence rule:
    - Parentheses are always respected
    - Exponentiation (raise to a power)
    - Multiplication, Division and Remainder
    - Addition and Subtraction
    - Left to right

>>> x = 1 + 2 ** 3 / 4 * 5 
>>> print(x)
11.0
1 + 2 ** 3 / 4 * 5
       \
    1 + 8 / 4 * 5
          \
       1 + 2 * 5
            /
       1 + 10
          \
          11


*TYPE MATTERS*
- Python knows what 'type' everything is
- Some operations are prohibited
- You cannot "add 1" to a string 
- We can ask Python what type something is by using the type()
function
eee = 'hello ' + 'there
eee = eee + 1 returns error 
type(eee) returns <class'str'>
type('hello') returns <class'str'>
type(1) returns <class'int'>

Several types of numbers 
- Numbers have two main types
    - Integers are whole numbers: -14, -2, 0, 1, 100, 401233
    - Floating Point Numbers have decimal parts: -2.5, 0.0, 98.6
    14.0
- There are other number types - they are variations on float and integer
>>> xx = 1
>>> type(xx)
<class'int'>
>>> temp = 98.6
>>> type(temp)
<class'float'>
>>> type(1)
<class'int'>
>>> type(1.0)
<class'float'>

*TYPE CONVERSIONS* 
- When you put an integer and floating point in an expression, the 
integer is implicitly converted to a float 
- You can control this with the built-in functions int() and float()
>>> print(float(99) + 100)
199.0
>>> i = 42 
>>> type(i)
<class'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<class'float'>

*INTEGER DIVISION*
- Integer division produces a floating point result
- This was different in Python2.x
>>> print(10 / 2)
5.0
>>> print(9 / 2)
4.5
>>> print(99 / 100)
0.99
>>> print(10.0 / 2.0)
5.0
>>> print(99.0 / 100.0)
0.99






"""

