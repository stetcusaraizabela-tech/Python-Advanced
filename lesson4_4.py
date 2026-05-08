class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 128

    def calculate(self):
        print("Calculator...")

class Display:
    def __init__(self):
        self.resolution = "4K"
    def display(self):
        print("Display...")

class Smartphone(Computer, Display):
    def print_info(self):
        print(self.memory)
        print(self.resolution)

iphone = Smartphone()
iphone.display()
iphone.calculate()