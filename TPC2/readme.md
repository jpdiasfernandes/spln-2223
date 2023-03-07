
# Table of Contents

1.  [Resumo](#orgbcec4b3)
2.  [Lex](#org04090de)
3.  [Yacc](#orge2fbd7d)
    1.  [Gramática (representação macro)](#org46a1f26)
4.  [Exemplo](#org3b1b813)
5.  [Trabalho futuro](#orgef7a8de)



<a id="orgbcec4b3"></a>

# Resumo

-   Neste TPC o objetivo era a criação de um dicionário que não fosse refém a uma só linguagem e que facilmente se expandisse para outras.
-   Para tal, não poderiam haver entradas numa só linguagem. No entanto, é de salientar que se adicionou, a cada entrada uma lista de áreas às quais ela pertence. Estas áreas podem no futuro vir a ser índices para entradas que representam informação dessa área. No teste apresentado representam a área em extenso.

-   No caso de se querer adicionar mais campos a solução é fácil devido a uma boa combinação entre simplicidade e açúcar sintático. Todos os atributos seguem o mesmo formato. A adição de linguagens é também muito fácil. Os elementos de uma entrada seguem também todos o mesmo formato, sendo que a criação de um novo elemento execuível.

-   Por fim,  disponibiliza-se duas versões de teste, uma que segue a gramática e outra que apresenta erros sintáticos.


<a id="org04090de"></a>

# Lex

-   Para a deteção de tokens foram utilizados três estados: INITIAL, TAG e TAGCONT. Era necessário a criação de estados para generalizar a criação de atributos. Assim era possível ter &ldquo;palavras reservadas&rdquo; num determinado estado, permitindo a utilização de palavras chave fáceis de escrever mas que correspondem a um Token necessário de capturar.
-   O espaço e o tab foram ignorados, sendo que o New line é fundamental para a gramática


<a id="orge2fbd7d"></a>

# Yacc

-   A estrutura da gramática é baseada numa lista de entradas


<a id="org46a1f26"></a>

## Gramática (representação macro)

    Dic -> Entrada*
    Entrada -> NL* Indice Areas Linguas
    Indice -> INDEX Conteudo NL
    Areas -> AREAS Area* NL
    Linguas -> LING NL Ling*
    Area -> OPEN AREA Cont CLOSE
    Ling -> LingCont ':' TEXT '|' ListAtrib NL


<a id="org3b1b813"></a>

# Exemplo

    Indice: e3
    Areas: (area financeira) (area credito)
    Ling:
        (swe): fordran | (syn krav) (syn ansprak)
        (en): claim | (syn demand) (syn requirement)
        (pt): cobrança | (nota ato ou feito de cobrar ou receber quaisquer dívidas ou donativos) (syn coleta de quantias)
        (es): cobro


<a id="orgef7a8de"></a>

# Trabalho futuro

1.  Uma vez que a quantidade de atributos era pequena era possível ter adicionado todos os atributos hardcoded na gramática. Seria possível generalizar este processo reconhecendo todos os atributos como um único Token e depois, por exemplo, numa construção de uma árvore sintática abstrata atribuir qual o atributo ao certo.
2.  Outro aspeto fundamental é a deteção de erros. É necessário contabilizar o número de linhas para ser possível fazer um debug  melhor de erros
3.  Por fim, poderia-se criar uma lista de conteudos com o mesmo atributo. Desta forma evitava-se escrever sempre o mesmo atributo vezes sem conta

