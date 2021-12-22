# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators(count, cycle, repeat, )
from itertools import product, repeat
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
import operator
from itertools import groupby
from itertools import count, cycle, repeat



a = [1,2, 3, 4, 5]
b=[3,4]
prod = product(a,b, repeat=2)
# print(list(prod))

perm = permutations(a,2)
# print(list(perm))

comb = combinations(a, 2)
# print(list(comb))

comb2 = combinations_with_replacement(a,2)
# print(list(comb2))

acc = accumulate(a)
accop = accumulate(a, func=operator.mul)
accma = accumulate(a, func=max)
# print(a)
# print(list(acc))
# print(list(accop))
# print(list(accma))

# def smaller_than_3(x):
#     return x < 3
persons = [
    {'name': "Kojo", 'age': 23},
    {'name': "AMa", 'age': 20},
    {'name': "Hamida", 'age': 20},
    {'name': "Jonior", 'age': 12},
    {'name': "Coded", 'age': 24},
    {'name': "Mohammed", 'age': 13},
    {'name': "Ayisha", 'age': 28},
    {'name': "Elder", 'age': 30},
    {'name': "Ali", 'age': 30},
    {'name': "Nimatu", 'age': 30},
]

groub_obj = groupby(a, key=(lambda x: x< 3))
for key, value in groub_obj:
    pass
    # print(key, list(value))

groub_obj = groupby(persons, key=(lambda x: x['age']))
for key, value in groub_obj:
    pass
    # print(key, list(value))


