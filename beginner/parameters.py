def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

print("Start")
# greet_user() this would return an error because we need 
# argument to satisfy the first_name parameter
greet_user("John", "Smith")
greet_user("Mary", "Jane")
print("Finish")
