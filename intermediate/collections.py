# collections: Counter, namedtuple, OrderedDict, defaultdict,
# deque 
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict

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


d = defaultdict(int)
d['a'] = 1
d['b'] = 2



