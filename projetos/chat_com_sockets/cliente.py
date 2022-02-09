#!/usr/bin/env python3

import socket
import sys

maquina = 'localhost'
porta = 10000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)
endereco_do_servidor = (maquina, porta)
#mensagem = b'This is the mensagem.  It will be repeated.'
mensagem = 'Olá, mundo!'

try:
    enviar = sock.sendto( bytes(mensagem, 'utf-8'), endereco_do_servidor)

    reposta, server = sock.recvfrom(4096)
    resposta = str(reposta, 'UTF-8')
    print( f'[{resposta}] Enviado para {maquina}: {mensagem}' )

finally:
    sock.close()