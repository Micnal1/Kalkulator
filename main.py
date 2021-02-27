import math
import logging

logging.basicConfig(level=logging.DEBUG)

def dodawanie():
    a = float(input('Podaj składnik 1:'))
    b = float(input('Podaj składnik 1:'))
    list = [a,b]
    while True:
        nr = 3
        c = input(f'Podaj składnik {nr} lub wciśnij enter:')
        if not bool(c):
            break
        c = float(c)
        nr += 1
        list.append(c)

    if len(list) == 2:
        logging.debug(f'Dodaję {a} i {b}')

    if len(list) > 2:
        text = ''
        for i in list:
            text += str(i) +" "

        logging.debug(f"Sumuję liczby : {text}")

    print('Wynik to:','{:0.2f}'.format(math.fsum(list)))

def mnożenie():
    a = float(input('Podaj składnik 1:'))
    b = float(input('Podaj składnik 1:'))
    list = [a,b]
    while True:
        nr = 3
        c = input(f'Podaj składnik {nr} lub wciśnij enter:')
        if not bool(c):
            break
        c = float(c)
        nr += 1
        list.append(c)

    if len(list) == 2:
        logging.debug(f'Mnożę {a} i {b}')

    if len(list) > 2:
        text = ''
        for i in list:
            text += str(i) +" "

        logging.debug(f"Mnożę liczby : {text}")

    print('Wynik to:','{:0.2f}'.format(math.prod(list)))

def odejmowanie():
    a = float(input('Podaj składnik 1:'))
    b = float(input('Podaj składnik 1:'))
    list = [a,b]
    if len(list) == 2:
        logging.debug(f'Odejmuję {b} od {a}')

    print('Wynik to:','{:0.2f}'.format(a - b))

def dzielenie():
    a = float(input('Podaj składnik 1:'))
    b = float(input('Podaj składnik 1:'))
    list = [a,b]
    if len(list) == 2:
        logging.debug(f'Dzielę {a} przez {b}')

    print('Wynik to:','{:0.2f}'.format(a / b))

if __name__ == "__main__":
    while True:
        menu = input(
        """
 0 - wyjście
 1 - Dodawanie
 2 - Odejmowanie
 3 - Mnaożenie
 4 - Dzielenie
 Jakie działanie chcesz wykonać?:""")

        if menu == '0':
            break

        if menu == '1':
            dodawanie()

        elif menu == '2':
            odejmowanie()

        elif menu == '3':
            mnożenie()

        elif menu == '4':
            dzielenie()