import os, sys


def extract_hash():
    rarname = sys.argv[1]
    os.system("rm -f hash.txt")
    os.system(f"rar2john {rarname} > hash.txt")
    os.system(f"sed -i 's/{rarname}://g' hash.txt")


def crack():
    mode = sys.argv[2]
    length = sys.argv[3]
    if mode == "bruteforce":
        if length == "4":
            os.system("hashcat -m 13000 -a 3 'hash.txt' ?d?d?d?d > /dev/null")
        if length == "6":
            os.system("hashcat -m 13000 -a 3 'hash.txt' ?d?d?d?d?d?d > /dev/null")
    if mode == "wordlist":
        wordlist = input("Name and path of the wordlist to use: ")
        os.system(f"hashcat -m 13000 -a 0 hash.txt {wordlist} > /dev/null")
    os.system("hashcat -m 13000 --show hash.txt > password.txt")


def show_password():
    with open("password.txt", "r") as file:
        hashandpass = file.read().strip()

    if not hashandpass:
        print("\033[31mPassword not found, try again with another length!\033[0m")
        return

    password = hashandpass.rsplit(":", 1)[1]
    print(f"The password is \033[32m{password}\033[0m.")
    os.system(f"echo {password} | xclip -selection clipboard")
    os.system("rm -f password.txt")
    



if len(sys.argv) < 3:
    print("Usage: python3 main.py (file) (mode: bruteforce/wordlist) (length of password to crack: 4/6)")
    print("Example: python3 main.py example.rar bruteforce 4")
    sys.exit(0)
if len(sys.argv) >= 3:
    extract_hash()
    crack()
    os.system("rm -f hash.txt")
    print()
    show_password()
    print()
    sys.exit(0)



