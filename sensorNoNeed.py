import requests
import socket
from time import sleep
import fuzzy

# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)

# print(ip_address)
# endpoint_url = f'http://{ip_address}/device/'
endpoint_url=f'http://127.0.0.1:8000/device/'
while True:
    temperature = 28
    humidity = 59
    gases = 989
    status=fuzzy.estimate_Shelf_life(temperature,humidity,gases)
    print(f"sensorNoNeed.py : temp={temperature}, Humidity={humidity}, gases={gases} ,status={status}, endpoint_url={endpoint_url}")
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




