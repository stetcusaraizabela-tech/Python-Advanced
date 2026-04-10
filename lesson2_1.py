#class attribute vs object attribute
class Student:
    #class-attribute
    amount_of_students = 0
    #object attribute
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_students += 1

    def __str__(self):
        return  f"Hallo, im a stundent my height is  {self.height}"


eyulel= Student(height=167)
print(eyulel.amount_of_students)

rafael= Student(175)
print(rafael.amount_of_students)


basim = Student(200)
print(basim.amount_of_students)

print(basim)

