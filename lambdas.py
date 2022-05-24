'''
Conhecidas por expressões lambdas são funções sem nome, ou seja, funções anônimas

# Função comum:

def soma(a):
  return 3 * a + 1

print(soma(2))

# Função lambda:

lambda a: 3 * a + 1

# Para utilizar a lambda: não é a forma ideal

var = lambda a: 3 * a + 1

print(var(2))

# Na expressão lambda utilizamos parâmetros como numa função comum, apenas não é nomeada e feita
# toda em uma mesma linha
# após os: é o retorno da função

nome = lambda nome, sobre: nome.strip().title() + ' ' + sobre.strip().title()

print(nome('bruno ', ' vittor  '))

nomes = ['Miguel Souza', 'Davi Augusto', 'Gabriel Vittor', 'Carlos Eduardo', 'Marcelo castro', 'rafael silva']

nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].title())

print(nomes)

OBS: Se passarmos mais argumentos do que parâmetros esperados teremos type error

# media = lambda nota1, nota2: (nota1 + nota2) / 2
#
# print(media(10, 5))

# pessoas = ['Bruno Vittor', 'kamila Ribeiro', 'Isabella Veronezi', 'Walter Vittor']
#
# pessoas.sort(key=lambda sobrenome: sobrenome.split(' ')[-1])
#
# print(pessoas)

Em resumo a lambda e formada assim :

variável = lambda parâmetro: o que deseja frazer com o parâmetro

'''



