
# Table of Contents

1.  [Objetivo](#org300bd8b)
2.  [Argparser](#org3b0f028)



<a id="org300bd8b"></a>

# Objetivo

-   O objetivo deste TPC era a criação de um package python que recebesse como input ficheiros textos e fosse capaz de os tokenizar. Passando como argumento alguns regex costumizados transformá-los em tokens que iriam aparecer no texto final.
-   Por fim era ainda objetivo a disponibilização do módulo feito num repositório como o pypi ou o testpypi
-   Era ainda possível adicionar tokens costumizáveis com o argumento &#x2013;abbreviations, sendo estas definidas em formato json


<a id="org3b0f028"></a>

# Argparser

    usage: Tokenizor [-h] [--files [FILES ...]] [--chapter CHAPTER] [--pagebreak PAGEBREAK] [--output [OUTPUT ...]]
                     [--append] [--abbreviations ABBREVIATIONS]
    
    Tokenize a file given as input
    
    options:
      -h, --help            show this help message and exit
      --files [FILES ...], -f [FILES ...]
                            Define the file that is supposed to be tokenized
      --chapter CHAPTER, -cap CHAPTER
                            Define the regex for a Chapter
      --pagebreak PAGEBREAK, -pb PAGEBREAK
                            Define the regex for a page break
      --output [OUTPUT ...], -o [OUTPUT ...]
                            Define the output files to be written. The output files will map to the same order of
                            input files. If number of output files is less than the number of input files then the
                            other files will be written to the stdin.
      --append, -a          Define if the output is supposed to be appended
      --abbreviations ABBREVIATIONS, -abbr ABBREVIATIONS
                            Define the path to a json with a json that maps the regex of the abbreviation with the
                            token wanted.

