
def dodawanie():
    output = 0
    counting_down = 1
    list_storage = []
    more_text = ''
    more_text2 = ''

    while True:
        numbers =['0','1','2','3','4','5','6','7','8','9','.']
        type_float = True
        storage = input(f'podaj {counting_down} liczbę{more_text}:')
        counting_down +=1

        if counting_down > 2:
            more_text = ' lub wciśnij ENTER'

        if bool(storage) == False:
            break

        for i in storage:
            if not i in numbers:
                type_float = False

        if type_float == False:
            print("Błąd: Źle napisana liczba!")
            break
        else:
            output +=float(storage) * 10
            list_storage.append(storage)

    if len(list_storage) == 1:
        print(f"{list_storage[0]} to {list_storage[0]}!")
    elif len(list_storage) == 2:
        print(f"Dodaję {(list_storage[0])} i {list_storage[1]}")  #wypisywane liczby nie mają formatu!!
    elif len(list_storage) > 2:
        for i in list_storage:
            more_text2 +=i+', '

        print(f"Sumuję liczby: {more_text2}")

    return output/10

def odejamowanie():
    output = 0
    counting_down = 1
    list_storage = []
    VS_BAG = 10

    while True:
        if counting_down > 2:
            break
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        type_float = True
        storage = input(f'podaj {counting_down} liczbę:')


        for i in storage:
            if not i in numbers:
                type_float = False

        if type_float == False:
            print("Błąd: Źle napisana liczba!")
            break
        else:
            if counting_down == 1:
                output +=float(storage) * VS_BAG
                list_storage.append(storage)
            else:
                output -=float(storage) * VS_BAG
        counting_down += 1

    return  output/VS_BAG

def mnożenie():
    output = 1
    counting_down = 1
    list_storage = []
    more_text = ''
    more_text2 = ''

    while True:
        numbers =['0','1','2','3','4','5','6','7','8','9','.']
        type_float = True
        storage = input(f'podaj {counting_down} liczbę{more_text}:')
        counting_down +=1

        if counting_down > 2:
            more_text = ' lub wciśnij ENTER'

        if bool(storage) == False:
            break

        for i in storage:
            if not i in numbers:
                type_float = False

        if type_float == False:
            print("Błąd: Źle napisana liczba!")
            break
        else:
            output *=float(storage)
            list_storage.append(storage)

    if len(list_storage) == 1:
        print(f"{list_storage[0]} to {list_storage[0]}!")
    elif len(list_storage) == 2:
        print(f"Mnożę {(list_storage[0])} i {list_storage[1]}")
    elif len(list_storage) > 2:

        for i in list_storage:
            more_text2 +=i+', '

        print(f"Mnożę liczby: {more_text2}")

    return output

def dzielenie():
    output = 0
    counting_down = 1
    list_storage = []
    VS_BAG = 1

    while True:
        if counting_down > 2:
            break
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        type_float = True
        storage = input(f'podaj {counting_down} liczbę:')


        for i in storage:
            if not i in numbers:
                type_float = False

        if type_float == False:
            print("Błąd: Źle napisana liczba!")
            break
        else:
            if counting_down == 1:
                output +=float(storage) * VS_BAG
                list_storage.append(storage)
            else:
                output = output/(float(storage) * VS_BAG)
        counting_down += 1

    return  output/VS_BAG


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
            wynik = '{:0.2f}'.format(dodawanie())
            print(f'wynik to: {wynik}')

        elif menu == '2':
            wynik = (odejamowanie())
            print(f'wynik to: {wynik}')

        elif menu == '3':
            wynik = '{:0.2f}'.format(mnożenie())
            print(f'wynik to: {wynik}')

        elif menu == '4':
            wynik = '{:0.2f}'.format(dzielenie())
            print(f'wynik to: {wynik}')