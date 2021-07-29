#!/usr/bin/env python3

import sys

def capital_city(*args):
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
    if args[1] in states:
        if states.get(args[1]) in capital_cities:
            print(capital_cities.get(states.get(args[1])))
            return
    print("Unknown state")

if __name__ == '__main__':
    capital_city(*sys.argv)
