from socket import *
import RPi.GPIO as GPIO
import time
from configuracao import ip_distribuido,porta_distribuido,nome_sala
from status import status_out,status_in
from dht22 import dht22

print(ip_distribuido, porta_distribuido)

svr_distribuido = socket(AF_INET, SOCK_STREAM)
svr_distribuido.connect((ip_distribuido, porta_distribuido))

while True:
    
    mensagem = svr_distribuido.recv(1024)
    print(mensagem.decode())
    mensagem_recebida = mensagem.decode()
    print(mensagem_recebida)

    while True:
        if svr_distribuido.recv(1024).decode() == 'pare': 
            print("-------------------------PARE--------------------------------------------------")
            break
        envia_mensagem = status_out() if mensagem_recebida == '1' else status_in() if mensagem_recebida == '2' else dht22()
        svr_distribuido.sendall(envia_mensagem.encode())
