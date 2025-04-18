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


def send_daily_soil_report(max_reading, min_reading):
    msg = EmailMessage()
    body = f"Today's maximum moisture reading: {max_reading}\nToday's minimum moisture reading: {min_reading}"
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = 'Daily soil Report'

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_email_addr, from_email_pass)
    server.send_message(msg)
    print("Email sent")
    server.quit()


moisture_readings = []
for i in range(5):
    moisture = GPIO.input(channel)
    moisture_readings.append(moisture)
    time.sleep(3600)

max_reading = max(moisture_readings)
min_reading = min(moisture_readings)
send_daily_soil_report(max_reading, min_reading)

while True:
    time.sleep(1)
