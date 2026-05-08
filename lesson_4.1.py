class Grandparent:
    height = 150
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    #kontruktor einer klasse
    def __init__(self):
        print(self.height)
        print(self.age)
        print(self.satiety)

basim = Child()