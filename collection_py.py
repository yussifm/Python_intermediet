# collection: Counter, namedtuple, OrderDict, defaultdict, deque



from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque


a = "aaaaaabbbcccd"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(4))
print(my_counter.most_common(1)[0][0])
