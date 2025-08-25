"""
Módulo Collections - Named Tuple

# Recap tupla

tupla = (num1=1, num2=2, num3=3)

print(tupla[1])

Named Tule -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e também parametros.
"""

# Importanto

from collections import namedtuple
# Precisamos difinir o nome e parâmetros.

# Forma 1

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 = Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

# cachorro = namedtuple('cachorro', ['idade,' 'raca,' 'nome'])

# Usando

ray = cachorro(idade=2, raca='Rotweiller', nome='Princesa')

print(ray)

# Acessando os dados

# Forma 1

print(ray[0]) # idade
print(ray[1]) # raça
print(ray[2]) # nome

# Forma 2

print(ray.idade) # idade
print(ray.raca) # raça
print(ray.nome) # nome

print(ray.index('Rotweiller'))

print(ray.count('Rotweiller'))