print("Willkommen bei meinem Rechner!")

def multiplizieren(a, b):
   ergebnis =  a * b
   return ergebnis

def dividieren(a, b):
    if b == 0:
        return None
    ergebnis = a / b
    return ergebnis

def subtrahieren(a, b):
    ergebnis = a - b
    return ergebnis

def addieren(a, b):
    ergebnis = a + b
    return ergebnis

def eingabechecken(text1, text2):
    try:
        a = float(input(text1))
        b = float(input(text2))
    except ValueError:
        print("Bitte nur Zahlen eingeben!")
        return None, None

    return a, b

    

while True:
    print("1 fuer Multiplikation")
    print("2 fuer Division")
    print("3 Fuer Subtraktion")
    print("4 fur Addition")

    auswahl = float(input("Bitte waehlen sie einen Rechenoperator: "))

    if auswahl == 1:
        a, b = eingabechecken("Bitte tippen sie den 1. Faktor ein: ", "Bitte tippen sie den 2. Faktor ein: ")
        if a is None or b is None:
            continue
        ergebnis = multiplizieren(a, b)
        print("Ihr Ergebnis lautet: ", round(ergebnis, 2))

    elif auswahl == 2:
        a, b = eingabechecken("Bitte tippen sie die Zahl ein mit der sie dividieren moechten: ", "Bitte tippen sie die Zahl ein mit der dividiert werden soll: ")
        if a is None or b is None:
            continue
        ergebnis = dividieren(a, b)
        if ergebnis is None:
            print("Division durch 0 nicht erlaubt!")
            continue
        print("Ihr Ergebnis lautet: ", round(ergebnis, 2))

    elif auswahl == 3:
        a, b = eingabechecken("Bitte geben sie die Zahl ein von der abgezogen werden soll: ", "Bitte geben sie die Zahl ein das abgezogen werden soll: ")
        if a is None or b is None:
            continue
        ergebnis = subtrahieren(a, b)
        print("Ihr Ergebnis lautet: ", round(ergebnis, 2))

    elif auswahl == 4:
        a, b = eingabechecken("Bitte geben sie die erste Zahl die addiert werden soll: ", "Bitte geben sie die zweite Zahl die addiert werden soll: ")
        if a is None or b is None:
            continue
        ergebnis = addieren(a, b)
        print("Ihr Ergebnis lautet: ", round(ergebnis, 2))

    else:
        print("Ungueltige Eingabe!")

    weiter = input("Moechten sie weiter rechnen? (j/n) : ")
    if weiter.lower() != "j":
        break