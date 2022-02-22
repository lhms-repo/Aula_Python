# O uso de funções que retornam um valor é útil para executar trechos 
# de código e ter uma resposta do que foi executado, seja um status de 
# sucesso/fracasso ou um valor (número, string, booleano, etc)

def login(usuario_certo, senha_certa):
    usuario = input('Digite o seu usuário: ')
    senha = input('Digite a sua senha: ')

    if usuario_certo != usuario and senha_certa != senha:
        return 'Nome de usuário ou senha incorreta'
    elif usuario_certo != usuario:
        return 'Nome de usuário incorreto'
    elif senha_certa != senha:
        return 'Senha incorreta'
    else:
        return 'Bem-vindo(a)'

print( login('user01', 'password01') )