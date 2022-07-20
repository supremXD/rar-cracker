import os, time

def decoracion():
    print("              |                    1 -->> Download the files (obligatory)")
    print("              |                    2 -->> Extract the hash of the rar")
    print("              |                    3 -->> Crack the hash")
    print("              |                    4 -->> Exit")    
    option = input("              +-> ")

    if option == "1":
        files()

    if option == "2":
        ddos()

    if option == "3":
        phishing()

    if option == "4":
        wpscan()