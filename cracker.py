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
    filenamehash = input("Complete file name (with path) -----> ")
    os.system("mv "+filenamehash+" rar.rar")
    os.system("clear")
    os.system("rm -f hash.txt")
    os.system("rar2john rar.rar > hash.txt")
    os.system("sed -i 's/rar.rar://g' hash.txt")
    os.system("mv rar.rar "+filenamehash+"")
    time.sleep(5)
    os.system("clear")
    print("")
    os.system("hashcat -m 13000 -a3 'hash.txt' ?d?d?d?d")

def crack():
    os.system("clear")
    print("")
    os.system("hashcat -m 13000 -a3 'hash.txt' ?d?d?d?d")


start_menu()