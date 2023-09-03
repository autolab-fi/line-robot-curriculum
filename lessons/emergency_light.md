---
index: 5
module: module_2 
task: emergency_light
previous: headlight_check
next: -
---
# Lesson 9. Emergency light

## Lesson objective
Learn about the `loop()` function.

## Introduction
In previous lessons, you learned about functions functions for controlling the robot's movemen and `setup()`. Now, let's create code for emergency light.


## Block of theory
The `loop()` function runs immediately after the `setup()` function, and anything inside this function will **continue to execute while robot is turned on**.

Be careful with the `loop()` function, because everything inside it will execute infinitely. This means that if you write:
```
...
void loop(){
    robot.moveForwardSeconds(3);
}
```
The robot will not move for three seconds; instead, it will continue moving indefinitely. This is because after executing the command and moving for three seconds, the robot will start executing the command again from the beginning. 

## Task 
Write a program for the robot to make the LED blink every second, meaning the LED is on for a second, then off for a second, and so on.


## Conclusion
Congratulations! Now you know about the loop function and can write more complex programs for the robot.

