import network
import time
import urequests

def connect_wifi(ssid, password, timeout=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(ssid, password)
        for _ in range(timeout * 2):
            if wlan.isconnected():
                break
            time.sleep(0.5)
        else:
            raise RuntimeError("Wi-Fi timeout")
    return wlan

def send_json(url, payload):
    try:
        res = urequests.post(url, json=payload)
        res.close()
        return res.status_code
    except Exception as e:
        print("POST failed:", e)
        return None
