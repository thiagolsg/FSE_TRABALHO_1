from socket import *
import os
from configuracao import ip_central,porta_central,ip_distribuido,porta_distribuido,nome_sala
import time

svr_central = socket(AF_INET, SOCK_STREAM)
svr_central.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #teste

svr_central.bind((ip_central, porta_central))
svr_central.listen(5)

print(f'Servidor Central conectado no HOST:  {ip_central} e PORTA: {porta_central}')

svr_distribuido, svr_distribuido_ip = svr_central.accept()
print(f'O Servidor distribuido: {svr_distribuido_ip} se conectou')


while True:
    print('=================================================')
    print(f'============= BEM VINDO A {nome_sala} =================')
    print('=================================================')

    
    entrada_usuario = str(input('VER DISPOSITIVOS DE ENTRADA (1)\nVER DISPOSITIVOS DE SAÍDA (2)\nVER VALORES DE TEMPERATURA E UMIDADE (3)\nACIONAR DISPOSITIVOS (4)\n'))
    svr_distribuido.send(entrada_usuario.encode())

    try:
        os.system('clear')
        while True:
            continua = 'continua'
            svr_distribuido.send(continua.encode())
            message_received = svr_distribuido.recv(1024)
            print(message_received.decode())
            time.sleep(2)
    except KeyboardInterrupt:
        pare = 'pare'
        svr_distribuido.send(pare.encode())
        os.system('clear')
        continue
    
    # clear_page = int(input('LIMPAR TELA (1)\n'))
    # if clear_page == 1:
    #     os.system('clear')


svr_distribuido.close()
