customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True 
}
# Each key is unique, therefore we can't repeat key names.
print(customer["name"])
# print(customer["Name"]) this will return error as we 
# capitalized the n and that key isn't in the dictionary
print(customer.get("name"))
print(customer.get("birthdate")) # getting a dictionary that
# doesn't exist returns None
print(customer.get("birthdate", "Jan 1 1980")) # second par
# is a default value this line will return if the "birthday"
# key returns None
customer["name"] = "Jack Smith" # we can reassign key values 
print(customer["name"])
customer["birthdate"] = "Jan 1 1980" # adding new key value pair 
print(customer["birthdate"])

# Program to return phone numbers as words 
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for char in phone:
    output += digits_mapping.get(char, "!") + " "
print(output)
   


