#!/usr/bin/env python3
import tree
import sys

def atribHtml(a):
    "Converts an Atribute ENUM to html string"
    return a.name

def contHtml(c):
    "Converts a Cont objecto to html string"
    if c.tipo == tree.ContType.TEXT:
        return c.conteudo
    elif c.tipo == tree.ContType.POP:
        return "POP."
    elif c.tipo == tree.ContType.CULT:
        return "CULT."

def tagHtml(t):
    "Converts a Tag object to html string"
    return "<i> " + atribHtml(t.atrib) + " </i> : " + contHtml(t.conteudo)

def linguaHtml(l):
    "Converts a Lingua object to html string"
    res = f'''
        <b> {l.idioma.name} </b> | {l.definicao}
        <ul>
    '''

    for atrib in l.atribs:
        res += "<li> " + tagHtml(atrib) + " </li>"

    res += '''
        </ul>
    '''

    return res

def areaHtml(a):
    "Converts a Tag object but with area syntax string"
    return contHtml(a.conteudo)
def entradaHtml(e):
    "Converts a Entrada object to html string"
    res = f'''
        <h2> Índice {e.index.index} </h2>
    '''

    res += '''
        <h2> Áreas </h2>
        <ul>
    '''

    for area in e.areas:
        res += "<li> " + areaHtml(area) + " </li>"

    res += '''
        </ul>
    '''

    res += '''
        <h2> Informação nas várias linguagens </h2>
        <ul>
    '''

    for lingua in e.linguas:
        res += linguaHtml(lingua)

    res += '''
        </ul>
    '''
    return res



class HTML:
    def __init__(self, dicTree):
        self.tree = dicTree
        # Initializes self.layout and self.layoutClose
        self.makeLayout()
        self.toHtml()


    def toHtml(self):
        self.page = self.layout
        #Body here

        self.page += '''
            <h1> Dicionário </h1>
        '''

        for entrada in self.tree.entradas:
            self.page += entradaHtml(entrada)
            self.page += '''
            <hr>
            '''

        self.page += self.layoutClose

    def flush(self, target=None):
        if target:
            file = open(target, "w")
        else:
            file = sys.stdout

        file.write(self.page)

        if target:
            file.close()


    def makeLayout(self):
        self.layout = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>Dicionário de conteúdos</title>
    </head>
    <body>
        '''

        self.layoutClose = '''
    </body>
        '''
