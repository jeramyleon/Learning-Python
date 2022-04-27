print("""
FILE PROCESSING 

- A text file can be thought of as a sequence of lines 
- A textfile has newlines at the end of each line
---------------------------------------
OPENING A FILE

- Before we can read the contents of the file, we must tell Python
which file we are going to work with and what we will be doing with 
the file
- This is done with the open() function
- open() returns a 'file handle'- a variable used to perform 
operations on the file 
- Similar to "File -> Open" in a Word Processor 
-----------------------------------------
USING OPEN()

- handle = open(filename, mode) ---> ex. fhand = open('mbox.txt', 'r')
- returns a handle use to manipulate the file 
- filename is a string
- mode is optional and should be 'r' if we are planning to read the 
file and 'w' if we are going to write to the file. 
----------------------------------------------------
WHAT IS A HANDLE?

fhand = open('mbox.txt')
print(fhand)
Output:

<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>
-----------------------------------------------------
WHEN FILES ARE MISSING 

fhand = open('stuff.txt')
Output:

FileNotFoundError: No such file or directory: 'stuff.txt'
------------------------------------------------------
THE NEWLINE CHARACTER 

- We use a special character called "newline" to indicate when a line
ends
- We represent it as \n in strings
- Newline is still one - not two

stuff = 'Hello\nWorld'
print(stuff)
Output:
""")
stuff = 'Hello\nWorld'
print(stuff)
print("""
stuff = 'X\nY'
print(stuff)
Output:
""")
stuff = 'X\nY'
print(stuff)
print("""
print(len(stuff))
Output:
""")
print(len(stuff))
print('---------------------------------------')
print("""
FILE HANDLE AS A SEQUENCE 

- A file handle open for read can be treated as a sequence of 
strings where each line in the file is a string in the 
sequence 
- We can use the for statement to iterate through a sequence 
- Remember - a sequence is an ordered set 

Ex.
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
-------------------------------------------------------
COUNTING LINES IN A FILE

- Open a file read-only
- Use a for loop to read each line 
- Count the lines and print out the number of lines 

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
Output:

Line Count: 132045
--------------------------------------------------------------
READING THE *WHOLE* FILE

- We can read the whole file (newlines and all) into a single string

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
Output:

94626

print(inp[:20])
Output:

From stephen.marquar
-------------------------------------------------
SEARCHING THROUGH A FILE

- We can put an if statement in our for loop to only print lines
that meet some criteria
- We can strip the whitespace from the right-hand side of the string
using rstrip() from the string library
- The newline is considered "white space" and is stripped

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
Output:

From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zquian@umich.edu 
From: rjlowe@iupui.edu 
-------------------------------------------------------------
SKIPPING WITH CONTINUE

- We can conveniently skip a line using the continue statement

Ex. 
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
---------------------------------
USING IN TO SELECT LINES 

- We can look for a string anywhere in a line as our selection
criteria 

Ex. 
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue 
    print(line)
-------------------------------------------------------
PROMPT FOR FILE NAME

fname = input('Enter the filename: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
Output:

Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
------------------------------------------------------
BAD FILE NAMES 

fname = input('Enter the filename: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print('There were', count, 'subject lines in', frame)
Output:

Enter the file name: na na boo boo
File cannot be opened: na na boo boo
--------------------------------------------------------------
""")



