---
index: 1
module: module_1
task: test_drive
previous: draw
next: license_to_drive
---
# Lesson 1. Test drive

## Objective
Get started with the robot and set it in motion promptly.

## Introduction
In this lesson, you will learn how to initiate movement in the robot. It's not a complex task; all you need is a strong desire and perseverance.

Behold the mighty robot who will assist you in learning.
![robot](https://github.com/autolab-fi/line-robot-curriculum/assets/13139586/888c76f9-8b02-4159-ae0c-64348a880620)

Now let's test the robot by writing a program for forward movement.

## Instructions
1. Copy the code provided below and paste it into the code editor.
```
#include <lineRobot.h>

void setup() {
  robot.moveForwardSeconds(3);
}

void loop(){
}
```
2. Upload the program to the robot.
3. Observe the program execution results in the output and on the video feed.


## Conclusion
Wasn't hard, was it? But you have successfully acquired the skill to make the robot move. Now, you can proceed to the next lesson!
