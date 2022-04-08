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
