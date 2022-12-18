from socket import *
import os
from configuracao import ip_central,porta_central,ip_distribuido,porta_distribuido,nome_sala
import time
import csv
from datetime import datetime
import threading

svr_central = socket(AF_INET, SOCK_STREAM)
svr_central.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #teste

svr_central.bind((ip_central, porta_central))
svr_central.listen(5)

print(f'Servidor Central:  {ip_central} e Porta: {porta_central}')

lista_svr_distribuido = []
svr_distribuido_conexao = ''

def recebe_conexao():
    try:
        while True:
            svr_distribuido, svr_distribuido_ip = svr_central.accept()
            nome_sala = svr_distribuido.recv(1024).decode()
            lista_svr_distribuido.append({'conexao':svr_distribuido,'sala': nome_sala})
            print(f'{svr_distribuido_ip} se conectou')
    except RuntimeError as error:
        return error.args[0]

threading.Thread(target=recebe_conexao, ).start()

while True:
    print('====================================================')
    print(f'============= BEM VINDO AO PRÉDIO =================')
    for sala in lista_svr_distribuido: print(sala['sala']+' esta conectada')
    print('=================================================')
    
    entrada_usuario = str(input('VER DISPOSITIVOS DE ENTRADA (1)\nVER DISPOSITIVOS DE SAÍDA (2)\nVER VALORES DE TEMPERATURA E UMIDADE (3)\nACIONAR DISPOSITIVOS (4)\n'))

    if entrada_usuario != '4':
        try:
            os.system('clear')

            for sala in lista_svr_distribuido: print(sala['sala'])
            numero_sala = str(input('Digite o número da sala que deseja\n'))

            with open('log.csv','a') as csvfile:
                evento = f'Visualizando Dispositivos de Entrada Sala {numero_sala}' if entrada_usuario == '1' else f'Visualizando Dispositivos de Saída Sala {numero_sala}' if entrada_usuario == '2' else f'Visualizando Temperatura e Humidade Sala {numero_sala}'
                writer = csv.writer(csvfile,delimiter = ',')
                print(datetime.now().strftime('%d/%m/%Y %H:%M')+',',evento,file = csvfile)
            
            for sala in lista_svr_distribuido:
                if sala['sala'][-1] == numero_sala:
                    svr_distribuido_conexao = sala['conexao']

            svr_distribuido_conexao.send(entrada_usuario.encode())

            while True:

                continua = 'continua'
                svr_distribuido_conexao.sendall(continua.encode())
                message_received = svr_distribuido_conexao.recv(1024)
                print(message_received.decode())
                time.sleep(2)
        except KeyboardInterrupt:
            pare = 'pare'
            svr_distribuido_conexao.send(pare.encode())
            os.system('clear')
            continue

svr_distribuido.close()