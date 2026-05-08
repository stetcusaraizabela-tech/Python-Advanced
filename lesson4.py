class Parent:
    pass

class Child(Parent):
    pass

 #vererbung btw

class Human:
    height = 170

class Student(Human):
    pass

class Worker(Human):
    pass

# objekt der klasse student
rafi = Student()
print(rafi.height)