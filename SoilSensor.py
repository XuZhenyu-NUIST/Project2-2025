import RPi.GPIO as GPIO
import time 

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
  if GPIO.input(channel):
    print("Water Detected!")
  else:
    print("Water NOT Detected!")

GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=300)
GPIO.add_event_callback(channel,callback)

i = 0
interval = 3*60*60
start_time = time.time()

while True:
  current_time = time.time()
    
  if (current_time - start_time) >= interval:
        if GPIO.input(channel):
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Water Detected!")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Water NOT Detected!")
        read_count += 1
        start_time = current_time
        if read_count == 4:
            break
  time.sleep(1)  







  time.sleep(1)
