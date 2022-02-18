# Da mesma forma, o for pode ser usado para criar um 
# loop, entretanto, ele acaba sendo mais versátil no 
# python. Veja alguns casos de uso:

for i in [0, 1, 2, 3, 4]:
    print(f'{i}  ', end='')
print(2*'\n')

for i in range(5):
    print(f'{i}  ', end='')
print(2*'\n')

for i in range(4, -1, -1):
    print(f'{i}  ', end='')
print(2*'\n')


frase = 'Imagine uma frase bem bacana aqui'
print(frase)
frase = frase.split(' ')
print(frase)

for palavra in frase:
    for letra in palavra:
        print(f'{letra} ', end='')
    print('   ', end='')
print(2*'\n')