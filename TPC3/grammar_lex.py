#!/usr/bin/env python3

import ply.lex as lex
import sys

tokens = "AREAS NOTA CONCEITO LING OPEN CLOSE CAT REG AREA VAR SG NL BR PT ES GA EN TEXT COLON SLASH POP CULT SWE SYN INDEX".split(" ")

states = (
    ('TAG', 'inclusive'),
    ('TAGCONT', 'inclusive')
)


# Reserved words

def t_SLASH(t):
    r'\|'
    return t

def t_POP(t):
    r'\(pop\)'
    return t

def t_CULT(t):
    r'\(cult\)'

def t_BR(t):
    r'\(br\)'
    return t

def t_SWE(t):
    r'\(swe\)'
    return t

def t_PT(t):
    r'\(pt\)'
    return t

def t_ES(t):
    r'\(es\)'
    return t

def t_GA(t):
    r'\(ga\)'
    return t

def t_EN(t):
    r'\(en\)'
    return t

def t_NL(t):
    r'\n'
    return t

def t_AREAS(t):
    r'Areas:'
    return t

def t_INDEX(t):
    r'Indice:'
    return t

def t_LING(t):
    r'Ling:'
    return t

def t_OPEN(t):
    r'\('
    t.lexer.push_state('TAG')
    return t

def t_COLON(t):
    r':'
    return t

def t_TAG_CAT(t):
    r'cat'
    t.lexer.push_state('TAGCONT')
    return t

def t_TAG_REG(t):
    r'reg'
    t.lexer.push_state('TAGCONT')
    return t
def t_TAG_AREA(t):
    r'area'
    t.lexer.push_state('TAGCONT')
    return t
def t_TAG_VAR(t):
    r'var'
    t.lexer.push_state('TAGCONT')
    return t

def t_TAG_SYN(t):
    r'syn'
    t.lexer.push_state('TAGCONT')
    return t

def t_TAG_SG(t):
    r'sg'
    t.lexer.push_state('TAGCONT')
    return t

def t_TAG_NOTA(t):
    r'nota'
    t.lexer.push_state('TAGCONT')
    return t

def t_TAG_CONCEITO(t):
    r'conceito'
    t.lexer.push_state('TAGCONT')
    return t

def t_TAGCONT_POP(t):
    r'\(pop\)'
    return t

def t_TAGCONT_CULT(t):
    r'\(cult\)'

def t_TAGCONT_BR(t):
    r'\(br\)'
    return t

def t_TAGCONT_SWE(t):
    r'\(swe\)'
    return t

def t_TAGCONT_PT(t):
    r'\(pt\)'
    return t

def t_TAGCONT_ES(t):
    r'\(es\)'
    return t

def t_TAGCONT_GA(t):
    r'\(ga\)'
    return t

def t_TAGCONT_EN(t):
    r'\(en\)'
    return t

def t_TAGCONT_CLOSE(t):
    r'\)'
    t.lexer.pop_state()
    t.lexer.pop_state()
    return t

def t_TAGCONT_TEXT(t):
    r'[^)]+'
    return t

def t_TEXT(t):
    r'[^|\n]+'
    return t

t_ignore = " \t"

def t_error(t):
    print('Caráter inválido', t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


#file = open(sys.argv[1], "r")
#program = file.read()
#lexer.input(program)
#
#for to in lexer:
#    print(to)
#lexer.input(sys.stdin.read())
#for to in lexer:
#    print(to)
#for linha in sys.stdin:
#    lexer.input(linha)
#    for to in lexer:
#        print(to)
