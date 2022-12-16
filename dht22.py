import adafruit_dht
import time
import board

dht_device = adafruit_dht.DHT22(board.D4,use_pulseio=False)

def dht22():
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity
        except RuntimeError as error:
            print(error.args[0])
            #print('não foi possivel ler')
            time.sleep(2)
            continue

        time.sleep(2)
        print(f"temperatura = {temperature}, humidade = {humidity}")
