import RPi.GPIO as GPIO
import time

# Set the GPIO pins that the HY-SRF05 sensor is connected to
TRIGGER_PIN = 23
ECHO_PIN = 24

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    # Send a pulse to the trigger pin
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    # Wait for the echo pin to go high
    start_time = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pass

    # Measure the time that the echo pin is high
    pulse_duration = time.time() - start_time

    # Calculate the distance in centimeters
    distance = pulse_duration * 17000

    return distance

# Print the distance to the console
distance = measure_distance()
print("Distance:", distance, "cm")

# import RPi.GPIO as GPIO
# import time
# 
# def isGoingIn(valu1, value2):
#     # TODO implementere logikk :)
#     return True
# 
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# counter = 0
# 
# # sensor 1
# PIR_PIN = 4
# GPIO.setup(PIR_PIN, GPIO.IN)
# 
# # sensor 2
# PIR_PIN2 = 5
# GPIO.setup(PIR_PIN2, GPIO.IN)
# 
# print('Starting up the PIR Module (click on STOP to exit)')
# time.sleep(1)
# print ('Ready')
# 
# while True:
#     if GPIO.input(PIR_PIN):
#         print("Motion Detected on {}!".format(str(PIR_PIN)))
# 
#         if isGoingIn(PIR_PIN, PIR_PIN2):
#             counter += 1
#         else:
#             counter -= 1
#         print('Antall personer i rommet {}'.format(counter))
#     time.sleep(1)
