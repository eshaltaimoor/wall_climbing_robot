/***********************************************************
File name: BlockPicking.ino 
Description: This code first makes all the servos 90 degrees (Straight). 
Then it delays the robot for 2 seconds and makes the robotic arm move in
a certain direction to pick a block. 
Author: Eshal Taimoor
Date: 01/07/2024
***********************************************************/
#include <Servo.h>。
int servopin1 = 9;    //Define servo interface digital interface 9
int servopin2 = 6;    //Define servo interface digital interface 6
int servopin3 = 5;    //Define servo interface digital interface 5
int servopin4 = 3;    //Define servo interface digital interface 3
int servopin5 = 11;   //Define servo interface digital interface 11

int moveServoData;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
int angle = 90;        //Angle of rotation of the servo

void setup() {
  // put your setup code here, to run once:
  pinMode(servopin1,OUTPUT);//Set the servo interface as the output interface
  pinMode(servopin2,OUTPUT);//Set the servo interface as the output interface
  pinMode(servopin3,OUTPUT);//Set the servo interface as the output interface
  pinMode(servopin4,OUTPUT);//Set the servo interface as the output interface
  pinMode(servopin5,OUTPUT);//Set the servo interface as the output interface
  Serial.begin(9600);
  servo1.attach(servopin1);
  servo2.attach(servopin2);
  servo3.attach(servopin3);
  servo4.attach(servopin4);
  servo5.attach(servopin5);
// Makes all servos to 90 Degrees (Straight)
  servo1.write(angle);
  servo2.write(angle);
  servo3.write(angle);
  servo4.write(angle);
  servo5.write(angle);
  delay(2000);
/**********************************************
This next part of the code makes the robotic arm
turn to its right, go down, and then pick up the
block I put there.
***********************************************/
  servo4.write(190);
  delay(3000);
  servo1.write(0);
  delay(3000);
  servo2.write(18);
  delay(3000);
  servo3.write(160);
  delay(3000);
  servo5.write(150);
  delay(3000);
  servo3.write(90);
}
void loop()
{
// There is no Code defined in loop to avoid repetition.
}
