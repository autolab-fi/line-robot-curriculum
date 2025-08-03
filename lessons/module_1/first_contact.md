# First Contact with Mars Rover

## Overview
In this introductory lesson, students will familiarize themselves with the Mars rover platform, its key components, and basic control systems. This foundation is essential for all future Mars exploration missions.

## Learning Objectives
- Understand the basic components of the Mars rover
- Learn the control interface and basic commands
- Master system initialization and status checking
- Perform basic movement operations

Let's imagine that you have to control remotely a Mars rover named Rover. Rover is equipped with various components that help it explore the red planet. Let's take a closer look at these components:

### 1. Mars Rover Components
- Drive system
- Sensor array
- Power management system
- Communication module

### System Initialization
In order to control Rover effectively, we need to initialize marsRover library. In C++ we can do it as follows:

```cpp
#include <marsRover.h>

void setup() {
}

void loop() {

}
```
_void setup()_ is a function that is called once at the beginning of the program.

_void loop()_ is a function that is called repeatedly in the program.

### 2. Control Interface
- Command structure
- System initialization
- Basic movement commands
- Status monitoring

In order to move rover, we need to use the following commands:
- move(_distance_)
- rotate(_angle_)
inside setup or loop funciton

```cpp
#include <marsRover.h>
void setup(){
   robot.move(20);
   robot.rotate(180);
   robot.move(20);
}
void loop(){
}
```
_

### 3. Safety Procedures
- Pre-operation checks
- Emergency protocols
- System limitations

Pre-operation checks:
- Rover must have power
- Rover must have connection to the network

You can check it in right bottom window it must have green background

If something went wrong you always can stop execution of robot by pressing STOP button



## Practical Exercises: Perimeter check
You must check perimeter by making Rover move around the perimeter, use square with side length 20

```cpp
#include <marsRover.h>
void setup(){
    // you code here
}
void loop(){
}
```
### System limitations

If you try to send signal to Mars it might take a long time to receive response due to distance and signal propagation delay.
In this simulation we also have limitations:
1. Code must be compiled and uploaded to the rover, it might take 30-40 seconds
2. Rover shared among multiple users so you might need to wait for other users to finish their tasks
3. Stream of the robot will be available only during eacution of your code on Rover after stream you will have video recoding of your code execution
4. Only 3 latest video available for each user

Now you can start your first exercise, write the code and hit VERIFY button.
Good luck!
