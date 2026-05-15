#exeption erheben
def checker(text):
    if type(text) != str:
        raise TypeError("ksdmjkjsdjjskakkds.   kein string !!!!!! wie konntest du nur?")
    else:
        return text

checker(123)