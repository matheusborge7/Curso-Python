"""
Escopo de variáveis

Dois casos de escopo:

1. Variáveis globais: Variáveis que são criadas fora de qualquer função, ou seja, no nível mais alto do
    - Variaveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2. Variáveis locais: Variáveis que são criadas dentro de uma função e só podem ser usadas dentro dessa função.
    - Variáveis locais só são reconhecidas dentro do bloco onde foram declaradas, ou seja, seu escopo é limitado ao bloco onde foram declaradas.

 Para declarar variaveis em Python, fazemos:

 nome_variavel = valor_da_variavel   

 Python é uma lingueagem de tipo dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dado dela.
 Este tipo é inferido ao atribuirmos o valor á mesma.

 Exemplo em C:
 int numero=42;

 Exemplo em Java:
 int numero=42;
 """

numero = 42 # Variável global
print (numero)
print(type(numero))

numero = 'Geek'
print (numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)

numero= 42
novo =0

if numero > 10:
    novo = numero + 10 # A variável novo esta declarada dentro do bloco if, mas como o bloco if é um bloco de código, ela é considerada uma variável local.
    print(novo)

print(novo)  