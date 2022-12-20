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
            print(f'{nome_sala} se conectou')
    except RuntimeError as error:
        return error.args[0]

def recebe_contagem():
    try:
        while True:
            quantidade = svr_distribuido.recv(1024).decode()
            if quantidade[0] == 'Q':
                # nome_sala = svr_distribuido.recv(1024).decode()
                # lista_svr_distribuido.append({'conexao':svr_distribuido,'sala': nome_sala})
                print(f'{quantidade}')
    except RuntimeError as error:
        return error.args[0]

threading.Thread(target=recebe_conexao, ).start()

#threading.Thread(target=recebe_contagem, ).start()

while True:
    print('====================================================')
    print(f'============= BEM VINDO AO PRÉDIO =================')
    for sala in lista_svr_distribuido: print(sala['sala']+' esta conectada')
    print('=================================================')
    
    entrada_usuario = str(input('VER DISPOSITIVOS DE ENTRADA (1)\nVER DISPOSITIVOS DE SAÍDA (2)\nVER VALORES DE TEMPERATURA E UMIDADE (3)\nACIONAR DISPOSITIVOS (4)\nPESSOAS NA SALA (5)\nLIGAR TODAS AS LAMPADAS (6)\nDESLIGAR TODAS AS CARGAS (7)\n'))

    if entrada_usuario != '4' and entrada_usuario != '6' and entrada_usuario != '7':
       
        os.system('clear')

        for sala in lista_svr_distribuido: print(sala['sala'])
        numero_sala = str(input('Digite o número da sala que deseja\n'))

        with open('log.csv','a') as csvfile:
            evento = f'Visualizando Dispositivos de Entrada Sala {numero_sala}' if entrada_usuario == '1' else f'Visualizando Dispositivos de Saída Sala {numero_sala}' if entrada_usuario == '2' else f'Visualizando Temperatura e Humidade Sala {numero_sala}' if entrada_usuario == '3'  else f'Visualizando Contagem de Pessoas Sala {numero_sala}' 
            writer = csv.writer(csvfile,delimiter = ',')
            print(datetime.now().strftime('%d/%m/%Y %H:%M')+',',evento,file = csvfile)
            
        for sala in lista_svr_distribuido:
            if sala['sala'][-1] == numero_sala:
                svr_distribuido_conexao = sala['conexao']

        try:
            while True:
                svr_distribuido_conexao.send(entrada_usuario.encode())
                message_received = svr_distribuido_conexao.recv(1024)
                print(message_received.decode())
                time.sleep(2)
        except KeyboardInterrupt:
            os.system('clear')
            continue
    elif entrada_usuario == '4':
        
        os.system('clear')

        for sala in lista_svr_distribuido: print(sala['sala'])
        numero_sala = str(input('Digite o número da sala que deseja\n'))

        with open('log.csv','a') as csvfile:
            evento = f'Acionando Dispositivos Sala {numero_sala}' 
            writer = csv.writer(csvfile,delimiter = ',')
            print(datetime.now().strftime('%d/%m/%Y %H:%M')+',',evento,file = csvfile)
            
        for sala in lista_svr_distribuido:
            if sala['sala'][-1] == numero_sala:
                svr_distribuido_conexao = sala['conexao']

        svr_distribuido_conexao.send(entrada_usuario.encode())
        print(svr_distribuido_conexao.recv(1024).decode())

        pino = str(input("\nDigite o dispositivo que deseja alterar o estado, Lampada 01 = 1, Lampada 02 = 2, Projetor = 3, Ar-Condicionado = 4\n"))

        svr_distribuido_conexao.sendall(pino.encode())
        print(svr_distribuido_conexao.recv(1024).decode())
    
    elif entrada_usuario == '6':
        
        os.system('clear')

        for sala in lista_svr_distribuido: print(sala['sala'])
        numero_sala = str(input('Digite o número da sala que deseja\n'))

        with open('log.csv','a') as csvfile:
            evento = f'Acionando Dispositivos Sala {numero_sala}' 
            writer = csv.writer(csvfile,delimiter = ',')
            print(datetime.now().strftime('%d/%m/%Y %H:%M')+',',evento,file = csvfile)
            
        for sala in lista_svr_distribuido:
            if sala['sala'][-1] == numero_sala:
                svr_distribuido_conexao = sala['conexao']

        svr_distribuido_conexao.send(entrada_usuario.encode())
        print(svr_distribuido_conexao.recv(1024).decode())
    
    elif entrada_usuario == '7':
        
        os.system('clear')

        for sala in lista_svr_distribuido: print(sala['sala'])
        numero_sala = str(input('Digite o número da sala que deseja\n'))

        with open('log.csv','a') as csvfile:
            evento = f'Acionando Dispositivos Sala {numero_sala}' 
            writer = csv.writer(csvfile,delimiter = ',')
            print(datetime.now().strftime('%d/%m/%Y %H:%M')+',',evento,file = csvfile)
            
        for sala in lista_svr_distribuido:
            if sala['sala'][-1] == numero_sala:
                svr_distribuido_conexao = sala['conexao']

        svr_distribuido_conexao.send(entrada_usuario.encode())
        print(svr_distribuido_conexao.recv(1024).decode())
             
                
svr_distribuido.close()