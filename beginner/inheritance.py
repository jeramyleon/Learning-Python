class Mammal:
    def walk(self):
        print("walk")
# Always use two line breaks after defining classes or functions

class Dog(Mammal): # This is how you inherit from another class
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")
# DRY, Don't repeat yourself, if many classes have identical
# functions, inherit from those classes.
dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.be_annoying()

