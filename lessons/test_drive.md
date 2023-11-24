---
index: 1
module: module_1
task: test_drive
previous: draw
next: license_to_drive
---
# Lesson 1. Test drive

## Lesson objective
Get started with the robot and set it in motion promptly.

## Introduction
In this lesson, you will learn how to initiate movement in the robot. It's not a complex task; all you need is a strong desire and perseverance.

Below is a photo of the robot.
_edit_photo_
![image](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/robot.png?raw=true)

Let's test the robot by writing a program for forward movement.

## Step-by-step Instructions
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
Congratulations! You have successfully acquired the skill to make the robot move. Now, you can proceed to the next lesson!
