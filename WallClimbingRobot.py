import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

in3 = 27
in4 = 22
en_2 = 17
in2 = 23
in1 = 24
en_1 = 25
en_3 = 4

# To use Broadcom GPIO numbers instead of using board pi numbers
GPIO.setmode(GPIO.BCM)

#Setup the output pins
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en_1,GPIO.OUT)
GPIO.setup(en_3,GPIO.OUT)

power_1 = GPIO.PWM(en_1,100)
power_1.start(50)
power_2 = GPIO.PWM(en_2,100)
power_2.start(50)
power_3 = GPIO.PWM(en_3,20)
power_3.start(0)
power_3.ChangeDutyCycle(10)
time.sleep(5)
power_3.ChangeDutyCycle(0)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

print(" Print f for Forward , b for Backward , s for Stop, r for Rabbit, t for Turtle")

while True:
    user_input = input()
    
    if user_input == 'f':
        power_3.ChangeDutyCycle(20)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        power_1.ChangeDutyCycle(50)
        power_2.ChangeDutyCycle(50)
    elif user_input == 'b':
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        power_1.ChangeDutyCycle(50)
        power_2.ChangeDutyCycle(50)
    elif user_input == 's':
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        power_3.ChangeDutyCycle(0)
    elif user_input == 'r':
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        power_1.ChangeDutyCycle(80)
        power_2.ChangeDutyCycle(80)
    elif user_input == 't':
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        power_1.ChangeDutyCycle(20)
        power_2.ChangeDutyCycle(20)