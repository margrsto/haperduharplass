import RPi.GPIO as GPIO
import time

def isGoingIn(valu1, value2):
    # TODO implementere logikk :)
    return True

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
counter = 0

# sensor 1
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)

# sensor 2
PIR_PIN2 = 5
GPIO.setup(PIR_PIN2, GPIO.IN)

print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print ('Ready')

while True:
    if GPIO.input(PIR_PIN):
        print("Motion Detected on {}!".format(str(PIR_PIN)))

        if isGoingIn(PIR_PIN, PIR_PIN2):
            counter += 1
        else:
            counter -= 1
        print('Antall personer i rommet {}'.format(counter))
    time.sleep(1)
