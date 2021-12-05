# Iterators

my_list = [1,2,3,4,5,6,7,8,9]

# my_iter = iter(my_list)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(my_iter.__next__())

# for ele in my_list:
#     pass 


iter_obj = iter(my_list)

while True:
    try:
        ele = next(iter_obj)
        pass 
    except StopIteration:
        break

