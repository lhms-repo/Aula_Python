# A função replace() busca um trecho de string e substitui por algo
# que o programador deseje, retornando a frase com a substituição
# realizada (caso tenha encontrado a substring desejada).
# Exemplo:

frase = 'Eu gosto da cor azul'
frase_nova = frase.replace('azul', 'vermelho')
print(frase)
print(frase_nova)

print()

# Caso a substring não seja encontrada, nenhuma substituição é feita:
frase_nova = frase.replace('verde', 'vermelho')
print(frase)
print(frase_nova)