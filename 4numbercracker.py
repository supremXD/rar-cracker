import os, time

def start_menu():
    os.system("clear")
    while True:
        options()

def options():
    print("")
    print("              |                    1 -->> Extract the hash of the rar (first step)")
    print("              |                    2 -->> Brute force attack")
    print("              |                    3 -->> Diccionary attack")
    print("              |                    4 -->> See password (last step)")
    print("              |                    5 -->> Exit")
    option = input("              +-> ")

    if option == "1":
        os.system("clear")
        print("")
        filenamehash = input("Complete file name (with path) -----> ")
        os.system("mv "+filenamehash+" rar.rar")
        os.system("rm -f hash.txt")
        os.system("rar2john rar.rar > hash.txt")
        os.system("sed -i 's/rar.rar://g' hash.txt")
        os.system("mv rar.rar "+filenamehash+"")
        print("Done!!")
        time.sleep(3)
        os.system("clear")
        while True:
            options()

    if option == "2":
        print("")
        os.system("hashcat -m 13000 -a 3 'hash.txt' ?d?d?d?d > password.txt")
        while True:
            options()

    if option == "3":
        print("")
        os.system("crunch 4 4 0123456789 -o wordlist.txt")
        os.system("hashcat -m 13000 -a 0 hash.txt wordlist.txt > password.txt")
        os.system("rm -f wordlist.txt")
        while True:
            options()

    if option == "4":
        print("")
        os.system("clear")
        print("The password is in the hash, there are the numbers behind the two points (:XXXX)")
        time.sleep(5)
        os.system("cat password.txt")
        time.sleep(5)
        while True:
            options()

    if option == "5":
        os.system("rm -f hash.txt")
        os.system("clear")
        print("Goodbye :D!!!")
        exit()

start_menu()