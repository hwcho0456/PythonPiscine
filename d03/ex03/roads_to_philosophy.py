#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

def roads_to_philosophy(prev, path):
    try:
        res = requests.get("https://en.wikipedia.org{}".format(path))
        res.raise_for_status()
    except requests.HTTPError as e:
        if (res.status_code == 404):
            return print("It's a dead end !")
        return print(e)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find(id='firstHeading').text
    if title in prev:
        return print("It leads to an infinite loop !")
    prev.append(title)
    print(title)
    if title == "Philosophy":
        return print("{} roads from {} to philosophy !".format(len(prev), prev[0]))
    content = soup.find(id="mw-content-text")
    links = content.select("p > a")
    for l in links:
        if l.get('href') is not None and l['href'].startswith('/wiki/') and not l['href'].startswith('/wiki/Wikipedia:') and not l['href'].startswith('/wiki/Help:'):
            return roads_to_philosophy(prev, l['href'])
    return print("It leads to a dead end !.")

def main():
    try:
        if (len(sys.argv) != 2):
            raise Exception("wrong arguments")
        roads_to_philosophy([], "/wiki/"+sys.argv[1])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
