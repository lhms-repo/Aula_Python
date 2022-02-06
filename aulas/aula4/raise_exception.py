# Existem diversos tipos de erros que podem fazer com que o código 
#   caia em um bloco 'exception', conforme é mostrado abaixo:
# - ZeroDivisionError: divisão por 0
# - NameError: erro na nomenclatura de uma variável, função, etc
# - TypeError: operação inválida com aquele tipo de variável
# - ValueError: erro na conversão de valor
# - KeyboardInterrupt: foi pressionado CTRL + C durante a execução do script
# E outros, como RuntimeError, OSError e BaseException...
# Mais detalhes em: https://docs.python.org/3/tutorial/errors.html

# Dessa forma, é possível ter um 'except' para cada tipo de erro:

a = 1
#a = 'Hello world!'

try:
    a += 1
except ZeroDivisionError:
    print('Divisão por 0 é proibido!')
except NameError:
    print('Alguma coisa não foi declarada...')
except TypeError:
    print('Essa operação é inválida para esse tipo de variável!')
except ValueError:
    print('Não é possível fazer essa conversão.')
except KeyboardInterrupt:
    print('Interrompendo a execução do script com CTRL + C...')
else:
    print('Nenhum erro foi encontrado!')
finally:
    print('Finalizado')

#TODO: colocar parte do raise exceptions