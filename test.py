# import RPi.GPIO as GPIO
from gpiozero import Motor
from time import sleep

arm = Motor(forward=17, backward=27)

arm.forward()
sleep(5)
