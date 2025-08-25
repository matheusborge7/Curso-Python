"""
Módulo Collections - Default Dict

dicionario = {'curso': 'Programação em Pyhton: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # ??? KeyError

Default Dict -> Ao criar um dicionario utilizando-o, nós informaos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre uque não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será 
criada e o valor default será atribuido.

OBS: Lambdas são funções sem nome, que pode ou não receber parâmetros de entrada e 
retornar valores.
"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programção em Pyrhon: Essencial'

print(dicionario)

print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não.

print(dicionario)