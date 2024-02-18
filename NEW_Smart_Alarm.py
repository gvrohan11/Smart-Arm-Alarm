from gpiozero import Robot
import RPi.GPIO as GPIO
from time import sleep
import schedule

arm = Robot(left=(23, 24), right=(2, 3))

def wake_up():
    while True:
        try:
            while True:
                x = 1
                print(x)
                while x < 60:
                    arm.backward()
                    sleep(1)
                    arm.forward()
                    sleep(1)
                    x += 1
                    print(x)
                arm.forward()
                sleep(60)
        except KeyboardInterrupt:
            GPIO.cleanup()
            break

# Test Code for arm:
# wake_up()

# Actual Arm setting (Press Ctrl + C + C to De-Activate):

schedule.every().day.at("08:00").do(wake_up)

while True:
    schedule.run_pending()
    sleep(1)
    
    
