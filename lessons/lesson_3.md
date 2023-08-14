---
module: module_1
task: short_distance_race
---
# Lesson 3. Short distance race

## Lesson objective
Learn about functions for moving the robot a specific distance.

## Introduction
Over two lessons, we have used only one function of the `lineRobot` library. It's now time to know about other functions for controlling the robot: moving backward and moving forward, where the parameter is not the number of seconds but the distance.

## Block of theory

In the previous lesson, you learned about **functions** and **parameters**, and used the `moveForwardSeconds(seconds)` function with a parameter representing the number of seconds for robot movement. However, we need precise control over the robot's position on the map. To achieve this, we can use functions for movement where the parameter represents the distance in centimeters.

`robot.moveForwardDistance(dist)` - function for moving the robot **forward** by the number of centimeters specified by the parameter dist.
`robot.moveBackwardDistance(dist)` - function for moving the robot **backward** by the number of centimeters specified by the parameter dist.


## Task 
Write a program for the robot to move **backward 35** centimeters, and then **forward 20** centimeters. Good luck!


## Conclusion
Congratulations! You have learned about two important functions of the library that you will be able to use in the next lessons.

