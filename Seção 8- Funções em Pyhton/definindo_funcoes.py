"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas:
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para excutar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza varias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Ja utilizamos várias funções desde que inciamos este curso:
- print()
-len()
-max()
-min()
-count()
- e muitas outras();
"""

# Exemplo de utilização de funções:

#cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Buil-in) do Pyhton print()

# print(cores)

# curso = 'Programação em Pyhton: Essencial'

# print(curso)

# cores.append('roxo')

# print(cores)

# curso.append('Mais dados.....') # AtributeError
# print(curso)

# cores.clear()
# print(cores)

# print(help(print))

# DRY - Dont't repeat yourself - Não repita você mesmo/ Não repita seu código.

# Mas então, como definir funções?

"""
Em Pyhton a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada): 
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por undeline(Snake case)
parametros_de_entrada -> Opicionais, onde tendo mais de um, cada um separado por virgula, podendo ser opicionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece;
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função utilizamos a palavra reservada 'def'informando
ao Pyhton estamos definindo uma função.Também abrimos o bloco de código com o ja conhecido dois pontos: que é
utilizado em Pyhton para definir blocos.
"""

# Definindo a primeira função 

#def diz_oi():
    #print('oi!')

"""
OBS:

1 - Veja que dentro das nossas funções podemos utilizar outras funções:
2- Veja que nossa função só executa uma tarefa, ou seja, a unica coisa que ela faz é dizer oi;
3- Veja que esta função nao receber nenhum parametro de entrada;
4 - Veja que esta função na retorna nada;
"""

# Utilizando funções

# Chamada de execução
# diz_oi()

"""
ATENÇÂO:

Nunca esqueça de utilizar o parênteses ao executar uma função.

# Errado!
diz_oi

# Certo
diz_oi()

# Errado
diz_oi ()
"""

# Exemplo 2

def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas Felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

cantar_parabens()
cantar_parabens()
cantar_parabens()
cantar_parabens()

for n in range(5):
    cantar_parabens()