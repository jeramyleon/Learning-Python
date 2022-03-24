class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point = Point(10, 20)
print(point.x)
point.x = 11
print(point.x)

# self is a reference to the current object

# Implementing it
class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
john.talk()
bob = Person("Bob Smith")
bob.talk()

