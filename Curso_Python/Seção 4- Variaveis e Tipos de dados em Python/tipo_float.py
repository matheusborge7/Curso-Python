"""
Tipo

Tipo Real, decimal

Casas decimais

OBS: O separador de casas decimais é o ponto (.) e não a vírgula (,)
"""

# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

#Certo do ponto de vista Float
valor = 1.44
print(valor) 
print (type (valor))

#É possível fazer dupla atribuição
valor1, valor2 = 1,44
print(valor1)
print (type(valor1))
print(valor2)
print (type(valor2))

# Podemos converter um pra float um int
"""
OBS: Ao coverter valores inteiros float para inteiros, nós pedemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
    