# Observe o array de string da palavra 'string':
# Posição (index):     0    1    2    3    4    5
#                 [ 's', 't', 'r', 'i', 'n', 'g']

string = 'string'
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5]+'\n')

# Podemos printar um trecho do string usando indexes:
# Obs: [<index inicial>:<index final - 1>]
print(string[1:5])

# É possível printar de n em n caracteres também:
# Obs: [<index inicial>:<index final - 1>:<n>]
print('\n'+string[0:6:2]+'\n')

# Pode ser útil usar a string invertida:
print(string[::-1])