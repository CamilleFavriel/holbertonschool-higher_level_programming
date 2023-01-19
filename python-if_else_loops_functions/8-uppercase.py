#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ascii = ord(i)
        if (ord(i) >= 97 and ord(i) <= 122):
            ascii -= 32
        print("{}".format(chr(ascii)), end="")
    print("\n", end="")
