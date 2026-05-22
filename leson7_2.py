#generatoren
#eng mit iteratoren
#funktion, die werte nach und nach liefern
import numbers
from itertools import count


def raise_to_the_degrees(number, max_degree):
    i = 0

    for _ in range(max_degree):
        yield number ** i
        i += 1

res = raise_to_the_degrees(2, 5)
print(res)

for value in res:
    print(value)

#yealdd gibt werte zurück bricht aber nicht ab, merkt zustand wie eine Variable
