#!/usr/bin/env python3

from elem import *

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content)

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', attr=attr, content=content)

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', attr=attr, content=content)

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', attr=attr, content=content)

class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='meta', attr=attr, tag_type='simple')

class Img(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='img', attr=attr, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', attr=attr, content=content)

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='tr', attr=attr, content=content)

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', attr=attr, content=content)

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', attr=attr, content=content)

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', attr=attr, content=content)

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', attr=attr, content=content)

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='li', attr=attr, content=content)

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h1', attr=attr, content=content)

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', attr=attr, content=content)

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', attr=attr, content=content)

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, content=content)

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', attr=attr, content=content)

class Hr(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='hr', attr=attr, tag_type='simple')

class Br(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='br', attr=attr, tag_type='simple')

if __name__ == '__main__':
    try:
        assert Html().__str__() == "<html></html>"
        assert Head().__str__() == "<head></head>"
        assert Title().__str__() == "<title></title>"
        assert Meta().__str__() == "<meta />"
        assert Img().__str__() == "<img />"
        assert Table().__str__() == "<table></table>"
        assert Tr().__str__() == "<tr></tr>"
        assert Th().__str__() == "<th></th>"
        assert Td().__str__() == "<td></td>"
        assert Ul().__str__() == "<ul></ul>"
        assert Ol().__str__() == "<ol></ol>"
        assert Li().__str__() == "<li></li>"
        assert H1().__str__() == "<h1></h1>"
        assert H2().__str__() == "<h2></h2>"
        assert P().__str__() == "<p></p>"
        assert Div().__str__() == "<div></div>"
        assert Span().__str__() == "<span></span>"
        assert Hr().__str__() == "<hr />"
        assert Br().__str__() == "<br />"
        assert Html([Head(),Body()]).__str__() == "<html>\n  <head></head>\n  <body></body>\n</html>"
    except:
        print("test failed")

    
    title = Title(Text("Hello ground!"))
    head = Head(title)
    h1 = H1(Text("Oh no, not again!"))
    img = Img({"src":"http://i.imgur.com/pfp3T.jpg"})
    body = Body([h1, img])
    html = Html([head, body])
    print(html)