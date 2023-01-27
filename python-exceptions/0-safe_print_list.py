#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return x
    except:
        for i in range(x):
            try:
                print(my_list[i], end="")
            except IndexError:
                break
            print()
            return i
