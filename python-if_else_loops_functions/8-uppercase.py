#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            letter_uppercase = ord(i) - 32
            print("{}".format(chr(letter_uppercase)), end="")
        else:
            print("{}".format(i), end ="")
