from socket import *
import RPi.GPIO as GPIO
import time
from configuracao import ip_central,porta_central,nome_sala
from status import status_out,status_in,contagem_pessoas
from dht22 import dht22
import threading
from acionamento import altera_estado,ligar_lampadas,desligar_cargas

print(ip_central, porta_central)

svr_distribuido = socket(AF_INET, SOCK_STREAM)
svr_distribuido.connect((ip_central, porta_central))
svr_distribuido.sendall(nome_sala.encode())

while True:
    
    mensagem = svr_distribuido.recv(1024)
    mensagem_recebida = mensagem.decode()
    print(mensagem_recebida)

    if mensagem_recebida != '4' and mensagem_recebida != '6' and mensagem_recebida != '7':
        envia_mensagem = status_out() if mensagem_recebida == '1' else status_in() if mensagem_recebida == '2' else contagem_pessoas() if mensagem_recebida == '5' else dht22()
        svr_distribuido.send(envia_mensagem.encode())
        
    elif mensagem_recebida == '4':
        svr_distribuido.sendall(status_out().encode())
        pino = int(svr_distribuido.recv(1024).decode())
        envia_mensagem = altera_estado(pino)
        svr_distribuido.sendall(envia_mensagem.encode())

    elif mensagem_recebida == '6':       
        envia_mensagem = ligar_lampadas()
        svr_distribuido.sendall(envia_mensagem.encode())

    elif mensagem_recebida == '7':       
        envia_mensagem = desligar_cargas()
        svr_distribuido.sendall(envia_mensagem.encode())
    
