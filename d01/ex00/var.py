#!/usr/bin/env python3

def my_var():
    var = [42, '42', 'quarante-deux', 42.0, True, [42], {42: 42}, (42,), set()]
    for i in var:
        print(str(i), "has a type", type(i))

if __name__ == '__main__':
    my_var()
