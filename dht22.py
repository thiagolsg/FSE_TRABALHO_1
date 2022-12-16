import adafruit_dht
import time
import board

dht_device = adafruit_dht.DHT22(board.D4,use_pulseio=False)

def dht22():
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
    except RuntimeError as error:
        return error.args[0]

    return f"temperatura = {temperature}, humidade = {humidity}"
    
