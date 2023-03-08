#!/usr/bin/env python3
from enum import Enum

class Dic:
    def __init__(self, entradas=[]):
        self.entradas = entradas

    def showDic(self):
        print(">>> Dicionário <<<")
        for entrada in self.entradas:
            entrada.showEntrada()



class Entrada:
    def __init__(self, index, areas, linguas):
        self.index = index
        self.areas = areas
        self.linguas = linguas

    def showEntrada(self):
        self.index.showIndex()
        print("> Areas : " , end=" ")
        for area in self.areas:
            area.showTag()
        print("")
        print("> Linguas : ")
        for ling in self.linguas:
            ling.showLing()

class Tag:
    def __init__(self, atrib, conteudo):
        self.atrib = atrib
        self.conteudo = conteudo

    def showTag(self):
        print("(ATRIB: " + str(self.atrib) , end=" ")
        self.conteudo.showCont()
        print(")", end=" ")

class Lingua:
    def __init__(self, idioma, definicao, atribs=[]):
        self.idioma = idioma
        self.definicao = definicao
        self.atribs = atribs

    def showLing(self):
        print(str(self.idioma), end=" ")
        string = ": " + self.definicao
        if len(self.atribs) > 0:
            string += " | "
            print(string, end=" ")
            for atrib in self.atribs:
                atrib.showTag()
        else:
            print(string, end=" ")
        print("")


class Indice:
    def __init__(self, index):
        self.index = index

    def showIndex(self):
        print("> Index: " + self.index)

class Cont:
    def __init__(self, tipo,conteudo):
        self.tipo = tipo
        self.conteudo = conteudo

    def showCont(self):
        print(self.conteudo,end="")

class LingCont:
    def __init__(self, idioma):
        self.idioma = idioma

    def showLingCont(self):
        print(str(self.idioma), end="")

class ContType(Enum):
    POP = 1
    CULT = 2
    TEXT = 3

class Idioma(Enum):
    PT = 1
    BR = 2
    GA = 3
    ES = 4
    EN = 5
    SWE = 6

class AtribType(Enum):
    CAT = 1
    REG = 2
    VAR = 3
    SYN = 4
    SG = 5
    NOTA = 6
    CONCEITO = 7
    AREA = 8
