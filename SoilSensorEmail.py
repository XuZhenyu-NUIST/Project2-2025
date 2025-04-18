import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

from_email_addr = "505183416@qq.com"
from_email_pass = "aeshagobzrmpbgie"
to_email_addr = "715660750@qq.com"


def callback(channel):
    if GPIO.input(channel):
        print("Water Not Detected!")
    else:
        print("Water Detected!")


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)



def send_plant_status_email(status):
    msg = EmailMessage()
    body = f"Plant status: {status}"
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = 'Plant Watering Notification'

    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(from_email_addr, from_email_pass)
    server.send_message(msg)
    print("Email sent")
    server.quit()



readings = []
times = [0, 6, 12, 18]  
for hour in times:
    current_hour = time.localtime().tm_hour
    if current_hour == hour:
        reading = GPIO.input(channel)
        readings.append(reading)
        if reading:
          status = "You need to water your plant"
        else:
          status = "Water not needed"
        send_plant_status_email(status)
        time.sleep(3600)  

while True:
    time.sleep(1)
