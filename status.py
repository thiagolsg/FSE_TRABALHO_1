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

def contagem_pessoas(contagem = 0):
    gpio_entrada = ''
    gpio_saida = ''

    for sensor in lista_in:
        if sensor['dispositivo'] == 'Sensor de Contagem de Pessoas Entrada':
            gpio_entrada = int(sensor['pino'])
        if sensor['dispositivo'] == 'Sensor de Contagem de Pessoas Saída':
            gpio_saida = int(sensor['pino'])

    time.sleep(0.0001)
    if GPIO.event_detected(gpio_entrada):
        contagem = contagem + 1
    if GPIO.event_detected(gpio_saida):
        contagem = contagem - 1
        if contagem < 0:
            contagem = 0

    return f'Quantidade de pessoas na sala {contagem}'
   
