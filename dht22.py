import adafruit_dht
import board
from configuracao import dht22

dht_device = adafruit_dht.DHT22(board.D18 if dht22[0]['gpio'] == 18 else board.D4,use_pulseio=False)

def dht22():
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
    except RuntimeError as error:
        return error.args[0]

    return f"Temperatura = {temperature} ºC, Humidade = {humidity}%"
    
