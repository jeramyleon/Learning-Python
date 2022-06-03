print("""
--------------------------------------------------------------------------
WARNING 
- This lecture is very much about definitions and mechanics for objects 
- This lecture is a lot more about "how it works" and less about "how you 
use it"
- You won't get the entire picture until this is all looked at in context 
of a real problem
- So please suspend disbelief and learn technique for the next 50 or so 
slides
------------------------------------------------------------------------
OBJECT ORIENTED 
- A program is made up of many cooperating objects 
- Instead of being the "whole program" - each object is a little "island"
within the program and cooperatively working with other objects 
- A program is made up of one or more objects working together - objects 
make us of each other's capabilities 
----------------------------------------------------------------------
OBJECT 
- An object is a bit of self-contained Code and Data
- A key aspect of the Object approach is to break the problem into smaller 
understandable parts (divide and conquer)
- Objects have boundaries that allow us to ignore un-needed detail
- We have been using objects all along: String Objects, Integer Objects,
Dictionary Objects, List Objects...
------------------------------------------------------------------------
DEFINITIONS 
- Class - a template - Dog
- Method or Massage - A defined capability of a class - bark()
- Field or attribute - A bit of data in a class - length
- Object or Instance - A particular instance of a class - Lassie 
--------------------------------------------------------------------------
TERMINOLOGY: CLASS
- A pattern(exemplar) of a class. The class of Dog defines all possible dogs
by listing the characteristics and behaviors they can have; the object Lassie
is one particular dog, with particular versions of the characteristics. A
Dog has fur; Lassie has brown-and-white fur.
---------------------------------------------------------------------------
TERMINOLOGY: INSTANCE 
- One can have an instance of a class or a particular object. The instance 
is the actual object created at runtime. In programmer jargon, the Lassie 
object is an instance of the Dog class. The set of values of the attributes 
of a particular object is called its state. The object consists of state and
the behavior that's defined in the object's class. 
--------------------------------------------------------------------------
TERMINOLOGY: METHOD 
- An object's abilities. In language, methods are verbs. Lassie, being a Dog,
has the ability to bark. So bark() is one of Lassie's methods. She may have 
other methods as well, for example sit() or eat() or walk() or save_timmy(). 
Within the program, using a method usually affects only one particular object;
all Dogs can bark, but you need only one particular dog to do the barking
- Method and Message are often used interchangeably.
--------------------------------------------------------------------------
A SAMPLE CLASS 

>>> class PartyAnimal:
>>>     x = 0
>>>
>>>     def party(self):
>>>         self.x = self.x + 1
>>>         print("So far", self.x)
>>>    
>>> an = PartyAnimal()
>>> an.party()
>>> an.party()
>>> an.party()
Output: 
""")
class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
print("""
----------------------------------------------------------------------
A NERDY WAY TO FIND CAPABILITIES
>>> x = list()
>>> print(type(x))
Output: 
""")
x = list()
print(type(x))
print("""
>>> print(dir(x)) 
Output:
""")
print(dir(x))
print("""
- The dir() command lists capabilities
- Ignore the ones with underscores, those are used by Python itself 
- The rest are real operations that the object can perform
- It is like type()- it tells us something "about" a variable
------------------------------------------------------------------------- 
OBJECT LIFECYCLE 
- Objects are created, used and discarded
- We have special blocks of code (methods) that get called 
    - At the moment of creation(constructor)
    - At the moment of destruction(destructor)
- Constructors are used a lot 
- Destructors are seldom used
-----------------------------------------------------------------------
CONSTRUCTOR 
- The primary purpose of the constructor is to set up some instance 
variables to have the proper initial values when the object is created 

>>> class PartyAnimal:
>>>     x = 0
>>> 
>>>     def __init__(self):
>>>         print('I am constructed')
>>>    
>>>     def party(self):
>>>         self.x = self.x + 1 
>>>         print('So far', self.x)
>>>     
>>>     def __del__(self):
>>>         print('I am destructed', self.x)
>>>
>>> an = PartyAnimal()
>>> an.party()
>>> an.party()
>>> an = 42 
>>> print('an contains', an)
Output: 
""")
class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')
    
    def party(self):
        self.x = self.x + 1 
        print('So far', self.x)
    
    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42 
print('an contains', an)
print("""
- The constructor and destructor are optional. The constructor is typically 
used to set up variables. The destructor is seldom used. 
- In object oriented programming, a constructor in a class is a special block
of statements called when an object is created 
-------------------------------------------------------------------------
MANY INSTANCES 
- We can create lots of objects - the class is the template for the object 
- We can store each distinct object in its own variable 
- We call this having multiple instances of the same class 
- Each instance has its own copy of the instance variables 

>>> class PartyAnimal:
>>>     x = 0
>>>     name = ""
>>>     def __init__(self, z):
>>>         self.name = z
>>>         print(self.name, "constructed")
>>>
>>>     def party(self):
>>>         self.x = self.x + 1 
>>>         print(self.name, "party count", self.x)
>>>    
>>> s = PartyAnimal("Sally")
>>> s.party()
>>> 
>>> j = PartyAnimal('Jim')
>>> j.party()
>>> s.party()
Output:
""")
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1 
        print(self.name, "party count", self.x)
    
s = PartyAnimal("Sally")
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()
print("""
- Constructors can have additional paramaters. These can be used to set up
instance variables for the particular instance of the class (i.e., for the 
particular object)
-------------------------------------------------------------------------
INHERITANCE 
- When we make a new class - we can reuse an existing class and inherit 
all the capabilities of an existing class and then add our own little bit to
make our new class
- Another form of store and reuse 
- Write once - reuse many times 
- The new class (child) has all the capabilities of the old class (parent) -
and then some more 
---------------------------------------------------------------------------
TERMINOLOGY: INHERITANCE 
- 'Subclasses' are more specialized versions of a class, which inherit 
attributes and behaviors from their parent classes, and can introduce 
their own

>>> class PartyAnimal:
>>>     x = 0
>>>     name = ""
>>>     def __init__(self, nam):
>>>         self.name = nam
>>>         print(self.name, "constructed")
>>>     
>>>     def party(self):
>>>         self.x = self.x + 1
>>>         print(self.name, "party count", self.x)
>>>
>>> class FootballFan(PartyAnimal):
>>>     points = 0
>>>     def touchdown(self):
>>>         self.points = self.points + 7
>>>         self.party()
>>>         print(self.name, "points", self.points)
>>>
>>> s = PartyAnimal('Sally')
>>> s.party()
>>>
>>> j = FootballFan('Jim')
>>> j.party()
>>> j.touchdown()
Outputs:
""")
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")
    
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()
print("""
FootballFan is a class which extends PartyAnimal. It has all the capabilities
of PartyAnimal and more. 
-----------------------------------------------------------------------
DEFINITIONS
- Class: a template 
- Attribute: A variable within a class
- Method: A function within a class
- Object: A particular instance of a class
- Constructor: Code that runs when an object is created
- Inheritance: The ability to extend a class to make a new class.
------------------------------------------------------------------
SUMMARY
- Object Oriented programming is a very structured approach to code reuse.
- We can group data and functionality together and create many independent
instances of a class
""")




































































