# Concatenar significa juntar, logo, neste tópico trabalhamos 
# a junção de strings

# A operação de concatenação é feita da seguinte maneira:
string1 = 'Olá'
string2 = 'mundo!'
frase = string1 + ' ' + string2
print(frase)

# Ela também pode ser feita com diferentes tipos de variáveis, desde 
# que haja a conversão de tipo:
idade = 16
string1 = '\nEu tenho ' + str(idade) + ' anos.\n'
print(string1)

# há a possibilidade de ir somando as strings:
frase = ''
frase += 'Olá '
print(frase)
frase += 'mundo!'
print(frase)