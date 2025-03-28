from gpiozero import Robot
import RPi.GPIO as GPIO
from time import sleep
import schedule

arm = Robot(left=(2, 3), right=(9, 11))

def wake_up():
    while True:
        try:
            while True:
                x = 1
                print(x)
                while x < 60:
                    arm.backward()
                    sleep(.5)
                    arm.stop()
                    sleep(.25)
                    arm.forward()
                    sleep(.5)
                    arm.stop()
                    sleep(.25)
                    x += 1
                    print(x)
                arm.forward()
                sleep(60)
        except KeyboardInterrupt:
            GPIO.cleanup()
            break

# Test Code for arm:
wake_up()

# Actual Arm setting (Press Ctrl + C + C to De-Activate):

# schedule.every().day.at("08:00").do(wake_up)

# while True:
    # schedule.run_pending()
    # sleep(1)
    
    
