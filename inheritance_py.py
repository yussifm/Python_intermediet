
class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w =w
    
    def area(self):
        return self.w*self.h #(w*h)

    def perimeter(self):
        return 2*(self.w + self.h) #2*(w+h)

class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)
        self.s = s


# sq1 = Square(10)
# print(sq1.area())
# print(sq1.perimeter())


# Monkey Patching
class A:
    def __init__(self, num):
        self.num = num

    def add(self, num2):
        print(self.num + num2)


def get_num(self):
    print(self.num)

# Adding a method to the class outside (Monkey Patching)
A.get_num = get_num
b =A(45)
# b.get_num()



# Multiple Inherintance

class foo:
    def foo_method():
        print("foo method")
    
class bar:
    def bar_method():
        print("bar method")

class foobar(foo, bar):

    # overring method
    def foo_method(self):
        super(foo, self).foo_method()






        