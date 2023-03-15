#!/usr/bin/env python3

import sys
import fileinput
import re

text = ""

for line in fileinput.input():
    text += line

# 0. Quebras de página X
# 1. separar pontuação das palavras X
# 2. Marcar capítulos X
# 3. Separar paragrafos de linhas pequenas
# 4. Juntar linhas da mesma frase X
# 5. Uma frase por linha X

regex_cap = r'.*(CAP[IÍ]TULO +(\w+)).*?\n(.*?)\n\n'

regex_nl = r'([a-z0-9,;–])\n\n([a-z0-9])'

text = re.sub(regex_cap, r"#CAP\2#\3#", text)
text = re.sub(regex_nl, r"\1=\n\2", text)

regex_poema = r'<poema>(.*?)</poema>'

abreviaturas = {
    "Sra." : "SRA",
    "Sr." : "SR"
}

def abrev(a):
    if a[0] in abreviaturas.keys():
        return abreviaturas[a[0]]
    return a[0]

regex_abrev = r'\w+\.'
text = re.sub(regex_abrev, abrev, text)

poemas = []
def guarda_poema(poema):
    poemas.append(poema[1])
    return ">>poema" + str(len(poemas)) +"<<"


text = re.sub(regex_poema, guarda_poema, text, flags=re.S)

regex_pontuacao_depois = r'(\w+)([,;.?!\"“”–]+)'
text = re.sub(regex_pontuacao_depois, r'\1 \2', text)

regex_pontuacao_antes = r'([,–;.?!\"“”]+)(\w+)'
text = re.sub(regex_pontuacao_antes, r'\1 \2', text)

regex_threepoints = r'\.\.\.'
# replace fullstop to FP and ... to Three points
text = re.sub(regex_threepoints, r'#ETC#', text)

regex_fullstop = r'\.'
text = re.sub(regex_fullstop, r'#FP#', text)


def frase(f):
    t = re.sub(r'#CAP\w+#(.*?)#', r'', f[2], flags=re.S)
    t = re.sub(r'\n', r'', t, flags=re.S)

    return f[1] + t + f[4]

regex_frase = r'([A-Z])((.|\n)*?)(#FP#)'

text = re.sub(regex_frase, frase, text, flags=re.S)

regex_fraseline = r'([A-Z])(.*?)(#FP#)'
text = re.sub(regex_fraseline, r'\1\2\3\n', text)
print(text)
#print(re.findall(regex_frase, text))
#text = re.sub(regex_frase, r'#\1 \2.', text, flags=re.S)




#print(text)
