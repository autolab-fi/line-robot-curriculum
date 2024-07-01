# Lesson 8: Electric Motor

## Lesson objective
Lear about electric motors.

## Introduction
In this lesson, you will learn about electric motors and the basic principles of DC motors.

## Theory
### What is Electric motor?

An electric motor is a device that converts electrical energy into mechanical energy using a magnetic field.

There are various classifications of electric motors, but they are mainly classified by the type of power supply voltage:
- Direct Current (DC) motors
- Alternating Current (AC) motors: asynchronous and synchronous

And by the method of power transmission:
- Brushed motors
- Brushless motors


In this lesson, we will take a closer look at direct current motors, also known as DC motors. DC motors are brushed motors, and we will examine how they work without delving deeply into the physics and mathematics!

### Structure of an Electric Motor

![image](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_3/inside_motor.png?raw=True)

An electric motor consists of a stator and a rotor. The stator creates a constant magnetic field, which in our case is provided by permanent magnets. The rotor is the rotating part and consists of a shaft with windings on several coils.


### Principle of Operation

1. Voltage of different polarities is applied to the brushes; one brush has a negative potential, and the other has a positive potential.
2. The potential from the brushes is transferred to the coil windings.
3. The coils generate a magnetic field with corresponding polarity: the coil with the negative potential generates a north pole magnetic field, while the coil with the positive potential generates a south pole magnetic field.
4. The polarities of the magnetic fields on the rotor coils match the polarity of the corresponding permanent magnets on the stator, causing them to repel each other since like charges repel.
5. The rotor rotates, and by inertia, the coil reaches the brush with the opposite potential, causing the coil to remagnetize. The polarity on the rotor coil again matches the polarity of the permanent magnet on the stator. This process continues, keeping the rotor in motion as long as there is voltage on the brushes.

You can also observe the principle of operation in the GIF image below, where each coil changes polarity as it moves due to the potential from the brushes:

![image](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_3/animation.gif?raw=True)

### Gearbox in Electric Motors

An electric motor can also be equipped with a gearbox, which transfers the rotational motion from the motor shaft to the mechanism. A gearbox can increase the maximum torque from the motor shaft and reduce the rotational speed. In the case of a line-following robot, the gearbox increases torque to allow the robot to move despite its weight and to overcome obstacles. A gearbox typically consists of a set of gears. You can see the internal structure of a gearbox in the photo below:

![image](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_3/small_size_gearbox.png?raw=True)



### Controlling Motor
In the **lineRobot** library, functions for controlling the motors are already written, and they can be used to control the motors individually.

The function **moveLeftMotorSpeed(speed)** is used to send a signal to the motors, with the speed parameter specified as a percentage. The speed can be either negative or positive, ranging from -100 to 100. When the parameter is greater than 0, the left wheel will rotate forward, and if the parameter is less than 0, the wheel will rotate in the opposite direction. IMPORTANT! These functions only start the motors; they do not stop them. To stop the motors, you can use specified function or provide 0 as parameter for the funtion **moveLeftMotorSpeed(speed)**.

The function **moveRightMotorSpeed(speed)** works similarly for the right motor.

To stop the motors, use the functions **stopMotorRight()** and **stopMotorLeft()**.

## Assignment
Write a program for the robot so that it navigates around two cones. The robot will have only 20 seconds to complete this maneuver. To succeed, it needs to follow an optimal trajectory. The best trajectory would be a figure-eight, which can be achieved using the new functions to control each motor individually.

![image](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_3/trajectory.png?raw=True)


## Conclusion
Congratulations! In this lesson, you learned about the structure of a simple electric motor. Electric motors are a fascinating area in robotics, with a wide variety of types, each having its own application.