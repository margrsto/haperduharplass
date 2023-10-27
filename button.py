#!/usr/bin/env python

import asyncio
import RPi.GPIO as GPIO

b1_pin = 8
bounce_time = 1000


def button1_callback(channel):
    print("Button 1 was pushed", channel)


print("Setting up IO pins")
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(b1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(b1_pin, GPIO.RISING, callback=button1_callback, bouncetime=bounce_time)

asyncio.get_event_loop().run_forever()

print("Finish")
GPIO.cleanup()  # Clean up
