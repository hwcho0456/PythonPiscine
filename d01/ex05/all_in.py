#!/usr/bin/env python3

import sys

def all_in(*args):
    if len(args) != 2:
        return
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    reverse_capital_cities = {v:k for k,v in capital_cities.items()}
    reverse_states = {v:k for k,v in states.items()}
    for string in args[1].split(','):
        name = string.strip().title()
        if name == "":
            continue
        elif name in states:
            if states.get(name) in capital_cities:
                print(capital_cities.get(states.get(name)), "is the capital of", name, end="\r\n")
        elif name in reverse_capital_cities:
            if reverse_capital_cities.get(name) in reverse_states:
                print(name, "is the capital of", reverse_states.get(reverse_capital_cities.get(name)), end="\r\n")
        else:
            print(string.strip(), "is neither a capital city nor a state", end="\r\n")

if __name__ == '__main__':
    all_in(*sys.argv)
