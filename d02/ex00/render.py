#!/usr/bin/env python3

import sys, os, re
import settings

def render(contents, html):
    for i in dir(settings):
        if not i.startswith("__"):
            contents = contents.replace("{"+i+"}", str(vars(settings).get(i)))
    html.write(contents)
    html.close()
    
if __name__ == '__main__':
    if len(sys.argv) != 2 or re.search(".template$", sys.argv[1]) is None:
        exit()
    try:
        template = open(sys.argv[1], 'r')
        contents = template.read()
        template.close()
    except:
        exit()
    else:
        try:
            html = open(re.sub(".template$", ".html", sys.argv[1]), 'w')
        except:
            exit()
        else:
            render(contents, html)
            html.close()