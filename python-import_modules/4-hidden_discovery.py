import sys
import hidden_4


def main():
    for words in dir(hidden_4):
        if words[:2] != "__":
            print(words)


if __name__ == "__main__":
    main()
