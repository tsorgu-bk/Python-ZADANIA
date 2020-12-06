#! /usr/bin/env python

import os
from PIL import Image

# *********************Working with files*************************


def files_count():
    path = input("Podaj ścieżkę:")
    list_b = list(os.listdir(path))
    len_l = len(list_b)
    print("Ilość plików w tym katalogu:", len_l)


def directory_structure(path):
    catalog = os.listdir(path)
    for file in catalog:
        new_path = os.path.join(path, file)
        print(new_path)
        if os.path.isdir(new_path):
            directory_structure(new_path)


def directory_structure_service():
    path = input("Podaj ścieżkę: ")
    directory_structure(path)


def extensions_converting(file_name):  # z wykorzystaniem biblioteki img
    img = Image.open(file_name)
    img.save(file_name[:-4] + ".png")


def extensions_converting_to_png(file_name):
    os.rename(file_name, file_name[:-4] + ".png")   # biblioteka os


def extensions_converting_to_jpg(file_name):
    os.rename(file_name, file_name[:-4] + ".jpg")  # biblioteka os


def extensions_converting_serviece(): # można podmienić, aby nie tworzyć nowych plików
    files = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg']
    #files = ['img1.png', 'img2.png', 'img3.png', 'img4.png']
    for file in files:
        extensions_converting_to_png(file)
        #extensions_converting_to_jpg(file)

if __name__ == '__main__':
    # files_count()
    # directory_structure_service()
     extensions_converting_serviece()
