def greet_user(first_name, last_name):
    """
    first_name and last_name are positional arguments, therefore
    their position matters. 
    Example: 
    greet_user("jeramy", "leon") returns:
    Hi jeramy leon!
    Welcome aboard 
    
    greet_user("leon", "jeramy") returns:
    Hi leon jeramy!
    Welcome aboard
    """
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

print("Start")
greet_user(last_name="Smith", first_name="John") # using
# keyword arguments to define which name to assign to which
# paramaters 
# calc_cost(total=50, shipping=5, discount=0.1) keyword arguments 
# can improve the readibility of your code
# keyword arguments should be the same as paramater names 
print("Finish")



