#!/usr/bin/env python3

def numbers():
    try:
        filename = open("numbers.txt", 'r')
    except:
        exit()
    else:
        for i in filename.readline().rstrip("\n").split(","):
            print(i)
        filename.close()

if __name__ == '__main__':
    numbers()
