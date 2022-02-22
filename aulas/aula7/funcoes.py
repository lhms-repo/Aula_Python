# Funções são trechos de códigos que são utilizadas com maior 
# frequência, de forma que sua criação torna o código mais legível,
# menor e dinâmico

a = 1
usuario_certo = 'user01'
senha_certa = 'password01'

def minha_funcao():
    print('Olá mundo!')

def incrementa_1():
    global a

    a += 1
    print(f'a = {a}\n')

def login():
    global usuario_certo, senha_certa

    usuario = str( input('Digite o nome de usuário: ') )
    senha = str( input('Digite a sua senha: ') )

    if usuario_certo != usuario and senha_certa != senha:
        print('\nNome de usuário ou senha incorreta')
    elif usuario_certo != usuario:
        print('\nNome de usuário incorreto')
    elif senha_certa != senha:
        print('\nSenha incorreta')
    else:
        print('\nBem-vindo(a)')


minha_funcao()
print(f'a = {a}')
incrementa_1()
login()
