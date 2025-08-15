"""
Dicionários

OBS: Em algumas lingagens de programação os dicionarios python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

OBS: Sobre dicionarios
     - Chave e valor são separados por dois pontos 'chave:valor;
     - Tanto chave quanto valor podem ser de qualquer tipo de dado;
     - Podemos misturar tipos de dados;

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai' }

print(paises)
print(type(paises))

# Forma 2(Menos Comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai' }

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])