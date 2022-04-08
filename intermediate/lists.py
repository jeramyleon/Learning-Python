# lists: ordered, mutable, allows duplicate elements 
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple"]
print(mylist2)

item = mylist[0]
print(item)

item = mylist[-1]
print(item)

for x in mylist:
    print(x)

if "lemon" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist))

mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item = mylist.remove("cherry")
print(mylist)

mylist.reverse()
print(mylist)

item = mylist.sort()
print(mylist)

new_list = sorted(mylist)
print(mylist)
print(new_list)

mylist = [0] * 5
print(mylist)

mylist2 = [1, 2, 3, 4, 5]
new_list = mylist + mylist2
print(new_list)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a)

a = mylist[1::2]
print(a)

a = mylist[1::-1]
print(a)

list_org = ["banana", "cherry", "apple"]
list_cpy = list_org.copy() # or list(list_org) 
list_cpy.append("lemon")
print(list_cpy)
print(list_org)

mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]
print(mylist)
print(b)









