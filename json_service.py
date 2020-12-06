#! /usr/bin/env python

import json

def write_json(x = None):
    f = open('film_database.json', 'w')
    json.dump(data, f, indent=4)


def show_database():

    for Movies in data['Movies']:
        print(Movies)
    print("")

def add_movie(title, rating):
    new_movie = {
        "Title": title,
        "Rating": rating
    }
    new_data = data['Movies']
    new_data.append(new_movie)
    write_json(data)
    print("New movie added")


def delete_movie(title):
    for Movies in data['Movies']:
        if Movies['Title'] == str(title):
            del Movies['Title']
            del Movies['Rating']
            write_json(data)


while 1:
    file = open("film_database.json")
    data = json.load(file)
    print("What do you want to do?")
    print("1. Show database")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Exit")
    write_json()

    choice = int(input())
    if choice == 1:
        show_database()
    elif choice == 2:
        title = input("Title:")
        rating = input("Rating:")
        add_movie(title, rating)
    elif choice == 3:
        title = input("Movie to delete:")
        delete_movie(title)
    elif choice == 4:
        break
    else:
        print("Pick 1, 2, 3 or 4 !! \n")
file.close()

