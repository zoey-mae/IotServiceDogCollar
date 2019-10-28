'''
Zoey Sears & Deanna Soukup 2019

During a panic attack, humans experience heart palpitations and elevated heart rate.
The human will wear a wear an IoT heart rate monitor.
simulated heart rate data is posted to piland.socialdevices.io
a button is depressed to simulate a panic attack
Because sustained exercise will also raise the human's heart rate,
the human's heart rate monitor should be removed or turned off during exercise.
'''

import RPi.GPIO as GPIO
import time
import requests
import random

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

requests.get("http://piland.socialdevices.io/42/write/11?name=Heart+Rate")
requests.get("http://piland.socialdevices.io/42/write/11?units=bpm")


while True:
    input_state = GPIO.input(18)
    if input_state == False:
        HR = random.randint(110,120)
        time.sleep(1)
    else:
        HR = random.randint(85,89)
        time.sleep(1)
    print(HR)
    try:
        requests.get("http://piland.socialdevices.io/42/write/11?value="+str(HR))
        print("Posted HR data to piland.socialdevices.io: " + str(HR) + " bpm")
    except:
        print("There was an error when posting anxiety attack HR to piland.")
    
    




              
