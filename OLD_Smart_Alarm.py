import RPi.GPIO as GPIO
import time
from time import sleep
import schedule

# Wire Setup

in1 = 23
in2 = 24
ena = 25

in3 = 9
in4 = 11
enb = 10

# GPIO setup 

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(ena,1000)
q=GPIO.PWM(enb,1000)

# Intial power:
p.start(100)
q.start(100)

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print("stop")

def move_down(sec):
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(sec)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print("down")

def move_up(time):
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    sleep(time)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print("up")

def low():
    p.ChangeDutyCycle(25)  
    q.ChangeDutyCycle(25)
    print('low')

def medium():
    p.ChangeDutyCycle(50)
    q.ChangeDutyCycle(50)
    print('medium')

def higher():
    p.ChangeDutyCycle(75)
    q.ChangeDutyCycle(75)
    print('high')

def max():
    p.ChangeDutyCycle(100)
    q.ChangeDutyCycle(100)
    print('max')

def wake_up():
    while True:
        try:
            while True:
                x = 1
                print(x)
                while x < 60:
                    move_down(.11)
                    sleep(1)
    #                break
                    move_up(.75)
                    sleep(.5)
    #                break
                    x = x + 1
                    print(x)
                move_up(1)
                sleep(60)
        except KeyboardInterrupt:
            GPIO.cleanup()
            break

# Test Code for arm:
#wake_up()

# Actual Arm setting (Press Ctrl + C + C to De-Activate):

schedule.every().day.at("07:00").do(wake_up)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    






