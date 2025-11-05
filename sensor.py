import requests
import socket
from time import sleep
import fuzzy
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create analog input channels for the ADC
chan_co2 = AnalogIn(ads, ADS.P0)  # Connect MQ-135 analog output to A0
# You may need to adjust the sensitivity (gain) based on your application
# Possible values for gain are: 2/3, 1, 2, 4, 8, 16
# Adjust as necessary for your application
chan_co2.gain = 16
import Adafruit_DHT
import requests
import socket
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
sensor = Adafruit_DHT.DHT11
pin = 16

# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)
#
# print(ip_address)
# endpoint_url = f'http://{ip_address}/device/'
endpoint_url = 'http://127.0.0.1:8000/device/'
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity) ("CO2 and NH3 Concentration: {:.2f} ppm".format(co2_ppm))))
    # gases=
    co2_voltage = chan_co2.voltage
    # Convert voltage to CO2 concentration (you'll need to calibrate this based on your sensor's datasheet)
    # This is just a hypothetical formula, you may need to adjust it based on actual sensor response
    gases = 250 * co2_voltage + 120  # Hypothetical conversion factor
    # print("CO2 Concentration: {:.2f} ppm".format(co2_ppm))

    print(f" Temp= {temperature}C, Humidity = {humidity}% , Co2 Concentration = {gases}ppm")
    GPIO.input(21)
    # print(gases)
    # humidity=70
    # temperature=22
    # gases=1
    # if(gases=True):
    # gas_presence = 'True'

    # true means nothing detected
    # print("reached")
    # data = {
    # 'name': 'Device 1',
    # 'temperature': temperature,
    # 'humidity': humidity,
    # 'toxicGases': gases,
    # 'status': 1
    # }
    # requests.post(endpoint_url, json=data)
    # print(data)
    status = fuzzy.estimate_Shelf_life(temperature, humidity, gases)
    print(
        f"sensorNoNeed.py : temp={temperature}, Humidity={humidity}, gases={gases} ,status={status}, endpoint_url={endpoint_url}")
    data = {
        'name': 'Device 1',
        'temperature': temperature,
        'humidity': humidity,
        'toxicGases': gases,
        'status': status
    }
    requests.post(endpoint_url, json=data)
    print("sensorNoNeed.py : post api called successfully")
    sleep(10)
# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)

# print(ip_address)
# endpoint_url = f'http://{ip_address}/device/'
# endpoint_url=f'http://127.0.0.1:8000/device/'
# while True:





