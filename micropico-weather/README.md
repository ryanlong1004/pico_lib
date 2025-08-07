# micropico-weather

A production-ready, reusable MicroPython application for the Raspberry Pi Pico W that logs temperature and humidity from a DHT22 sensor and sends data to a remote server via HTTP POST.

## 📦 Features

- ✅ Wi-Fi connection with error handling
- ✅ DHT22 sensor reading
- ✅ Alerting on temp/humidity thresholds
- ✅ Logging with file rotation
- ✅ HTTP POST JSON payloads
- ✅ LED status indication
- ✅ Auto-reboot on failure
- ✅ `.env` support for secrets/configs

## 🛠 Setup Instructions

1. Clone the repo:
    ```bash
    git clone https://github.com/youruser/micropico-weather
    ```

2. Upload files to your Pico W using [mpremote](https://github.com/micropython/micropython-tools), Thonny, or rshell:
    ```bash
    mpremote cp src/* :/
    ```

3. Create a `.env` file in the Pico’s root directory (based on `.env.example`):
    ```env
    WIFI_SSID=your_wifi_name
    WIFI_PASSWORD=your_wifi_password
    POST_URL=http://your-webhook-or-server-endpoint
    ```

4. Reboot the board. The `main.py` will auto-run.

## 🧪 Example Output

```
Connected: 192.168.1.34
POST: 200
Data: {'temperature_f': 77.5, 'humidity_percent': 45.3, 'alert': 'OK', 'timestamp': '2025-08-07 21:25:43'}
```

## 📡 Future Enhancements

- MQTT or InfluxDB support
- Support for BME280/AM2320 sensors
- OLED display integration

---
MIT License • Maintained by [you]
