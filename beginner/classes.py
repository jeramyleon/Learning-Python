# Types include:
# Numbers, strings, booleans
# Lists, dictionaries 
# These cannot always be used to represent complex things,
# we can use classes to model newer concepts 

class Point: # naming conventions for classes include
# capitalizing all words
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


# two line breaks after classes and functions is a good practice
point1 = Point()
point1.draw()
point1.x = 10 # classes can have attributes that we can set 
point1.y = 20 # anywhere 
print(point1.x)
print(point1.y)

point2 = Point()
point2.x = 1
print(point2.x)
