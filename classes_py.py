
class Person:
    #attributes
    species = "HomoSP"

    # constructor
    def __init__(self, name):
        self.name = name

    # Method
    def walk(self):
        print("walking")
    
    def talking(self):
        print("Talking")


# john = Person("john")
# john.walk()


# bund, unbund, classmethod, staticmethod
class A:

    @classmethod
    def f(self, b):
        print(2*b)

    @staticmethod
    def g(name):
        print("Hello %s" %name)

A.f(2)
A.g("coded")