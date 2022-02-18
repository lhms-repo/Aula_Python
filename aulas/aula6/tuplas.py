# A tupla é igual à uma lista, no entanto, seus valores não podem ser alterados
tupla = ('abc', 123, True)
print(tupla, '\n')

# Acessando um item da tupla
print(tupla[1], '\n')

# Há um esquema para 'alterar o valor de uma tupla', convertendo-a
# para uma lista, alterando o valor na lista e, por fim, convertendo
# essa lista em uma tupla novamente
print(tupla)
lista = list(tupla)
lista [1] = 456
tupla = tuple(lista)
print(tupla, '\n')
# Demais operações, como append, pop, etc, podem usar esse mesmo esquema

# Lendo diversos valores de uma tupla
String, _, nome = tupla
print(f'String: {String}\nnome: {nome}\n')

# Soma de tuplas
tupla1 = ('spgw', 23.32534346, False, ['1', 2, 3.0])
tupla1 += tupla
print(tupla1, '\n')

# Replicando tuplas
tupla1 *= 2
print(tupla1, '\n')

# Contar o número de ocorrências de um valor
print(f'Número de ocorrências: {tupla1.count(False)}\n')

# Encontrar o index na primeira ocorrências de um valor
print(f'Index de ocorrências: {tupla1.index("abc")}')