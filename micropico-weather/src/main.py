import time
import ntptime
import machine
from env import load_env
from sensor import DHTSensor
from net import connect_wifi, send_json
from logger import log_to_file, rotate_log

# Load configuration
config = load_env()
SSID = config["WIFI_SSID"]
PASSWORD = config["WIFI_PASSWORD"]
POST_URL = config["POST_URL"]
LOG_FILE = "dht_log.csv"
MAX_FAILS = 5
led = machine.Pin("LED", machine.Pin.OUT)

# Setup
connect_wifi(SSID, PASSWORD)
ntptime.settime()
sensor = DHTSensor(pin=2)

if LOG_FILE not in os.listdir():
    log_to_file(LOG_FILE, "timestamp,temperature_f,humidity_percent,alert")

failures = 0

while True:
    try:
        temp_f, humidity = sensor.read()
        alert = "OK"
        if temp_f > 80: alert = "HIGH_TEMP"
        elif temp_f < 50: alert = "LOW_TEMP"
        if humidity > 70: alert = "HIGH_HUMIDITY"
        elif humidity < 20: alert = "LOW_HUMIDITY"

        ts = "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(*time.localtime()[:6])
        log_line = f"{ts},{temp_f:.2f},{humidity:.2f},{alert}"
        rotate_log(LOG_FILE)
        log_to_file(LOG_FILE, log_line)

        payload = {"timestamp": ts, "temperature_f": temp_f, "humidity_percent": humidity, "alert": alert}
        led.value(1)
        send_json(POST_URL, payload)
        led.value(0)

        failures = 0
        time.sleep(10)

    except Exception as e:
        print("Error:", e)
        failures += 1
        if failures >= MAX_FAILS:
            machine.reset()
        time.sleep(5)
