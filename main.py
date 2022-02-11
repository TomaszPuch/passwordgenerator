#program generujacy bezpieczne hasla
#definicje
import random, pyperclip
def generujhaslo():
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    liczby = "1234567890"
    znaki_specjalne = "~!@#$%^&*()_+{:}<>?[];"
    haslo = []
    for i in range(15):
        temp = random.randrange(1,4)
        if temp == 1:
            znak = alfabet[random.randrange(1,len(alfabet))]
            tak_nie = random.randint(1,2)
            if tak_nie == 1:
                nowy_znak = znak.upper()
                haslo.insert(1, nowy_znak)
            if tak_nie == 2:
                haslo.insert(1, znak)
        if temp == 2:
            haslo.insert(1,liczby[random.randrange(1, len(liczby))])
        if temp == 3:
            haslo.insert(1,znaki_specjalne[random.randrange(1, len(znaki_specjalne))])
    haslo = str(haslo)
    haslo = haslo.replace(",","").replace("[","").replace("'","").replace(" ","")
    print(haslo)
    pyperclip.copy(haslo)
    pyperclip.paste()
def wejscie_mozliwosci():
    #print("Cześć, witaj w programie generującym bezpieczne hasła oto nasze możliwości:\n[1] - wygeneruj nowe hasło\n\n[2]\n\n[3]\n\n:")
    print("\n\nOto twoje bezpieczne hasło:\n\n")
    generujhaslo()
    print("\nżeby ułatwić ci życie, skopiowaliśmy twoje bezpieczne hasło automatycznie do schowka")

wejscie_mozliwosci()
input("Wciśnij dowolny przycisk aby zakończyć działanie\n:")






