import RPi.GPIO as GPIO
import json


with open("configuracao_sala_04.json", encoding='utf-8') as meu_json:
    config_pinos = json.load(meu_json)

ip_central = config_pinos["ip_servidor_central"]
porta_central = config_pinos["porta_servidor_central"]

ip_distribuido = config_pinos["ip_servidor_distribuido"]
porta_distribuido = config_pinos["porta_servidor_distribuido"]
nome_sala = config_pinos['nome']

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def setup_out():
    list_dict = []
    for gpios in config_pinos['outputs']:
        GPIO.setup(gpios['gpio'], GPIO.OUT)
        list_dict.append({'dispositivo': gpios['tag'], 'pino': gpios['gpio']})
    return list_dict

def setup_in():
    list_dict = []
    for gpios in config_pinos['inputs']:
        GPIO.setup(gpios['gpio'], GPIO.IN)
        list_dict.append({'dispositivo': gpios['tag'], 'pino': gpios['gpio']})
    GPIO.add_event_detect(config_pinos['inputs'][4]['gpio'], GPIO.RISING)
    GPIO.add_event_detect(config_pinos['inputs'][5]['gpio'], GPIO.RISING)
    return list_dict

