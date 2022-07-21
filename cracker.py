import os, time

def start_menu():
    os.system("clear")
    while True:
        options()

def options():
    print("              |                    1 -->> Extract the hash of the rar")
    print("              |                    2 -->> Crack the hash")
    print("              |                    3 -->> Exit")    
    option = input("              +-> ")

    if option == "1":
        hash()

    if option == "2":
        crack()

    if option == "3":
        exit()

def hash():
    os.system("clear")
    print("")
    filenamehash = input("Complete file name -----> ")
    os.system("clear")
    os.system("rar2john "+filenamehash+" > hash.txt")