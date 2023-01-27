#!/usr/bin/python3
def safe_print_integer(value):
    i = 0
    try:
        for i in range(value):
            print(value[i], end='')
            i += 1
    except IndexError:
        pass
    print()
    return i
