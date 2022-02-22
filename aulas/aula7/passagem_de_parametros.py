# O uso de funções com parâmetros é extremamente útil, pois torna 
# o código mais dinâmico e otimizado

def login(usuario_certo, senha_certa):
    usuario = input('Digite o seu usuário: ')
    senha = input('Digite a sua senha: ')

    if usuario_certo != usuario and senha_certa != senha:
        print('Nome de usuário ou senha incorreta')
    elif usuario_certo != usuario:
        print('Nome de usuário incorreto')
    elif senha_certa != senha:
        print('Senha incorreta')
    else:
        print('Bem-vindo(a)')

login('user01', 'password01')
