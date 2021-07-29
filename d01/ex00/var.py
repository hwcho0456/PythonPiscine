#!/usr/bin/env python3

def my_var():
    data = [42, '42', 'quarante-deux', 42.0, True, [42], {42: 42}, (42,), set()]
    for i in range(len(data)):
        locals()["var_{}".format(i)] = data[i]
        print(locals()["var_{}".format(i)], "has a type", type(locals()["var_{}".format(i)]))

if __name__ == '__main__':
    my_var()
