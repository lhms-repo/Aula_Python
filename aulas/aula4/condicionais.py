# Condicionais servem para executar um trecho de código caso
# uma condição seja cumprida. Exemplo:

numero = 4

if numero > 3:
    print(f'{numero} é > que 3')
elif numero < 3:
    print(f'{numero} é <= 3')
else:
    print(f'{numero} é = 3')


# Exemplo com string
string = 'Hello world!'
if 'world' in string:
    print('A frase contém o trecho \'world\'')
else:
    print('A frase não contém o trecho \'world\'')

# As verificações podem ser quão grandes o programador desejar.
# Observe que o exemplo abaixo não é eficiente, é só um exemplo:
numero = 5
if numero == 1:
    print('numero é = 1')
elif numero == 2:
    print('numero é = 2')
elif numero == 3:
    print('numero é = 3')
elif numero == 4:
    print('numero é = 4')
elif numero == 5:
    print('numero é = 5')
else:
    print('numero é > 5')