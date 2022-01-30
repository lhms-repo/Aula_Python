# Declaração das variáveis
a = 1
b = 3

# Operação com maior ( > )
print('a é maior que b?\n' + str( a > b ) )

# Operação com menor ( < )
print('\na é maior que b?\n' + str( a < b ) )

# Operação com igual ( == )
print('\na é maior que b?\n' + str( a == b ) )

# Operação com diferente ( != )
print('\na é maior que b?\n' + str( a != b ) )

# Operação com maior ou igual ( >= )
print('\na é maior que b?\n' + str( a >= b ) )

# Operação com menor ou igual ( <= )
print('\na é maior que b?\n' + str( a <= b ) )

# Operação com conta
print('\n(a-b+1) é maior ou igual a (-a*b)?\n' + str( a - b + 1 >= -a * b ) )

# Operação composta
print('\n(a-b+1) é maior ou igual a (-a*b) ou (-b * a < 6)?\n' + str(   (a - b + 1 >= -a * b ) or (-b * a < 6)  ) )

# Comparação com strings
a = 'palavra'
b = 'palavra'
print('\na é igual a b?\n' + str( a == b ) )