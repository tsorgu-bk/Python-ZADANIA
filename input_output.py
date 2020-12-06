#! /usr/bin/env python

# *********************INPUT/OUTPUT*************************

def hello_world():
    print("Witaj Podróżniku!!!!")


def inputting_data():
    dane = input("Podaj imię, nazwisko oraz rok urodzenia:")
    name, surname, birth_year = dane.split()
    print("Witaj", name, "z rodu", surname, "będący w służbie od", birth_year)


def data_saving():
    file = "key.txt"
    file = open(file, 'r')
    key = file.read()
    file.close()
    password = input("Podaj szyfr:")

    while password != key:
        password = input("Podaj szyfr:")

    action = input("Chcesz zmienić kod? [y/n]")
    if action == "y":
        new_key = input("Podaj nowy szyfr: ")
        file = open("key.txt", "w")
        file.write(new_key)
        file.close()
        print("Zmieniono szyfr !!!! ")
    elif action == "n":
        print("nara")


if __name__ == '__main__':
    # hello_world()
    # inputting_data()
    data_saving()

