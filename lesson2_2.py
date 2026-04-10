import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Time to chill")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Executed!")
        elif self.gladness < 0:
            print("Sayori!")
            self.alive = False
        elif self.progress > 5:
            print("You passed the Exam! You will also be killed. sorry not sorry")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness is {self.gladness}")
        print(f"Progress is {round(self.progress, 2)}")

    def live(self, day):
        day = " Day" + str(day) + "of" + self.name + ("life! ")
        print(f"{day:=^50}")

        life_cube = random.randint(1, 3)

        if life_cube==1:
            self.to_study()
        elif life_cube==2:
            self.to_sleep()
        else:
            self.to_chill()

        self.end_of_day()
        self.is_alive()

sara = Student("Sara")

for day in range(1, 365):
    if not sara.alive:
        break
    sara.live(day)
    #s