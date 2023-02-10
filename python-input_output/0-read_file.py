def read_file(filename=""):
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read(), end='')
