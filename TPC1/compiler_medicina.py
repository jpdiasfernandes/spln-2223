#!/usr/bin/env python3

import re
import ply.lex as lex
import sys
import json

tokens = "EC AREA SIN ES EN PT NOTA ER LANGCONT ERCONT NL".split(" ")

dic = {}
states = (
    ('area', 'inclusive'),
    ('lang', 'inclusive'),
    ('er', 'inclusive'),
    #('en', 'exclusive'),
    #('pt', 'exclusive'),
    #('er', 'exclusive')
)
def t_EC(t):
    r'<text .*>.*<b>(\s*\w+\s+.+)</b>.*</text>'
    t.lexer.count += 1
    t.lexer.cur_er = 0
    m_obj = t.lexer.lexmatch
    ec = m_obj.group(2)
    #print("")
    #print(ec)
    number = re.match("\d+", ec)
    if number != None:
        t.lexer.cur = int(number[0])
    else:
        t.lexer.cur += 1
    number = t.lexer.cur

    t.lexer.dict[number] = {}

    t.lexer.begin('area')

def t_area_AREA(t):
    r'<text .*height="\d+" .*>.*<i>(.*)</i>.*</text>'
    m_obj = t.lexer.lexmatch
    area = m_obj.group(2)
    #print(area)
    t.lexer.area += 1
    t.lexer.begin('INITIAL')
    cur = t.lexer.cur
    t.lexer.dict[cur]["area"] = area

def t_SIN(t):
    r'<text .*>.*(SIN\.-.*)</text>'
    m_obj = t.lexer.lexmatch
    sin = m_obj.group(4)
    t.lexer.sin += 1
    cur = t.lexer.cur
    t.lexer.dict[cur]["sin"] = sin
    #print(sin)

def t_lang_LANGCONT(t):
    r'<text .*>.*<i>(.*)</i>.*</text>'
    m_obj = t.lexer.lexmatch
    cont = m_obj.group(2)
    cur = t.lexer.cur
    language = t.lexer.cur_lang
    t.lexer.dict[cur][language] = cont
    #print(cont)
    t.lexer.begin('INITIAL')


def t_ES(t):
    r'<text .*>.*\s(es)\s.*</text>'
    m_obj = t.lexer.lexmatch
    es = m_obj.group(6)
    t.lexer.begin('lang')

    cur = t.lexer.cur
    t.lexer.cur_lang = "es"

    t.lexer.es += 1
    #print(es, end=" ")

def t_PT(t):
    r'<text .*>.*\s(pt)\s.*</text>'
    m_obj = t.lexer.lexmatch
    pt = m_obj.group(8)
    t.lexer.begin('lang')
    t.lexer.pt += 1

    cur = t.lexer.cur
    t.lexer.cur_lang = "pt"

    #print(pt, end=" ")

def t_EN(t):
    r'<text .*>.*\s(en)\s.*</text>'
    m_obj = t.lexer.lexmatch
    en = m_obj.group(10)
    t.lexer.begin('lang')
    t.lexer.en += 1

    cur = t.lexer.cur
    t.lexer.cur_lang = "en"

    #print(en, end=" ")

def t_LA(t):
    r'<text .*>.*\s(la)\s.*</text>'
    m_obj = t.lexer.lexmatch
    la = m_obj.group(12)
    t.lexer.begin('lang')
    t.lexer.la += 1

    cur = t.lexer.cur
    t.lexer.cur_lang = "la"

    #print(la, end=" ")

def t_ER(t):
    r'<text .*>.*<b>(\s+\w+.*)</b>.*</text>'
    m_obj = t.lexer.lexmatch
    er = m_obj.group(14)
    t.lexer.begin('er')
    #print(er)

    cur = t.lexer.cur
    t.lexer.cur_er_name = er
    if t.lexer.cur_er == 0:
        t.lexer.dict[cur]["ER"] = []
    t.lexer.er += 1

def t_er_ERCONT(t):
    r'<text .*>.*(Vid.-.*)</text>'
    m_obj = t.lexer.lexmatch
    er_cont = m_obj.group(2)
    t.lexer.begin('INITIAL')
    #print(er_cont)
    t.lexer.er_cont += 1
    cur = t.lexer.cur
    er_name = t.lexer.cur_er_name
    t.lexer.dict[cur]["ER"].append({er_name : er_cont})

def t_NOTA(t):
    r'<text .*>\s*(Nota\.-.*)</text>'
    m_obj = t.lexer.lexmatch
    nota = m_obj.group(16)

    cur = t.lexer.cur
    #print(nota)
    t.lexer.dict[cur]["nota"] = nota

def t_area_default(t):
    r'(.|\n)'
    pass
def t_default(t):
    r'(.|\n)'
    pass

def t_error(t):
    r'.'
    t.lexer.skip(1)

def t_eof(t):
    #print(t.lexer.count)
    json_object = json.dumps(t.lexer.dict, indent=4, ensure_ascii=False)
    print(json_object)


ex = open(sys.argv[1], "r")
proc = lex.lex()
proc.input(ex.read())

proc.count = 0
proc.area = 0
proc.sin = 0
proc.es = 0
proc.en = 0
proc.pt = 0
proc.la = 0
proc.er = 0
proc.er_cont = 0
proc.dict = {}
proc.cur = None
proc.last = None
proc.cur_lang = None
proc.cur_er = 0
proc.cur_er_name = None

res = proc.token()
