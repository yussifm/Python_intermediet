# finb sequence

from random import randint


a, b = 0,1

for i in range(0,10):
    print(a)
    a, b = b, a+b
    

print("-------------------------------")
print("-------------------------------")
#Fibn generator
print("-------------------------------")
print("Generator")
print("-------------------------------")
def fibgen(num):
    a, b = 0,1

    for i in range(0,num):
        yield "{}: {}".format(i+1, a)
        a, b = b, a+b
        
        
for items in fibgen(30):
    print(items)
    
    
    