#!/usr/bin/env python3

import sys
import requests
import json
import dewiki

def request_wikipeadia(argv):
    try:
        if len(argv) != 2:
            raise Exception("wrong arguments")
        res = requests.get("https://en.wikipedia.org/w/api.php", {"action":"parse","page":argv[1],"prop":"wikitext","format":"json","redirects":"true"})
        res.raise_for_status()
        data = json.loads(res.text)
        if data.get("error") is not None:
            raise Exception(data["error"]["info"])
        wiki_data = dewiki.from_string(data["parse"]["wikitext"]["*"])
        with open("{}.wiki".format(sys.argv[1]), "w") as f:
            f.write(wiki_data)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    request_wikipeadia(sys.argv)