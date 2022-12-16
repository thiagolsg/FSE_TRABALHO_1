
from socket import *
import os
from configuracao import ip_central,porta_central,ip_distribuido,porta_distribuido,nome_sala

# default_host = gethostname()
# default_port = 10350 

# ip_central = gethostname()
# porta_central = default_port



servidor_central = socket(AF_INET, SOCK_STREAM)

servidor_central.bind((ip_central, porta_central))
servidor_central.listen(5)
print(f'Servidor Central conectado no HOST:  {ip_central} e PORTA: {porta_central}')

# distributed_server_connection, distributed_server_address = servidor_central.accept()
# print(f'O Servidor distribuido: {distributed_server_address} se conectou')

while 1:
        print('=================================================')
        print(f'============= BEM VINDO A {nome_sala} =================')
        print('=================================================')
        commands = ''
        new_message = input('VER DISPOSITIVOS DE ENTRADA (1)\nVER DISPOSITIVOS DE SAÍDA (2)\nVER VALORES DE TEMPERATURA E UMIDADE (3)\nACIONAR DISPOSITIVOS (4)\n')
        

        clear_page = int(input('LIMPAR TELA (1)\n'))
        if clear_page == 1:
            os.system('clear')
distributed_server_connection.close()
