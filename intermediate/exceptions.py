# Errors and Exceptions
x = 5
if x < 0:
    # raise Exception('x should be positive')
    pass

assert(x>=0), 'x is not positive'

# it's good to know the errors you want to catch
try:
    a = 5 / 0
    b = a + + 4
except ZeroDivisionError as e: # except runs when a specific error is
    # thrown
    print(e)
except TypeError as e:
    print(e)
else: # else runs if no errors came up
    print("everything is fine")
finally: # this always runs no matter what
    print('cleaning up')


# making our own errors
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message 
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)
# test_value(200)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)



    




