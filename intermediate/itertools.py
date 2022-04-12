# itertools: product, permutations, combinations, accumulate
# groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))

a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))

def smaller_than_3(x):
    return x < 3

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
{'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))


a = [1, 2, 3]
#for i in cycle(a): will cycle through a list until stop conditon
# is given
#    print(i)

for i in count(10):
    print(i)
    if i == 15:
        break

for i in repeat(1, 4):
    print(i)



