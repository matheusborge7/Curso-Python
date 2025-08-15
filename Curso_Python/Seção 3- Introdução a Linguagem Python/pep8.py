"""PEP8- Python Enhacement Proposal

São propostas de melhorias para a linguagem Python.

The Zen of Python

import this

A idéia da PeP8 é ue possamos escrever códigos Python de foma Pythonica

[1] - Utilize CamelCase para nomes de classes;
"""


"""Se nome for simples, a inicial é maiuscula, se for composto, a primeira letra de cada palavra é maiúscula"


class Calculadora 
pass

class CalculadoraCientifica:
    pass
"""
"""[2] Utilize nomes em minusculos, separados por underline para funções e variáveis

def soma():
    pass


def soma_dois():
    pass

numero = 4

numero_impar = 5"""

"""[3]-Utilize uatros espaços para identação!

if 'a' in 'banana':
    print('Tem a letra a na palavra banana')
    """
"""[4] - Linhas em Brancos
-Separar funções e defibições de classes com duas linhas em branco
-Métodos dentro de uma classe devem ser separados por uma linha em branco
    class Classe:
    pass


    class outraClasse:
    pass
"""

"""[5] - Imports

- Imports devem ser feitos em linhas separadas;

# Import Errado

import os, sys

# Import Correto

import os
import sys

# Não há problemas em utlizar:

from types import StringType, ListType

#Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType
    Outrotype
)

#Impots devem ser colocados no topo do arquivo, logo após de quaisuer comentário ou docstring, e antes de consatantes ou variáveis globais.

[6] - Espaços em expressões e instruções

# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:
funcao(algo[1], {outro: 2})

# Não faça:
algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = lista [ indice]

# Faça:

dict['chave'] = lista[indice]

#não faça:

x                         = 1
y                         = 2
variavel longa            = 5

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Temine sempe uma instrução com uma nova linha
"""
import this
