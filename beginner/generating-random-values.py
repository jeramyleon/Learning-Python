import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return first, second # this automatically returns both 
        # numbers as a tuple.
# add two line breaks 

dice = Dice()
print(dice.roll())





