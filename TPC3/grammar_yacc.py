#!/usr/bin/env python3
import ply.yacc as yacc
from grammar_lex import tokens
import sys
import tree

def p_Dic(p):
    "Dic : ListEnt"
    p[0] = tree.Dic(p[1])

def p_ListEnt(p):
    "ListEnt : ListEnt Entrada"
    p[0] = p[1] + [p[2]]

def p_DicOne(p):
    "ListEnt : Entrada"
    p[0] = [p[1]]

def p_Entrada(p):
    "Entrada : ListNL Indice Areas Linguas"
    p[0] = tree.Entrada(p[2], p[3], p[4])

def p_ListNL(p):
    "ListNL : ListNL NL"
    pass

def p_ListNLEmpty(p):
    "ListNL : "
    pass

def p_Indice(p):
    "Indice : INDEX TEXT NL"
    p[0] = tree.Indice(p[2])


def p_Areas(p):
    "Areas : AREAS ListArea NL"
    p[0] = p[2]

def p_ListArea(p):
    "ListArea : ListArea Area"
    p[0] = p[1] + [p[2]]

def p_ListAreaEmpty(p):
    "ListArea : "
    p[0] = []

def p_Area(p):
    "Area : OPEN AREA Cont CLOSE"
    p[0] = tree.Tag(tree.AtribType.AREA, p[3])

def p_ContText(p):
    "Cont : TEXT"
    p[0] = tree.Cont(tree.ContType.TEXT, str(p[1]))

def p_ContPop(p):
    "Cont : POP"
    p[0] = tree.Cont(tree.ContType.POP, str(p[1]))

def p_ContCult(p):
    "Cont : CULT"
    p[0] = tree.Cont(tree.ContType.CULT, str(p[1]))

def p_ContLing(p):
    "Cont : LingCont"
    p[0] = tree.LingCont(p[1])

def p_LingContBR(p):
    "LingCont : BR"
    p[0] = tree.Idioma.BR

def p_LingContSWE(p):
    "LingCont : SWE"
    p[0] = tree.Idioma.SWE

def p_LingContPT(p):
    "LingCont : PT"
    p[0] = tree.Idioma.PT

def p_LingContES(p):
    "LingCont : ES"
    p[0] = tree.Idioma.ES

def p_LingContGA(p):
    "LingCont : GA"
    p[0] = tree.Idioma.GA

def p_LingContEN(p):
    "LingCont : EN"
    p[0] = tree.Idioma.EN

def p_Linguas(p):
    "Linguas : LING NL ListLing"
    p[0] = p[3]


def p_ListLing(p):
    "ListLing : ListLing Ling"
    p[0] = p[1] + [p[2]]

def p_ListLingOne(p):
    "ListLing : Ling"
    p[0] = [p[1]]

def p_Ling(p):
    "Ling : LingCont COLON TEXT SLASH ListAtrib NL"
    p[0] = tree.Lingua(p[1], str(p[3]), p[5])

def p_LingOne(p):
    "Ling : LingCont COLON TEXT NL"
    p[0] = tree.Lingua(p[1], str(p[3]))

def p_ListAtrib(p):
    "ListAtrib : ListAtrib Tag"
    p[0] = p[1] + [p[2]]

def p_ListAtribOne(p):
    "ListAtrib : Tag"
    p[0] = [p[1]]

def p_Tag(p):
    "Tag : OPEN Atrib Cont CLOSE"
    p[0] = tree.Tag(p[2], p[3])

def p_AtribCat(p):
    "Atrib : CAT"
    p[0] = tree.AtribType.CAT


def p_AtribReg(p):
    "Atrib : REG"
    p[0] = tree.AtribType.REG

def p_AtribVar(p):
    "Atrib : VAR"
    p[0] = tree.AtribType.VAR

def p_AtribSyn(p):
    "Atrib : SYN"
    p[0] = tree.AtribType.SYN

def p_AtribSg(p):
    "Atrib : SG"
    p[0] = tree.AtribType.SG

def p_AtribNota(p):
    "Atrib : NOTA"
    p[0] = tree.AtribType.NOTA

def p_AtribConceito(p):
    "Atrib : CONCEITO"
    p[0] = tree.AtribType.CONCEITO

def p_error(p):
    parser.success = False
    if p is not None:
        print ("Line %s, illegal token %s" % (p.lineno, p.value))
    else:
        print('Unexpected end of input')

parser = yacc.yacc()

parser.success = True
file = open(sys.argv[1], "r")
program = file.read()
result = parser.parse(program)

result.showDic()
print(parser.success)
