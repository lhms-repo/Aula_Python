# O dicionário é uma excelente maneira de organizar dados em uma estrutura, pois é 
# humanamente legível e intuitivo, além de permitir que seus dados sejam alterados

dicionario = {
    'nome': 'John Due',
    'idade': 34,
    'altura': 1.78,
    'casado': True,
    'filhos': ['Vinicius', 'Ana'],
    'pais': ('Maria', 'Mateus')
}

# Printando o dicionário inteiro
print(dicionario,'\n')

# Printando cada item do dicionário
for item in dicionario:
    print(f'dicionario[{item}]: {dicionario[item]}')

# Printando um item específico da lista
print('\n',dicionario['filhos'][0], '\n')

# Substituindo um valor
dicionario['altura'] = 1.83
print('Nova altura: ' + str(dicionario['altura']) + '\n')

# Adicionando um item
dicionario['peso'] = 85.7
print(dicionario, '\n')

# Removendo um item
dicionario.pop('pais')
print(dicionario, '\n')

# Copiando o dicionário
dicionario1 = dicionario.copy()

# Limpando o dicionário
print('Antes: ', dicionario, '\n')
dicionario.clear()
print('Depois: ', dicionario, '\n')

# Deletando o dicionário
try:
    print('Deletando o dicionário...')
    del dicionario1
    print(dicionario1)
except NameError:
    print('O dicionário foi deletada')
else:
    print('O dicionário não foi deletada')