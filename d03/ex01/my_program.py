#!/usr/bin/env python3

from path import Path

def my_program():
    try:
        Path.makedirs("testdir")
    except Exception as e:
        print(e)
    Path.touch("testdir/testfile")
    file = Path("testdir/testfile")
    file.write_text("file write test")
    print(file.read_text())

if __name__ == '__main__':
    my_program()