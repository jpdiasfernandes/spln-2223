#!/usr/bin/env python3
"TPC para SPLN 2022/2023"
import sys
import fileinput
import re
import argparse
import json
from tokenizador.abbr_helpers import jsonFromAbr

def main():
    parser = argparse.ArgumentParser(
        prog= 'Tokenizor',
        description= 'Tokenize a file given as input',
        epilog= 'Made by José Pedro Fernandes'
    )


    parser.add_argument('--files', '-f', help="Define the files that are going to be tokenized", default=None,required=False, nargs="*")
    parser.add_argument('--chapter', '-cap', help="Define the regex for a Chapter", required=False)
    parser.add_argument('--pagebreak', '-pb', help="Define the regex for a page break", required=False)
    parser.add_argument('--output', '-o', help="Define the output files to be written. The output files will map to the same order of input files. If number of output files is less than the number of input files then the other files will be written to the stdin.", required=False, nargs="*")
    parser.add_argument('--append', '-a', help="Define if the output is supposed to be appended", required=False, action='store_true')
    parser.add_argument('--abbreviations', '-abbr', help="Define the path to a json with a json that maps the regex of the abbreviation with the token wanted.", required=False)
    parser.add_argument('--lang', '-l', help="Define the language of abbreviations to use", required=False)
    args = parser.parse_args()

    files_path = []
    cap = r'(CAP[IÍ]TULO +(\w+)).*?\n(.*?)\n\n'
    pagbreak = r'\n\n'
    output_files = []
    append = args.append
    lang = "pt"
    abbreviations = {}

    abbrev_path = None
    try:
        if args.files != None:
            files_path = args.files
        if args.chapter != None:
            cap = args.chapter
        if args.pagebreak != None:
            pagbreak = args.pagebreak
        if args.output != None:
            output_files = args.output
        if args.abbreviations != None:
            abbrev_path = args.abbreviations
        if args.lang != None:
            lang = args.lang

    except:
        print("[Usage: Tokenizer]\n")
        exit()

    if abbrev_path:
        f = open(abbrev_path, "r")
        abbreviations = json.load(f)
        f.close()

    jsonFromAbr(lang)
    abbreviations.update(jsonFromAbr(lang))



    #regex_cap = r'.*(CAP[IÍ]TULO +(\w+)).*?\n(.*?)\n\n'
    regex_cap = r'.*?{}'.format(cap)
    #regex_emptyLine = r'([a-z0-9,;–])\n\n([a-z0-9])'
    regex_emptyLine = r'([a-z0-9,;–]){}([a-z0-9])'.format(pagbreak)
    #regex_poema = r'<poema>(.*?)</poema>'
    regex_poema = r'<poema>(.*?)</poema>'
    #regex_pontuacao_depois = r'(\w+)([,;.?!\"“”–]+)'
    regex_pontuacao_depois = r'(\w+)([,;.?!\"“”–]+)'
    #regex_pontuacao_antes = r'([,–;.?!\"“”]+)(\w+)'
    regex_pontuacao_antes = r'([,–;.?!\"“”]+)(\w+)'
    #regex_frase = r'([A-Z])((.|\n)*?)(#FP#)'
    regex_frase = r'([A-Z])((.|\n)*?)(#(FP|E|Q)#)'
    #regex_fraseline = r'([A-Z])(.*?)(#FP#)'
    regex_fraseline = r'([A-Z])(.*?)(#(FP|E|Q)#)'




    # 0. Quebras de página X
    # 1. separar pontuação das palavras X
    # 2. Marcar capítulos X
    # 3. Separar paragrafos de linhas pequenas
    # 4. Juntar linhas da mesma frase X
    # 5. Uma frase por linha X

    def out(text, path=None):
        if path != None:
            f = open(path, "w")
        else:
            f = sys.stdout
        f.write(text)
        f.close()

    def tokenize(text):
        # Substitui um Capitulo por um Token CAP
        text = re.sub(regex_cap, r"#CAP\2#\3#", text)

        # Substitui uma quebra de página por um Token PAGBREAK
        text = re.sub(regex_emptyLine, r"\1#PAGBREAK#\2", text)

        def abrev(a):
            lower = a[0].lower()
            if lower in abbreviations.keys():
                return "#A#" + abbreviations[lower] + "#"
            return a[0]

        regex_abrev = r'\w+\.'
        text = re.sub(regex_abrev, abrev, text)

        poemas = []
        def guarda_poema(poema):
            poemas.append(poema[1])
            return ">>poema" + str(len(poemas)) +"<<"


        text = re.sub(regex_poema, guarda_poema, text, flags=re.S)

        text = re.sub(regex_pontuacao_depois, r'\1 \2', text)

        text = re.sub(regex_pontuacao_antes, r'\1 \2', text)

        regex_threepoints = r'\.\.\.'
        # replace fullstop to FP and ... to Three points
        text = re.sub(regex_threepoints, r'#ETC#', text)

        regex_fullstop = r'\.'
        text = re.sub(regex_fullstop, r'#FP#', text)

        regex_question = r'\?'

        text = re.sub(regex_question, r'#Q#', text)

        regex_exclamation = r'\!'
        text = re.sub(regex_exclamation, r'#E#', text)

        def frase(f):
            t = re.sub(r'#CAP\w+#(.*?)#', r'', f[2], flags=re.S)
            t = re.sub(r'\n', r'', t, flags=re.S)

            return f[1] + t + f[4]


        text = re.sub(regex_frase, frase, text, flags=re.S)

        text = re.sub(regex_fraseline, r'\1\2\3\n', text)
        return text
    #print(text)
    #print(re.findall(regex_frase, text))
    #text = re.sub(regex_frase, r'#\1 \2.', text, flags=re.S)


    texts = []
    myinput = fileinput.FileInput(files=files_path)
    text = ""
    first = True
    with myinput as input:
        for line in input:
            if input.isfirstline() and not first:
                text = tokenize(text)
                texts.append(text)
                if not append:
                    if len(output_files) == 0:
                        out(texts[-1])
                    else:
                        out(texts[-1], output_files.pop(0))
                text = ""
            text += line
            first = False


        text = tokenize(text)
        texts.append(text)

        text_final = ""
        if not append:
            text_final = texts[-1]
        else:
            for t in texts:
                text_final += t


        if len(output_files) == 0:
            out(text_final)
        else:
            out(text_final, output_files.pop(0))


