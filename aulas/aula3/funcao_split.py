# A função split divide uma string em função de um caractere divisor
# Por exemplo, vamos dividir uma frase em função dos espaços entre
# as palavras:
frase = 'Curso de Python'
nova_frase = frase.split(' ')
print(frase, '\n', nova_frase, '\n')

frase = 'a,b,c,d,e'
nova_frase = frase.split(',')
print(frase, '\n', nova_frase)

frase = 'abacate'
nova_frase = frase.split('a')
print(frase, '\n', nova_frase)