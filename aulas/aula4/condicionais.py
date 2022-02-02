# Condicionais servem para executar um trecho de código caso
#   uma condição seja cumprida. Exemplo:

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
