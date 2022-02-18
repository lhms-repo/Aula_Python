# Matriz é um vetor com mais de uma dimensão. Observe:

# vetor: [1, 2, 3]

# Matriz: [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]

matriz = [
    [1, 2, 3],
    [True, False],
    'Hello world!'.split(),
]

# Percorrendo uma matriz
print(matriz, '\n')
for linha in matriz:
    for item in linha:
        print(f'{item} ')

# Printando uma matriz de forma organizada
print('\n'*2)
for linha in matriz:
    for item in linha:
        print(f'{item} ', end='')
    print('\n')