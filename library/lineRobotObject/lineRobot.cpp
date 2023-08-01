#include "lineRobot.h"


lineRobot::lineRobot(){
    //Setup Channel A
    pinMode(directionPinA, OUTPUT); //Initiates Motor Channel A pin
    pinMode(brakePinA, OUTPUT); //Initiates Brake Channel A pin

    //Setup Channel B
    pinMode(directionPinB, OUTPUT); //Initiates Motor Channel A pin
    pinMode(brakePinB, OUTPUT);  //Initiates Brake Channel A pin
}
void lineRobot::startMotorA(uint8_t direction, int speed){
    digitalWrite(directionPinA, direction); 
    digitalWrite(brakePinA, LOW);   
    analogWrite(speedPinA, speed);   
}
void lineRobot::startMotorB(uint8_t direction, int speed){
    digitalWrite(directionPinB, direction);
    digitalWrite(brakePinB, LOW);
    analogWrite(speedPinB, speed);
}
void lineRobot::stopMotorA(){
    digitalWrite(brakePinA, HIGH);
}
void lineRobot::stopMotorB(){
    digitalWrite(brakePinB, HIGH);
}
void lineRobot::stopRobot(){
    stopMotorA();
    stopMotorB();
}
void lineRobot::moveForward(int speed) {
    startMotorA(HIGH, speed);
    startMotorB(HIGH, speed);
}
void lineRobot::moveBackward(int speed){
    startMotorA(LOW, speed);
    startMotorB(LOW, speed);
}
void lineRobot::moveForwardSeconds(int seconds){
    moveForward(60);
    delay(seconds*1000);
    stopRobot();
}
void lineRobot::moveBackwardSeconds(int seconds){
    moveBackward(60);
    delay(seconds*1000);
    stopRobot();
}
void lineRobot::turnLeft(){
    startMotorA(HIGH, 60);
    startMotorB(LOW, 60);
    delay(1000);
    stopRobot();
}
void lineRobot::turnRight(){
    startMotorA(LOW, 60);
    startMotorB(HIGH, 60);
    delay(1000);
    stopRobot();
}

lineRobot robot = lineRobot();