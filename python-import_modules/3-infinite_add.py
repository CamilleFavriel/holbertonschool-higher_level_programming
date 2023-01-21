#!/usr/bin/python3
import sys

def main():
    args = sys.argv[1:]
    total = 0
    
    for i in args:
        total += int(i)
    print(total)


if __name__ == "__main__":
    main()
