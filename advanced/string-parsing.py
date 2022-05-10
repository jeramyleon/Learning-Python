print("""
----------------------------------------------------------------------

STRING PARSING EXAMPLES 
- Extracting a host name - using find and string slicing 

>>> data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> atpos = data.find('@')
>>> print(atpos)
""")
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
print("""
>>> sppos = data.find(' ', atpos)
>>> print(sppos) 
""")
sppos = data.find(' ', atpos)
print(sppos)
print("""
>>> host = data[atpos+1 : sppos]
>>> print(host)
""")
host = data[atpos+1 : sppos]
print(host)
print("""
--------------------------------------------------------------------

THE DOUBLE SPLIT PATTERN
- Sometimes we split a line one way, and then grab one of the pieces of
the line and split that piece again

>>> line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> words = line.split()
>>> email = words[1]
>>> pieces = email.split('@')
>>> print(pieces[1])
""")
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
print("""
-------------------------------------------------------------------

THE REGEX VERSION

>>> import re 
>>> lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> y = re.findall('@([^ ]*)', lin)
>>> print(y)
""")
import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', lin)
print(y)
print("""
---------------------------------------------------------------------

EVEN COOLER REGEX VERSION

>>> import re 
>>> lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> y = re.findall('^From .*@([^ ]*)', lin)
>>> print(y)
""")
import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', lin)
print(y)
print("""
            '^From .*@([^ ]*)
^ Starting at the beginning of the line 
From look at the string 'From'
----------------------------------------------------------------------

ESCAPE CHARACTER 
- If you want a special regular expression character to just behave 
normally (most of the time) you prefix it with '\'

>>> import re 
>>> x = 'We just received $10.00 for cookies.'
>>> y = re.findall('\$[0-9.]+', x)
>>> print(y)
""")
import re 
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)
print("""

--------------------------------------------------------------------

SUMMARY
- Regular expressions are a cryptic but powerful language for matching
strings and extracting elements from those strings
- Regular expressions have special characters that indicate intent
""")









