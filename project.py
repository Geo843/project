def main():
    meniu()


def meniu():
    print(f'********Bine ai Venit ********')
    print()
    choice = input('''

               A. Login
               S.Logout

                 Alege o varianta: ''')

    if choice == 'A' or choice == 'a':
        login()

    elif choice == 'S' or choice == 's':
        iesire()
    else:
        print(f'Trebuie sa selectezi fie A sau B')
        print('mai incearca ')
        meniu()


def login():
    pass


def iesire():
    pass
main()

class Manager:

    def __init__(self,adaugare,eliminare,calificari):
        self.adaugare = adaugare
        self.eliminare = eliminare
        self.calificari = calificari


class Operator:

    def __init__(self,produse ):
        self.produse = produse


class Gestionar:

    def __init__(self,materie_prima ):
        self.materie_prima = materie_prima


