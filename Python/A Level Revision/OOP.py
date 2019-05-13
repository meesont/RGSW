# OOP Programming
class Person():
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.dead = False
    def set_dead(self, value):
        self.dead = value
    def set_age(self, value):
        self.age = value
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

tom = Person("Tom")
tom.set_dead(False)
tom.set_age(18)
tomsName = tom.get_name
print(tomsName)
