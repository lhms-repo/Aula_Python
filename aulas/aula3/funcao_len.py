# A função len() retorna o tamanho do array
# len(<nome da variável>)

# Tomando como exemplo a palavra 'array', que tem 5 letras:
print( len('array') )
print() # pula uma linha

# Essa função é muito útil para saber o tamanho do array em 
# trechos de código em que o array pode ter diferentes tamanhos

# Teste digitando diferentes palavras na variável abaixo:
variavel = ''
print( len(variavel) )
print()

# Exemplo de aplicação da função len():
# Printe o penúltimo caractere de uma string aleatória:
variavel = 'string aleatória'
print(   variavel[ len(variavel) - 2 ]   )