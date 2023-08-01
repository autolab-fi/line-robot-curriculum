#pragma once    
#include "Arduino.h"

//defining pins for motor A 
#define directionPinA 12
#define brakePinA 9
#define speedPinA 3

//defining pins for motor B
#define directionPinB 13
#define brakePinB 8
#define speedPinB 11


class lineRobot
{
private:
    /* data */
public:
    lineRobot();
    void startMotorA(uint8_t direction, int speed);
    void startMotorB(uint8_t direction, int speed);
    void stopMotorA();
    void stopMotorB();
    void stopRobot();
    void moveForward(int speed);
    void moveBackward(int speed);
    void moveForwardSeconds(int seconds);
    void moveBackwardSeconds(int seconds);
    void turnRight();
    void turnLeft();
};

extern lineRobot robot;