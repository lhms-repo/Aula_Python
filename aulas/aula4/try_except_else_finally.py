# try: o script tentará executar o trecho de código dentro dele
# except: caso o trecho do 'try' falhe, o except é executado
# else: é executado caso o trecho do 'try' dê certo
# finally: é executado em qualquer ocasião

# Logo:
# try (OK) -> else -> finally
# try (Falhou) -> except -> finally

# Teste essa hipótese executando este script com a declaração abaixo
#   (x = 1) comentada e, depois, descomentada:

x = 1

try:
    print(x)
except:
    print('2')
else:
    print('3')
finally:
    print('4')
    print()


# Observe que os blocos 'else' e 'finally' são opcionais, logo,
#   é possível usar somente o 'try' e o 'except', como é mostrado 
#   abaixo. Além disso, é possível printar qual o erro em questão:

try:
    print(x)
except Exception as erro:
    print(erro)