print(""" 
-------------------------------------------------------------------

MATCHING AND EXTRACTING DATA 
- re.search() returns a True/False depending on whether the string matches
the regular expression
- If we actually want the matching strings to be extracted, we use
re.findall()

                   [0-9]+
[0-9]+ One or more digits 

>>> import re
>>> x = 'My 2 favorite numbers are 19 and 42'
>>> y = re.findall('[0-9]+', x)
>>> print(y)
""")
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
print("""
- When we use re.findall(), it returns a list of zero or more sub-strings
that match the regular expression

>>> y = re.findall('[AEIOU]+, x')
>>> print(y)
""")
y = re.findall('[AEIOU]+', x)
print(y)
print("""
----------------------------------------------------------------------

WARNING: GREEDY MATCHING
- The repeat characters (* and +) push outward in both directions (greedy)
to match the largest possible string 

                ^F.+:
^F first character in the match is an F
.+ one or more characters 
: last character in the match is a ':'

>>> import re 
>>> x = 'From: Using the : character'
>>> y = re.findall('^F.+:', x)
>>> print(y)
""")
import re 
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
print("""
--------------------------------------------------------------------

NON-GREEDY MATCHING 
- Not all regular expression repeat codes are greedy! If you add a ?
character, the + and * chill out a bit.
            ^F.+?:
^F  First character in the match is an F 
.+? One or more characters but not greedy
: Last character in the match is a :
---------------------------------------------------------------------

FINE-TUNING STRING EXTRACTION
- You can refine the match for re.findall() and seperately determine 
which portion of the match is to be extracted by using parentheses

>>> x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> y = re.findall('\S+@\S+', x)
>>> print(y)
""")
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)
print("""
                \S+@\S+
\S At least one non-whitespace character 

- Parentheses are not part of the match - but they tell where to start
and stop what string to extract 

>>> y = re.findall('^From (\S+@\S+)', x)
>>> print(y)
""")
y = re.findall('^From (\S+@\S+)', x)
print(y)












