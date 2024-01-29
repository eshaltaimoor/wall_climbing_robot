"""
Code Name: WallClimbingRobotJoy.py
Description: This code is the main code, it is for controlling
the Fan and the DC Motors. If you press a certain botton on the
bluetooth gaming controller, it either moves the robot forward
and starts the fan or only starts the fan or stops the robot.
Author: Eshal Taimoor
Date: 11/06/2023
"""
import time
import RPi.GPIO as GPIO
import pygame
GPIO.setwarnings(False)
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

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

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.JOYBUTTONDOWN:
            if pygame.joystick.Joystick(0).get_button(3):
                 power_3.ChangeDutyCycle(20)
                 print("Fan Started")
            elif pygame.joystick.Joystick(0).get_button(0):
                 GPIO.output(in1,GPIO.LOW)
                 GPIO.output(in2,GPIO.LOW)
                 GPIO.output(in3,GPIO.LOW)
                 GPIO.output(in4,GPIO.LOW)
                 power_3.ChangeDutyCycle(0)
                 print("Robot Stopped")
            elif pygame.joystick.Joystick(0).get_button(1):
                 power_3.ChangeDutyCycle(20)
                 time.sleep(2)
                 GPIO.output(in1,GPIO.HIGH)
                 GPIO.output(in2,GPIO.LOW)
                 GPIO.output(in3,GPIO.HIGH)
                 GPIO.output(in4,GPIO.LOW)
                 power_1.ChangeDutyCycle(50)
                 power_2.ChangeDutyCycle(50)
                 print("Robot Moving Forward")
   

