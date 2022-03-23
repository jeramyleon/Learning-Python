temperature = 35
# > greater than
# < less than
# == equal to
# != not equal to

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "John Smith"

if len(name) < 3:
    print("Name must be at lesst 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")
   