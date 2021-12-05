import random


print("Hello !!! there")
print("What's your name")
name = input()

print("How old are you " +name)
age = int(input())
if age >= 21:
    print("Matured")
elif age < 21:
    print("small")
else:
    print("invilid age")
print("Nice to be that age " + str(age))

for i in range(0, 100):
    print("I is ", i*random.randint(1, 200))