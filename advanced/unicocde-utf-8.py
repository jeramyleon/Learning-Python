print("""
--------------------------------------------------------------------
REPRESENTING SIMPLE STRINGS 
- Each character is represented by a number between 0 and 256 stored 
in 8 bits of memory 
- We refer to 8 bits of memory as a "byte" of memory --(i.e my disk drive
contains 3 terabytes of memory)
- The ord() function tells us the numeric value of a simple ASCII 
character 

>>> print(ord('H'))
""")
print(ord('H'))
print("""
>>> print(ord('e'))
""")
print(ord('e'))
print("""
---------------------------------------------------------------------
MULTI-BYTE CHARACTERS
- To represent the wide range of characters computers must handle we 
represent characters with more than one byte
    - UTF-16 - Fixed length - Two bytes
    - UTF-32 - Fixed length - Four bytes
    - UTF-8 - 1-4 bytes
        - Upwards compatible with ASCII
        - Automatic detection between ASCII and UTF-8
        - UTF-8 is recommended practice for encoding data to be
        exchanged between systems 
---------------------------------------------------------------------
PYTHON3 AND UNICODE
- In Python 3, all strings internally are UNICODE
- Working with string variables in Python programs and reading data 
from files usually 'just works'
- When we talk to a network resource using sockets or talk to a database
we have to encode and decode data (usually to UTF-8)
----------------------------------------------------------------------
PYTHON STRINGS TO BYTES
- When we talk to an external resource like a network socket we sends 
bytes, so we need to encode Python 3 strings into a given character 
encoding 
- When we read data from an external resource, we must decode it based 
on the character set so it is properly represented in Python 3 as a string

>>> while True:
>>>     data = mysock.recv(512)
>>>     if (len(data) < 1):
>>>         break 
>>>     mystring = data.decode()
>>>     print(mystring)
----------------------------------------------------------------------
AN HTTP REQUEST IN PYTHON

>>> import socket 
>>> mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> mysock.connect(('data.pr4e.org', 80))
>>> cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
>>> mysock.send(cmd)
>>> 
>>> while True: 
>>>     data = mysock.recv(512)
>>>     if (len(data) < 1):
>>>         break
>>>     print(data.decode())
>>> mysock.close()

""")









