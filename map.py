# Map
#
# Com map, fazemos mapeamento de valores para uma função
#
# Map é uma função que recebe dois parâmetros: o primeiro a função que vai ser utilizada, o segundo um iterável
#
# import math
#
# def area(r):
#     return math.pi * (r ** 2)
#
#
# raios = [2, 5, 7, 3, 10]
#
# # forma comum
# areas = []
# for c in raios:
#     # areas.append((area(c)))
# print(areas)
#
# # forma 2 - Map
#
# areas = map(area, raios)
# print(areas)
# print(list(areas))
#
# # Obs: após a conversão do map os dados serão limpos
#

# f = 9/5 * c + 32
#
# cidades = [('Paraná', 30), ('New York', 15), ('Berlin', 20)]
#
# c_para_f = lambda city: (city[0], (9 / 5) * city[1] + 32)
#
# print(list(map(c_para_f, cidades)))

# Obs: a função passada no map só recebe apenas um parâmetro