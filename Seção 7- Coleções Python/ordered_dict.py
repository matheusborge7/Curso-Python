"""
Módulo Collections: Ordered Dict

# Em um dicionário, a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
   print(f'chave={chave}:valor={valor}')

OrderedDict -> É um diconário, que nos garante a ordem de inserção dos elementos.
# Fazendo Import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
    
"""
from collections import OrderedDict
# Entendo a difrença ente Dict e OrderedDIct

# Dicionários comuns

dict1 = {'a': 1, 'b':2}
dict2 = {'b':2, 'a': 1}

print(dict1 ==dict2) # True -> Já que a ordem dos elmentos não importa ára o diconario

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b':2})
odict2 = OrderedDict({'b': 2, 'a':1})

print(odict1 == odict2) # False -> Já que a ordem dos elementos importa para o OrderedDict