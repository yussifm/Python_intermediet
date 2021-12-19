class Duck:
    def sound(self):
        print("quick quick .......")
    def canSwin(self):
        print("duck swins")

class Person:
    def sound(self):
        print("Person imiting the sound of duck")

    def canSwin(self):
        print("Person can also swim")


def combine_all(obj):
    obj.sound()
    obj.canSwin()

john = Person()
donaldDuck = Duck()
combine_all(john)
combine_all(donaldDuck)