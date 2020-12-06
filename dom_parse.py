#! /usr/bin/env python

import xml.dom.minidom as md
import json

def xml_parse():
    dom_tree = md.parse('plik.xml')
    users = dom_tree.documentElement
    user = users.getElementsByTagName('user')
    i=0
    for u in user:
        print("User number:", i)
        print("Name: {}".format(u.getElementsByTagName('name')[0].childNodes[0].data))
        print("Password: {}".format(u.getElementsByTagName('password')[0].childNodes[0].data))
        i+=1

    id = int(input("Change password to user :"))
    new_passwd = input("New password: ")
    user[id].getElementsByTagName('password')[0].childNodes[0].data = new_passwd
    dom_tree.writexml(open("nowy_plik.xml", 'w'))


if __name__ == '__main__':
    xml_parse()