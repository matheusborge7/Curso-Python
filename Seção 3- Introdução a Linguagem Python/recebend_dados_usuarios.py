"""
Recebendo dados do usuário

input () -> Todo dado recebido via input é do tipo string (str)

Em Python, tudo que estiver entre:
- Aspas Simples;
- Aspas Duplas;
- Aspas simples Triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'angelina jolie'
- Aspas duplas -> "angelina jolie"
- Aspas simples triplas -> '''angelina jolie'''
"""
#- Aspas duplas triplas -> """angelina jolie"""

# Entrada de dados do usuário
#print("Digite seu nome: ")
#nome = input() #Input -> Entrada 

nome = input("Qual seu nome? ") 

#Saída de dados
# Exemplo de print 'antigo' 2.x
#print("Seja bem-vindo(a), %s" % nome)

#Exemplo de print "moderno" 3.x
#print('Seja Bem-vindo(a), {}'.format(nome))

#Exemplo de print "mais atual" 3.7
print(f'Seja bem-vindo(a), {nome}')

#print("Digite sua idade: ")
#idade = input() #Input -> Entrada

idade = int (input ("Qual sua idade? "))

#Exemplo de print 'antigo' 2.x
#print("A %s tem %s anos." % (nome, idade))

#Exemplo de print "moderno" 3.x
#print('A {0} tem {1} anos.'.format(nome, idade))

#Exemplo de print "mais atual" 3.7
#print (f'A {nome} tem {idade} anos.')

#Exemplo de print "mais atual" 3.7
print (f'A {nome} tem {idade} anos.')

print(f'O(a) {nome} nasceu em {2025 - (idade)}')
#Processamento

#Saída de dados
print("Seja bem-vindo(a), %s" % nome)