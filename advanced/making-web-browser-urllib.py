print("""
-------------------------------------------------------------------
USING URLLIB IN PYTHON
- Since HTTP is so common, we have a library that does all the socket 
work for us and makes web pages look like a file 

>>> import urllib.request, urllib.parse, urllib.error
>>>
>>> fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
>>> for line in fhand:
>>>     print(line.decode().strip())
""")

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
print("""
----------------------------------------------------------------------
LIKE A FILE...

>>> import urllib.request, urllib.parse, urllib.eror
>>>
>>> fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
>>>
>>> counts = dict()
>>> for line in fhand:
>>>     words = line.decode().split()
>>>     for word in words:
>>>         counts[word] = counts.get(word, 0) + 1
>>> print(counts)
""")
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
print("""
----------------------------------------------------------------------
READING WEB PAGES

import urllib.request, urllib.parse, urllib.erro

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
""")
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
print(""" 
-----------------------------------------------------------------------

""")

