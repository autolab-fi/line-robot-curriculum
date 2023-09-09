#pragma once    
#include "Arduino.h"

#include <Encoder.h>
  
class lineRobot
{

private:
    int in1;
    int in2;
    int in3;
    int in4;
    int encoderLeftPin1;
    int encoderLeftPin2;
    int encoderRightPin1;
    int encoderRightPin2;
    long oldPositionLeft;
    long oldPositionRight;
    long leftPosition;
    long rightPosition;
    Encoder encLeft;
    Encoder encRight;
    

public:
    lineRobot(int pinLeft1, int pinLeft2, int pinRight1, int pinRight2, int encoderLeftPin1, int encoderLeftPin2, int encoderRightPin1, int encoderRightPin2, float radius_wheel, float distance_between_wheels):encLeft(encoderLeftPin1, encoderLeftPin2),encRight(encoderRightPin1, encoderRightPin2){
        distance_between_wheel_and_center = distance_between_wheels/2;
        radius_wheel = radius_wheel;
        in1 = pinLeft1;
        in2 = pinLeft2;
        in3 = pinRight1;
        in4 = pinRight2;
        //Setup left motor
        pinMode(in1, OUTPUT);
        pinMode(in2, OUTPUT);

        //Setup right motor
        pinMode(in3, OUTPUT); 
        pinMode(in4, OUTPUT); 
        k=0.1;
        radius_wheel = 0.0325;
        distance_between_wheel_and_center = 0.097;
        encoder_degrees_optimal = 6.65;
        k_rot = 0.04;
        oldPositionLeft  = -999;
        oldPositionRight  = -999;
        leftPosition = 0;
        rightPosition = 0;
    };
    void set_rotate_coefficinet(float value);
    void set_straight_motion_coefficinet(float value);
    void set_encoder_degrees(float value);
    void startMotorForwardLeft(int sp);
    void startMotorBackwardLeft(int sp);
    void startMotorForwardRight(int sp);
    void startMotorBackwardRight(int sp);
    void stopMotorLeft();
    void stopMotorRight();
    long moveMotors(int dir, int sp);
    void moveForwardDistance(int sp, float  dist);
    void moveBackwardDistance(int sp, float  dist);
    void moveForwardSeconds(int seconds);
    void moveBackwardSeconds(int seconds);
    long getPositionLeftEncoder();
    long getPositionRightEncoder();
    void turnLeftAngle(int ang);
    void turnRightAngle(int ang);
    void resetLeftEncoder();
    void resetRightEncoder();
    void turnLeft();
    void turnRight();
    void rotate();
    //radius of wheels
    float radius_wheel;
    //distance between wheel and center
    float distance_between_wheel_and_center;
    //Coefficient for converting values from the encoder to an angle in degrees
    float encoder_degrees_optimal;
    // Coefficient for turning speed control
    float k_rot;
    // Coefficient for robot motion straight. The coefficient is greater -> the lagging wheel turns more
    float k;
};

extern lineRobot robot;