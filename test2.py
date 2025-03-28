from gpiozero import OutputDevice
from time import sleep

in1 = OutputDevice(17)
in2 = OutputDevice(27)

print("forward")
in1.on()
in2.off()
sleep(2)

print("backward")
in1.off()
in2.on()
sleep(2)

print("stop")
in1.off()
in2.off()
