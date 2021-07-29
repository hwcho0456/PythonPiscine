#!/usr/bin/env python3

import sys

def state(*args):
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
    if args[1] in reverse_capital_cities:
        if reverse_capital_cities.get(args[1]) in reverse_states:
            print(reverse_states.get(reverse_capital_cities.get(args[1])))
            return
    print("Unknown capital city")

if __name__ == '__main__':
    state(*sys.argv)
