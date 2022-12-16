import RPi.GPIO as GPIO
import time
import json
from configuracao import setup_out,setup_in

lista_out = setup_out()
lista_in = setup_in()

while 1:
    for i in range(len(lista_out)):
        status = "ligado" if GPIO.input(lista_out[i]['pino']) == 1 else "desligado"
        print(f"{lista_out[i]['dispositivo']} esta {status}")

    print("-----------------------------------------------------------------")

    for i in range(len(lista_in)):
        status = "ligado" if GPIO.input(lista_in[i]['pino']) == 1 else "desligado"
        print(f"{lista_in[i]['dispositivo']} esta {status}")

    print("-----------------------------------------------------------------")
    time.sleep(5)

