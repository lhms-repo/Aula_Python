from time import sleep

# É uma maneira de repetir um trecho de código desde que a sua 
#   condição seja cumprida. Ex:

i = 0
limite = 5
lista = ['O', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'Roma.']

while i < 5:
    print(i)
    i += 1
print('\n')


# É possível usar loops para percorrer arrays:
i = 0

while i < len(lista):
    print(f'{lista[i]} ', end="")
    i += 1
print(2*'\n')


# Loops infinitos podem ser usados de forma favorável:
i = 0

while True:
    if i > 3*limite:
        break
    else:
        print(f'{i}  ', end="")
    i += 1
print(2*'\n')

# Por fim, é extremamente útil poder escolher entre continuar  
#   o loop sem executar o restante do código ou interromper o 
#   loop:

i = -1

while True:
    i += 1

    if i < 3:
        print(i)
        
    elif i < 10:
        print(i)
        continue
    else:
        break

    print('Esperando...')
    sleep(1)