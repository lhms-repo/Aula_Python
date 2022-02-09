#!/usr/bin/env python3

import socket
from datetime import datetime

maquina = 'localhost'
porta = 10000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
endereco_do_servidor = (maquina, porta)
print('Iniciando na maquina {} e porta {}'.format(*endereco_do_servidor))
sock.bind(endereco_do_servidor)
sock.settimeout(1)
print('\nEsperando para receber uma messagem...')

while True:
    try:
        mensagem, endereco = sock.recvfrom(4096)

        if mensagem:
            enviar = sock.sendto(b'OK', endereco)

        tempo_atual = datetime.now().strftime('%H:%M:%S')
        mensagem = str(mensagem, 'UTF-8')
        print(f'[{tempo_atual}] {endereco[0]}: {mensagem}')

    except TimeoutError:
        continue

    except KeyboardInterrupt:
        print('Encerrando servidor...')
        exit(1)