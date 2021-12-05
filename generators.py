# Generators

# def my_generator():
#     n=1
#     print("THis is first iteration")
#     yield n

#     n +=1
#     print("this is the second iteration")
#     yield n

#     n +=1
#     print("this is the final iteration")
#     yield n


# a = my_generator()
# print(next(a))
# print(next(a))


# def rev_str(str_toRev):
#     length = len(str_toRev)
#     for i in range(length-1,-1,-1):
#         yield str_toRev[i]


# for char in rev_str("Happy"):
#     print(char)





my_list = [1,2,3,4,5,6,7,8,9,0]

# print([x**2 for x in my_list])


# Generator expression
a = (x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
