class Human:
    def __init__(self, name="Human"):
        self.name = name


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for human in args:
            self.passengers.append(human)


    def print_passengers_name(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"No passengers in {self.brand}")

olivia = Human("Olivia")
timofej = Human("Timofej")
david = Human("David")

fahrrad = Car("fahrrad")

fahrrad.add_passenger(olivia, timofej, david)

fahrrad.print_passengers_name()


