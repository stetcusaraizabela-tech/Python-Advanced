#introspection

import random

from lesson2 import makarius

help(random)   #erklärt dir was random bedeutet

print(__name__)   #startpunkt des programmes

print(type(5))       #eine art support - sagt dir, dass es ein integer ist
print(type(2.34))       #eine art support - sagt dir, dass es ein float ist
print(type("Hiiii")) #eine art support - sagt dir, dass es ein string ist
print(type(True)) #eine art support - sagt dir, dass es ein boolean ist
print(type([1, 2, 3])) #eine art support - sagt dir, dass es ein list ist #kann verändert werden
print(type((1, 2, 3))) #eine art support - sagt dir, dass es ein tupil ist  #kann nicht verändert werden
print(type({"bob": "telefonnummer"})) #eine art support - sagt dir, dass es ein dictionary ist

class Student:
    pass

nick = Student()
print(type(nick))

class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("I Eat")

david = Human("David")
print(dir(david))

print(dir())

print(hasattr(david, "name")) #true
print(hasattr(david, "age")) #false
#hasattr überprüft,ob es das gibt
print(getattr(david, "age", "Nicht gefunden")) #nicht gefunden
print(getattr(david, "name", "Nicht gefunden")) #david
#hasattr überprüft,ob es das gibt und sagt ob es das gibt oder nicht


def hello()
    print("Hello")

x =  10

print(callable(x)) #false
print(callable(hello)) #true


 #n
# issubclass() achschauen ob kind was von den eltern geerbt hat
class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent)) #true
print(issubclass(Parent, Child)) #false

#objektzugehörigkeit prüfen mit isinstance()
makarius = Parent()
print(isinstance(makarius, Parent)) #true
print(isinstance(makarius, Child)) #true
#warum?????????????????????? weill kind von elternteil erbt