import RPi.GPIO as GPIO
from configuracao import setup_out,setup_in
import time

lista_out = setup_out()
lista_in = setup_in()

def status_out():
    string = ''
    for i in range(len(lista_out)):
        status = "ligado" if GPIO.input(lista_out[i]['pino']) == 1 else "desligado"
        string += f"{lista_out[i]['dispositivo']} esta {status}" + ',' + ' '
    return string[:-2]    

def status_in():
    string = ''
    for i in range(len(lista_in)):
        status = "ligado" if GPIO.input(lista_in[i]['pino']) == 1 else "desligado"
        string += f"{lista_in[i]['dispositivo']} esta {status}" + ',' + ' '
    return string[:-2]