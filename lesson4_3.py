class Hello():
    def __init__(self):
        print("Hello!")

class HelloWorld(Hello):
    def __init__(self):
        super().__init__()
        print("World!")

hello_world = HelloWorld()

class Class1:
    var = 20

    def __init__(self):
        self.var = 10

class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)

class2 = Class1()

class Grandparent:
    def about(self):
        print("Grandparent")

    def about_myself(self):
        print("Ana")

class Parent(Grandparent):
    def __init__(self):
        print("Mkjijgihs PRAkeijiPARENT")

class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()

timofej = Child()
