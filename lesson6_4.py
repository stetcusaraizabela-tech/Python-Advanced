try:
    number = int("ABC")
except ValueError as error:
    print("Fehlermeldung", error)