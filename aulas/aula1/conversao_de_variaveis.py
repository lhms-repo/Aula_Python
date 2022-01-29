# Transformando um float em um int:
flutuante = 1.0214
inteiro = int(flutuante)
print(inteiro)

# Transformando um int em um float:
inteiro = 5
flutuante = float(inteiro)
print(inteiro)

# É possível especificar o tipo de input:
conteudo_digitado = int(input('Digite um valor inteiro (int) e pressione <Enter>: '))
print('Você digitou:\n' + '\t' + str(conteudo_digitado) + '\n')
# Dica: tente digital uma letra em vez de um número