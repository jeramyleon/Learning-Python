# collections: Counter, namedtuple, OrderedDict, defaultdict,
# deque 
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaaaabbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2)[0][0])
print(list(my_counter.elements()))


Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)
print(pt.x)
print(pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)


d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d)
print(d['a'])
print(d['b'])
print(d['c'])


d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d.extend([4, 5, 6])
print(d)

d.extendleft([4, 5, 6])
print(d)

d.rotate(2)
print(d)




