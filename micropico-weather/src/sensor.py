import dht
import machine

class DHTSensor:
    def __init__(self, pin=2):
        self.sensor = dht.DHT22(machine.Pin(pin))

    def read(self):
        self.sensor.measure()
        temp_c = self.sensor.temperature()
        temp_f = (temp_c * 9 / 5) + 32
        humidity = self.sensor.humidity()
        return temp_f, humidity
