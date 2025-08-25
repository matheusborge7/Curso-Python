"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

-Estiver entre aspas simples -> 'uma string', '234', 'True', 'a', '42.3'
-Estiver entre aspas duplas -> "uma string", "234", "True", "a", "42.3"
-Estiver entre aspa simpless triplas -> '''uma string''', '''uma string''', '''234''', '''True''', '''a''', '''42.3'''

nome = 'João'
print(nome)
print (type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome='Angelina" \nJolie'
print(nome)
print(type(nome))

nome= 'Angelina \" Jolie'
print(nome)
print(type(nome))

print(nome.upper())  # Converte para maiúsculas
print(nome.lower())  # Converte para minuscula
print(nome.split())  # Divide a string em uma lista de palavras
print(nome[0:4]) # Pega do índice 0 ao 3/ Slice de string

print(nome[5:15])  # Pega do índice 5 ao 14/ Slice de string

# ['Geek', 'University']
print(nome.split()[0])  # Divide a string em uma lista de palavras])

print(nome.split()[1])  # Divide a string em uma lista de palavras])
print(nome[14], nome[13]) # Pega o índice 14 e o 13
"""
#-Estiver entre aspas duplas triplas -> """ uma string""", """234""", """True""", """a""", """42.3"""

# [ 0,  1,   2,  3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,]
# ['G, 'e', 'e' 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'

"""
[::-1] -> Comece do primeiro elemento [0], vá até o último elemento [-1] e inverta [::-1]"""
print(nome[::-1])  # Inversão da string Pythônico

print(nome.replace('e', 'i'))  # Substitui o 'E' por 'I'

print(type(nome))

texto = 'socorram me subino onibus em marrocos' #Palíndromo
print(texto)

print(texto[::-1])

nome = 'ana'
print(nome)

print(nome[::-1])
