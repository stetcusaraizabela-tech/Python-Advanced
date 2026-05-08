class HelloWorld:
    name = "Hello"
    _name = "_Hello" #empfehlung nicht außen zu verwenden
    __name = "__Hello" #python verstckr,gm skm jbnrwau8

    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"

    def printer(self):
        print(self.name)
        print(self._name)
        print(self.__name)
        print(self.world)
        print(self._world)
        print(self.__world)

hey = HelloWorld()
hey.printer()

class Hello(HelloWorld):
    def __init__(self):
        print.(self.__hello)

hi = Hello()
