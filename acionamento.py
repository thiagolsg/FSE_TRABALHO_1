import RPi.GPIO as GPIO
from configuracao import setup_out,setup_in
import time

lista_out = setup_out()
# print(lista_out)
def altera_estado(pino):
    dispositivo = ''
    if pino == 1:
        dispositivo = lista_out[0]['dispositivo']
        pino = lista_out[0]['pino']
    if pino == 2:
        dispositivo = lista_out[1]['dispositivo']
        pino = lista_out[1]['pino']
    if pino == 3:
        dispositivo = lista_out[2]['dispositivo']
        pino = lista_out[2]['pino']
    if pino == 4:
        dispositivo = lista_out[3]['dispositivo']
        pino = lista_out[3]['pino']
    try:
        situacao  = GPIO.input(pino)
        estado = 'ligado' if situacao else 'desligado'
        GPIO.output(pino,GPIO.LOW) if situacao else GPIO.output(pino,GPIO.HIGH)

        estado = 'ligado' if GPIO.input(pino) else 'desligado'
        return f'Dispositivo {dispositivo} esta {estado}'
    except RuntimeError as error:
        return error.args[0]

def ligar_lampadas():
    try:
        GPIO.output(lista_out[0]['pino'],GPIO.HIGH)
        GPIO.output(lista_out[1]['pino'],GPIO.HIGH)

        return f'Lampadas da Sala ligadas'
    except RuntimeError as error:
        return error.args[0]

def desligar_cargas():
    try:
        GPIO.output(lista_out[0]['pino'],GPIO.LOW)
        GPIO.output(lista_out[1]['pino'],GPIO.LOW)
        GPIO.output(lista_out[2]['pino'],GPIO.LOW)
        GPIO.output(lista_out[3]['pino'],GPIO.LOW)
        
        return f'Cargas da Sala desligadas'
    except RuntimeError as error:
        return error.args[0]

#altera_estado(26)