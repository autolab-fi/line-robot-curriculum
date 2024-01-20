---
index: 6
module: module_2
task: headlight_check
previous: long_distance_race
next: emergency_light
---
# Lesson 6: Headlight Check

## Objective
Learn about the **setup()** function and how to control the LED using the lineRobot library.

## Introduction
In the previous lessons, you acquired knowledge about functions for managing the robot's movement. In this lesson, we will inspect the robot's headlights to learn about the **setup()** function in Arduino Wiring.

## Theory

### setup function
In the Wiring language for Arduino, each program consists of two functions: **setup()** and **loop()**.
The **setup()** function executes **only once** after the program initiation. Within this function, you can compose code to perform other functions or initialize variables.

### Light Emitting Diode (LED)
Light Emitting Diode is a device that emits light when an electric current passes through it.

![image](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/LED.jpg?raw=true)

LED Control Functions in the lineRobot library:
- The **turnOnHeadlight()** function illuminates the LED.
- The **turnOffHeadlight()** function extinguishes the LED.
- The **turnOnHeadlightForSecond()** function activates the LED on the robot for precisely one second.

## Assignment
Write a program for the robot to illuminate the headlights for 3 seconds.
<details>
<summary>Hint</summary>

You can achieve this in two ways: using **delay()** or **turnOnHeadlightForSecond()**.
</details>

## Conclusion
Congratulations! You now possess knowledge about one of the fundamental functions in Arduino programs and can manipulate the LED on the robot.