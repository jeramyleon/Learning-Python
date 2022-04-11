mydict = {
    "name": "Max", 
    "age": 28, 
    "city": "New York"
}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

value = mydict["name"]
print(value)

mydict["email"] = "max@xyz.com"
print(mydict)

mydict["email"] = "coolmax@xyz.com"
print(mydict) # you can overwrite variables in a dictionary

# del mydict["name"]
# print(mydict)
# mydict.pop("age")
# print(mydict)
# mydict.popitem()
# print(mydict)

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("error")

for key in mydict.keys(): 
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

mydict_cpy = mydict # this isn't a copy, rather it's a reference 
# to the variable so if we modify this, the original variable gets 
# modified
print(mydict_cpy)
mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)

mydict_cpy = mydict.copy() # proper way to make a seperate copy
mydict_cpy = dict(mydict) # another way to do so

my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Mary", age=27, city="Boston")
my_dict.update(my_dict_2)
print(my_dict)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)
value = my_dict[3]
print(value)

mytuple = (8, 7) # tuples can be keys in a dictionary, lists cannot
mydict = {mytuple: 15}
print(mydict)




