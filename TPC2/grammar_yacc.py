#!/usr/bin/env python3
import ply.yacc as yacc
from grammar_lex import tokens
import sys

def p_Dic(p):
    "Dic : ListEnt"
    pass

def p_ListEnt(p):
    "ListEnt : ListEnt Entrada"
    pass

def p_DicOne(p):
    "ListEnt : Entrada"
    pass

def p_Entrada(p):
    "Entrada : ListNL Areas Linguas"
    pass

def p_ListNL(p):
    "ListNL : ListNL NL"
    pass
def p_ListNLEmpty(p):
    "ListNL : "
    pass


def p_Areas(p):
    "Areas : AREAS ListArea NL"
    pass

def p_ListArea(p):
    "ListArea : ListArea Area"
    pass

def p_ListAreaEmpty(p):
    "ListArea : "
    pass

def p_Area(p):
    "Area : OPEN AREA Cont CLOSE"
    pass

def p_ContText(p):
    "Cont : TEXT"
    pass

def p_ContPop(p):
    "Cont : POP"
    pass

def p_ContCult(p):
    "Cont : CULT"
    pass

def p_ContLing(p):
    "Cont : LingCont"
    pass

def p_LingContBR(p):
    "LingCont : BR"
    pass

def p_LingContSWE(p):
    "LingCont : SWE"
    pass

def p_LingContPT(p):
    "LingCont : PT"
    pass

def p_LingContES(p):
    "LingCont : ES"
    pass

def p_LingContGA(p):
    "LingCont : GA"
    pass

def p_LingContEN(p):
    "LingCont : EN"
    pass

def p_Linguas(p):
    "Linguas : LING NL ListLing"
    pass


def p_ListLing(p):
    "ListLing : ListLing Ling"
    pass

def p_ListLingOne(p):
    "ListLing : Ling"
    pass

def p_Ling(p):
    "Ling : LingCont COLON TEXT SLASH ListAtrib NL"
    pass

def p_LingOne(p):
    "Ling : LingCont COLON TEXT NL"
    pass

def p_ListAtrib(p):
    "ListAtrib : ListAtrib Tag"
    pass

def p_ListAtribOne(p):
    "ListAtrib : Tag"
    pass

def p_Tag(p):
    "Tag : OPEN Atrib Cont CLOSE"

def p_AtribCat(p):
    "Atrib : CAT"
    pass

def p_AtribReg(p):
    "Atrib : REG"
    pass

def p_AtribVar(p):
    "Atrib : VAR"
    pass

def p_AtribSyn(p):
    "Atrib : SYN"
    pass

def p_AtribSg(p):
    "Atrib : SG"
    pass

def p_AtribNota(p):
    "Atrib : NOTA"
    pass

def p_AtribConceito(p):
    "Atrib : CONCEITO"
    pass

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

parser.parse(program)

print(parser.success)
