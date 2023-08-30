---
module: module_1
task: speed_record
---
# Lesson 6. Speed record

## Lesson objective
Learn about functions for controlling speed of the robot.

## Introduction
In this lesson, you will learn about three new functions. You will also try to accelerate the robot to its maximum speed, and we will find out how fast it was moving.


## Block of theory
To control the speed of the robot while moving straight, you will need the `moveForwardSpeed(speed)` function. The `speed` parameter can take values from 0 to 100. However, there is one problem: this function only starts the robot but doesn't stop it. Previously, we used functions that automatically stop the robot after execution. Now, we will need a function to manually stop the robot - `stopRobot()`.

But if you tell the robot to stop immediately after the movement function, it won't go anywhere because you've given the command to stop. This means we need to instruct it to stop only after a certain amount of time. For this purpose, we can use the `delay(milliseconds)` function, which is a standard function in the Arduino Wiring programming language and is not part of the `lineRobot` library.

The `delay(milliseconds)` function introduces a pause between executing commands. Inside this function, you need to specify the duration of the pause. The parameter `milliseconds` is given in milliseconds, so 5000 milliseconds is 5 seconds.

The `moveForwardSpeed(speed)` function initiates the robot's forward movement with a speed of `speed` parameter, which can range from 0 to 100.

The `stopRobot()` function stops the robot.

## Task 
Write a program for the robot to make it move with maximum speed for three seconds. Good luck!


## Conclusion
Congratulations! You have written a program for the robot and made it go so fast!
