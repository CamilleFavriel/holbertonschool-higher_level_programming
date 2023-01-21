#!/usr/bin/python3
import sys

argv = sys.argv[1:]

if len(argv) == 0:
    print("0 arguments.")

elif len(argv) == 1:
    print("1 argument:")

else:
    print(f"{len(argv)} arguments:")

for i, words in enumerate(argv, start=1):
    # Print the position and value of each argument
    print(f"{i}: {words}")


if __name__ == "__main__":
    main()
