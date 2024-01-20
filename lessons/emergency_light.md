---
index: 7
module: module_2 
task: emergency_light
previous: headlight_check
next: -
---
# Lesson 7: Emergency Light

## Objective
Learn about the **loop()** function.

## Introduction
In previous lessons, you learned about functions for controlling the robot's movement and the **setup()**. Now, let's create code for an emergency light using **loop()** arduino function.

## Theory
The `loop()` function runs immediately after the `setup()` function, and anything inside this function will **continue to execute while the robot is turned on**.

Exercise caution with the `loop()` function because everything inside it will execute infinitely. For instance:
```cpp
...
void loop(){
    robot.moveForwardSeconds(3);
}
```
In this case, the robot will not move for three seconds; instead, it will continue moving indefinitely. After executing the command and moving for three seconds, the robot will start executing the command again from the beginning.

## Task
Write a program for the robot to make the LED blink every second, meaning the LED is **on for a second**, then **off for a second**, and so on.

## Conclusion
Congratulations! You now have an understanding of the loop function and can create more complex programs for the robot.