import os

def install():
    print("")
    os.system("sudo apt install crunch -y")
    os.system("clear")
    print("Done!!!")
    while True:
        exit()

install()