# String é um array unidimensional de caracteres. Embora
#  sejam muito úteis, consomem mais memória que os demais
#  tipos de variáveis

# Tipos de declarações de strings (são iguais):
string1 = "string"
string_2 = 'string'
print('{string1} é igual a {string_2}? {string1 == string_2}')
print(f'{string1} é igual a {string_2}? {string1 == string_2}')


# Para imprimir no print caracteres especiais, como ', \ ou ", 
#   deve-se colocar uma barra invertida antes, conforme mostrado
#   abaixo:
print('\'')
#print(''') # Este print foi comentado porque gera um erro, teste descomentá-lo