---
module: module_2
task: headlight_check
---
# Lesson 8. Headlight check

## Lesson objective
Learn about the `setup()` function and how to control LED using the `lineRobot` library.

## Introduction
In previous lessons, you learned about functions for controlling the robot's movement. Now, let's check the robot's headlights to learn about the `setup()` function in Arduino Wiring.


## Block of theory
In the Wiring language for Arduino, every program has two functions: `setup()` and `loop()`
The `setup()` function runs **only once** after the program starts. Inside this function, you can write code to execute other functions or to initialize variables.

The `turnOnHeadlight()` function turns on the LED.
The `turnOffHeadlight` function turns off the LED.
The `turnOnHeadlightForSecond()` function turns on the LED on the robot for exactly one second.

## Task 
Write a program for the robot to turn on Headlights for 3 seconds. 
Hint: you can do this by two ways: using `delay()` or `turnOnHeadlightForSecond()`


## Conclusion
Congratulations! Now you know about one of the fundamental functions in Arduino programs and can control the LED on the robot.

