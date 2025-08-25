"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not; 
Operadores binários:
    - and, or, is

Regras de Funcionamento:

Para o 'and', ambos os valores precisam ser True.
Para o 'or', pelo menos um dos valores precisa ser True.
Para o 'not', inverte o valor booleano, ou seja, True se torna False e vice-versa
Para o 'is', verifica se dois objetos são o mesmo objeto na memória.
"""
ativo = False
logado = False

"""if ativo or logado:
    print("Bem vindo usúario!")
else:
    print("Você precisa ativar sua conta. Por favor,cheque seu e-mail!")
"""
"""# Se não estiver ativo 
if not ativo:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail!")
else:
    print("Bem vindo usuário!")

print(not True)
"""

if ativo:
    print("Bem vindo Usúario")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail!")

# ativo é falso?
print(ativo is True)

