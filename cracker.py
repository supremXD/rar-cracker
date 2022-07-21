import os, time

def start_menu():
    os.system("clear")
    while True:
        hash()

def hash():
    os.system("clear")
    print("")
    filenamehash = input("Complete file name (with path) -----> ")
    os.system("mv "+filenamehash+" rar.rar")
    os.system("rm -f hash.txt")
    os.system("rar2john rar.rar > hash.txt")
    os.system("sed -i 's/rar.rar://g' hash.txt")
    os.system("mv rar.rar "+filenamehash+"")
    time.sleep(3)
    os.system("clear")
    print("")
    os.system("hashcat -m 13000 -a3 -o password.txt 'hash.txt' ?d?d?d?d --show")
    os.system("rm -f hash.txt")
    print("The password is the next digits of the last ':' of the line (Example: ':0000'")
    os.system("cat password.txt")
    while True:
        exit()

start_menu()