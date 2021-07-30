#!/usr/bin/env python3

from elements import *

class Page:
    def __init__(self, elem):
        self.elem = elem

    def __str__(self):
        if isinstance(self.elem, Elem) and self.elem.tag == "html":
            return "<!DOCTYPE HTML>\n{}".format(self.elem)
        else:
            return "{}".format(self.elem)
    
    def write_to_file(self, filename):
        try:
            html = open(filename+".html", 'w')
        except: 
            exit() 
        else:
            html.write(self.__str__())
            html.close()
        
    def is_valid(self):
        if not isinstance(self.elem, Elem):
            return False
        if not self.elem.tag in ["html", "head", "body", "title", "meta", "img", "table", "th", "tr", 
                                "td", "ul", "ol", "li", "h1", "h2", "p", "div", "span", "hr", "br"]:
            return False
        else:
            if self.elem.tag == "html":
                if len(self.elem.content) != 2:
                    return False
                elif not isinstance(self.elem.content[0], Elem) or self.elem.content[0].tag != "head":
                    return False
                elif not isinstance(self.elem.content[1], Elem) or self.elem.content[1].tag != "body":
                    return False

            elif self.elem.tag == "head":
                if len(self.elem.content) != 1:
                    return False
                elif not isinstance(self.elem.content[0], Elem) or self.elem.content[0].tag != "title":
                    return False

            elif self.elem.tag in ["body", "div"]:
                for i in self.elem.content:
                    if not isinstance(i, Elem) and not isinstance(i, Text):
                        return False
                    elif isinstance(i, Elem) and not i.tag in ["h1", "h2", "div", "table", "ul", "ol", "span"]:
                        return False
            
            elif self.elem.tag in ["title", "h1", "h2", "li", "th", "td"]:
                if len(self.elem.content) != 1:
                    return False
                elif not isinstance(self.elem.content[0], Text):
                    return False
            
            elif self.elem.tag =="p":
                for i in self.elem.content:
                    if not isinstance(i, Text):
                        return False
            
            elif self.elem.tag == "span":
                for i in self.elem.content:
                    if not isinstance(i, Elem) and not isinstance(i, Text):
                        return False
                    elif isinstance(i, Elem) and i.tag != "p":
                        return False

            elif self.elem.tag in ["ul", "ol"]:
                if len(self.elem.content) == 0:
                    return False
                for i in self.elem.content:
                    if not isinstance(i, Elem):
                            return False
                    elif i.tag != "li":
                        return False
            
            elif self.elem.tag == "tr":
                if len(self.elem.content) == 0:
                    return False
                elif not isinstance(self.elem.content[0], Elem) or not self.elem.content[0].tag in ["th", "td"]:
                    return False
                elif self.elem.content[0].tag == "th":
                    for i in self.elem.content:
                        if not isinstance(i, Elem) or i.tag != "th":
                            return False
                elif self.elem.content[0].tag == "td":
                    for i in self.elem.content:
                        if not isinstance(i, Elem) or i.tag != "td":
                            return False
            
            elif self.elem.tag == "table":
                for i in self.elem.content:
                    if not isinstance(i, Elem) or i.tag != "tr":
                        return False
            
            valid = True
            for i in self.elem.content:
                if not isinstance(i, Elem) and not isinstance(i, Text):
                    return False
                if isinstance(i, Elem):
                    valid = valid and Page(i).is_valid()
            return valid

if __name__ == '__main__':
    
    try:
        # Check TAG
        assert (Page( Elem(tag="small") ).is_valid()) == False
        assert (Page( Elem(tag="input") ).is_valid()) == False
        assert (Page( Elem(tag="abcd") ).is_valid()) == False
        # Check HTML
        assert (Page(Html([Body(), Head()])).is_valid()) == False
        assert (Page(Html([Head(), Body()])).is_valid()) == False
        assert (Page(Html([Body(), Head([Title(),Div()])])).is_valid()) == False
        assert (Page(Html([Body(), Head(Title(Text('asdas')))])).is_valid()) == False
        assert (Page(Html([Head(Div()), Body()])).is_valid()) == False
        assert (Page(Html([Head(Title(Text())), Body()])).is_valid()) == False
        # Check body
        assert (Page(Html([Head(Title(Text('tetetat'))), Body()])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(P())])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Div())])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Div(Text("asdsa")))])).is_valid()) == True
        # Check H1, H2
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(H1())])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(H1(Div()))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(H1(Text("H1")))])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(H2())])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(H2(Div()))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(H2(Text("H2")))])).is_valid()) == True
        # Check Ul, Ol
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ul())])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ul(Li()))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ul(Div()))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ul([Li(),Li(),Li(),Div()]))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ol())])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ol(Li()))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ol(Div()))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ol([Li(),Li(),Li(),Div()]))])).is_valid()) == False
        # Check Li
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ul([Li(Text("asd")),Li(),Li()]))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ul([Li(Text("asd")),Li()]))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ul(Li(Text("asd"))))])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ul(Li(Text("asas"))))])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ol([Li(Text("asd")),Li(),Li()]))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ol([Li(Text("asd")),Li()]))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ol(Li(Text("asd"))))])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Ol(Li(Text("asas"))))])).is_valid()) == True
        # Check P
        assert (Page(P()).is_valid()) == True
        assert (Page(P( Text() )).is_valid()) == True
        assert (Page(P(Text('akdjash'))).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Div(P()))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Div(Span(P())))])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Div(Span(P(Text()))))])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Div(Span(P(Text('asas')))))])).is_valid()) == True
        # Check Span
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Span())])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Span( Text("asdasd") ))])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Span([Text("aaa"),P()]))])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Span(Div()))])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body(Span([P(), Div()]))])).is_valid()) == False
        # Check Table
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table() )])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table(Text("aa")) )])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( Div() ) )])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( [Div(), Text("aa")] ) )])).is_valid()) == False

        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( [Div(), Tr(Th(Text("aaa")))] ) )])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( [Tr(Th(Text("aaa"))), Tr(Th(Text("aaa")))] ) )])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( Tr(Th(Text("aaa"))) ) )])).is_valid()) == True

        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( [Div(), Tr(Td(Text("aaa")))] ) )])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( [Tr(Td(Text("aaa"))), Tr(Td(Text("aaa")))] ) )])).is_valid()) == True
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( Tr(Td(Text("aaa"))) ) )])).is_valid()) == True
        # Check Tr
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( Tr() ) )])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( Tr(Div()) ) )])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( Tr([Div(), Text("aa")]) ) )])).is_valid()) == False
        # Check Th, Td
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( Tr( Th(Div()) ) ) )])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( Tr( Th([Div(), Text('aa')]) ) ) )])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( Tr( Th([Text('aa'), Text('aa')]) ) ) )])).is_valid()) == False
        assert (Page(Html([Head(Title(Text('tetetat'))), Body( Table( Tr( Th(Text('aa')) ) ) )])).is_valid()) == True
        # Check doctype
        assert Page(Html([Head(Title(Text('tetetat'))), Body()])).__str__() == "<!DOCTYPE HTML>\n<html>\n  <head>\n    <title>\n      tetetat\n    </title>\n  </head>\n  <body></body>\n</html>"
        assert Page(Head(Title(Text('tetetat')))).__str__() == "<head>\n  <title>\n    tetetat\n  </title>\n</head>"
    except:
        print("test failed")
    else:
        print("test success")