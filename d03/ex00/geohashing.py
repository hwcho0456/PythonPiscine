#!/usr/bin/env python3

import antigravity
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("usage example: ./geohashing.py 37.421542 -122.085589 2005-05-26-10458.68") # "37.857713 -122.544543"
        exit()
    try:
        antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode())
    except Exception as e:
        print(e)