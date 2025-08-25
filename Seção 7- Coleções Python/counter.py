"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Receber um iteravel como parâmetro e cira um objeto do tipo Collections Counter que é parecido com um dicionário,
contendo como chave o elemnto da lista passada como parâmtetro e como valor a quantidade
de ocorrências desse elemento.

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iteravel, aqui usamos uma lista
lista = {1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34}

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 66: 1, 34: 1, 43: 1, 45: 1})

# Veja que para cada elemento da lista, o counter criou uma chave e colocou como valor a quantidade de ocorrencias.

# Exemplo 2
print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""

from collections import Counter

# Exemplo 3

texto = """ Sou Matheus Borges da Silva, formado em Informática para Internet e graduando em Análise e Desenvolvimento de Sistemas pela UNIP (Alphaville). Tenho 19 anos e atuo na área de Tecnologia da Informação com foco em suporte técnico e infraestrutura, aliando conhecimento prático e formação técnica para oferecer soluções eficientes e seguras.
Possuo experiência no atendimento a demandas relacionadas à infraestrutura de TI, incluindo suporte aos usuários na utilização e inicialização de sistemas operacionais, pacote Office, configuração de redes, soluções antivírus e diagnóstico de hardware (memória, SSDs, fontes e nobreaks). Entre as minhas principais atividades estão a formatação e reinstalação de sistemas, reposição de insumos (como toners), organização de equipamentos, liberação de acessos à rede interna e geração de vouchers de internet. Atuo com foco na agilidade, precisão e segurança, sempre contribuindo para a continuidade dos serviços e o bom funcionamento do ambiente tecnológico.
Além da atuação em infraestrutura, tenho conhecimentos em desenvolvimento web, programação orientada a objetos, bancos de dados e boas práticas de codificação. Sou comprometido, proativo e tenho facilidade em aprender novas tecnologias. Valorizo o trabalho em equipe e estou em constante busca por aprimoramento profissional. """

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(10))