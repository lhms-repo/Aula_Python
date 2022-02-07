# Listas são um conjunto de dados endereçados de forma mais 
#   eficiente. É uma variável 'que tem vários valores'
# Exemplo de uma lista:
lista = [0, 1, 2, 3]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[-1], '\n\n') # ou print(lista[3], '\n\n')


# É útil saber o tamanho da lista:
print( f'O tamanho da lista é {len(lista)}' )


# Controlando os index da lista
print( lista[2:] )      # printar do item 3 até o final
print( lista[::2] )     # printar a lista de 2 em 2
print( lista[::-1] )    # pritar a lista invertida
print( lista[1:3], '\n\n' )     # printar do item 2 até o 3


# Soma de listas
lista1 = ['a', 'b', 'string']
lista2 = lista + lista1
print(lista2, '\n\n')

# Adição de item ao final da lista
lista = ['teste1']
item = 'teste2'
lista.append(item)
print(lista, '\n\n')

# Adição de item em posição específica da lista
lista = ['abacaxi', 'bronze', 'casa']
print( lista )
lista.insert(2, "melancia") # coloca a string melancia na posicao 2
print( lista, '\n\n' )

# Removendo itens
lista = list( range(0, 10, 1) ) # Cria uma lista de 0 a 9
print( lista )
lista.remove(1) # Remove o número 1
print( lista )
lista.pop(3) # Remove o 3º item da lista
print( lista )
lista.pop() # Remove o último item da lista
print( lista, '\n\n' )

# Deletando uma lista
del lista
try:
    print( lista )
except Exception as erro:
    print(f'Occorreu um erro: {erro}\n\n')

# Copiando uma lista para outra variável
lista = ['a', 'b', 'c']
lista1 = []
lista1 = lista.copy()
print(f'lista: {lista}\nlista1: {lista1}')