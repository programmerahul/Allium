import smtplib
from email.message import EmailMessage
import ssl
import requests
import socket
from time import sleep
from twilio.rest import Client
import keysTwilio as keys
client=Client(keys.account_sid,keys.auth_token)

sender_email = "raspberrypiallium@gmail.com"
receiver_email = "20bcs075@nith.ac.in"
password = "spptbmptonthxofw"

# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)

# endpoint_url = f'http://{ip_address}/device/'
endpoint_url=f'http://127.0.0.1:8000/device/'

status=requests.get(endpoint_url).headers['status']
subject="Estimated lifetime of onion is less than a month!"
body=(f"By analysing the present realtime parameters such as temperature, humidity, co2 and ammonia concentration and using fuzzy logic, it has been found that estimated lifetime of stored onion is only {status} months. Thus it requires immediate actions. Thanks")

em=EmailMessage()
em['From']=sender_email
em['To']=receiver_email
em['Subject']=subject
em.set_content(body)

context = ssl.create_default_context()
print(f"notify.py status :{status}")
while True:
    if float(status) < 1:
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(sender_email,password=password)
            smtp.sendmail(sender_email,receiver_email,em.as_string())
        print("notify.py: mail send")
        message = client.messages.create(
            body=body,
            to=keys.target_number,
            from_=keys.twilio_number
        )
        print("notify.py: sms send")
        sleep(3600)
    sleep(10)


        








