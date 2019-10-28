from gpiozero import Buzzer
from time import sleep
import time
import requests

#autostart
#https://www.raspberrypi.org/documentation/linux/usage/rc-local.md

#resting heart rate to be either calcualted from data over time,
#either in program on human wearable
#or pulled fro existing wearable data

restingHR = 60

buzzer = Buzzer(15)
heartRate = raw_input("HeartRate: ")
while True:
    #heartRate = float((requests.get("http://piland.socialdevices.io/42/read/11")).text)
    
    print (str(heartRate))
    if int(heartRate) > 110:
        buzzer.on()
        time.sleep(3)
        buzzer.off()
        heartRate = raw_input("HeartRate: ")
    else:
        buzzer.off()
        heartRate = raw_input("HeartRate: ")

    time.sleep(1)
