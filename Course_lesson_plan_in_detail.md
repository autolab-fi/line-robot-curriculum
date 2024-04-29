# Course Lesson Plan

## Contents
- [Introduction to the Robot](#introduction-to-the-robot)
- [Controlling Robot Movement](#controlling-robot-movement)
- [Understanding the Robot's Brain](#understanding-the-robots-brain)
- [Controlling LEDs](#controlling-leds)
- [Controlling Motors](#controlling-motors)
- [Encoders](#encoders)
- [Controllers](#controllers)
- [New Motion Logic](#new-motion-logic)
- [Line and Color Sensor](#line-and-color-sensor)
- [LED Matrix](#led-matrix)
- [Smart City](#smart-city)

### Introduction to the Robot
Getting familiar with the platform. How to control the robot.
0. "Drawing" - Introduction to the platform, list of all peripherals, what we will be working with, any restrictions on libraries and tag words.
1. "Test Drive" - Some introductory words and moving the robot forward using a library.
2. "Driver's License" - Writing a simple program similar to the previous lesson independently.

### Controlling Robot Movement
Demonstrating the robot's capabilities.

1. "Short distance race" - Library functions for moving a specific distance. Forward and backward movement.
2. "Maneuvering" - Turning right and left in place. Task: read data from a file and write it to another.
3. "Fruit Ninja" - Write a program with a sequence of commands for moving along a trajectory depicted on the scheme.

### Controlling LEDs
Basic functions of working with gpio using LEDs as examples.

1. "Headlights" - How LEDs work. Task: turning on LEDs.
2. "Robot's alarm system" - More about digitalWrite(), pinMode() functions. Task: blinking LEDs.

### Controlling Motors
What are DC motors, how to control them via a driver, concept of PWM.

1. "Electric Motor" - Basic principles of DC motors. Task: get the robot moving by sending a signal to the driver.
2. "Robot Movement" - PWM and analogWrite(), information about the driver, a bit about robot kinematics. Task: implement turning by sending a signal to the driver.

### Encoders
What are encoders, solving the problem of turning to a given angle. Studying robot kinematics.

1. "Encoder" - What is an encoder, how it can be used. Task: add a condition to the prepared code for reading data from encoders so that the robot stops when it receives data corresponding to a certain average value.
2. "Odometer" - What is an odometer device, detailed description of implementation and functions. Task: write an odometer that will convert data from encoders into centimeters, and the robot will stop after covering a certain distance.
3. "Working with File System" - Reading, writing files on ESP32. Task: read text from a file, then write the text from this file to another file.
4. "Speedometer" - What is a speedometer, how it can be implemented using distance data. Task: implement a speedometer that measures the average speed of the robot's movement.
5. "Steering Adjustment" - More information about robot kinematics, solving the problem of tracking the robot's angle of rotation. Task: write code to rotate the robot by 90 degrees.

### Controllers
**Still challenging with checks, but ideas are there**
A simple version of automatic control theory using several simple controllers as examples.

1. "Relay Controller" - What are controllers, why they are needed (open-loop and closed-loop systems), what is a relay controller, how it works, where it is used. Task: implementation of a relay controller for turning the robot.
2. "P-Controller" - What is a P-controller, why it is better than a relay. Task: implementation of turning with a P-controller.
3. "PI-Controller" - Drawbacks of a P-controller. Eliminating steady-state error using the integral component. Task: implementation of turning with a PD-controller.
4. "PID-Controller" - What is a differential component and how it helps eliminate overshoot. Task: implementation of turning with a PD-controller.
5. "Methods of Tuning PID-Controller" - Ziegler-Nichols method for tuning coefficients. Maybe without a task.

### New Motion Logic
**Still challenging with checks, but ideas are there**
Writing our own library for the robot, writing motion functions, learning to divide code into blocks, applying controllers to improve motion, optimizing motion.

1. "Motion Library" - Why do we need a library. Functions for reading data from encoders.
2. "Straight Motion" - Improving straight motion using a controller. Task: apply a controller to improve straight motion.
3. "Automatic Transmission" - Improving motion functions with a speed controller.
4. "Turning Functions" - Turning the robot to a specific angle, angle passed as an argument.

### Line and Color Sensor
Working with a line sensor, solving the line tracking task. Working with a color sensor. Algorithms for complex robot movements. Simple noise filter for line sensors.

For a simple track:
1. "Line Sensor" - What is a line sensor and how does it work. How to read data, add a function to read data from the sensor to the library. Task: the robot should travel 50 cm and record data from the sensors along the way, which will then be compared to the expected data in percentage.
2. "Track Entry" - A bit about calibration (without calibration functions just for general understanding). (Possibly about working with a library for reading data from sensors) Algorithm idea for entering the track. Task: write an algorithm for automatic entry onto the track, i.e., if the track is encountered on the way, the robot stops on the track.
3. "Line Following" - line following algorithm. Task: implement line following using a simple algorithm.
4. "Noise Filter" - moving average filter to average data obtained from sensors.
5. "Line Tracking Controller" - Controllers for line following. P, PD, or PID. Task: go around a circle within a certain time.
6. "Colorful World" - What is a color sensor and how does it work. How to read data from the sensor. Task: travel n centimeters and record data from the sensor.

For a more complex track:
1. "Night Road" - Algorithm for track navigation if there is a section with inverted color on it.
2. "Speed Bumps" - The road is interrupted and several transverse lines begin, the task is to overcome this section. Example algorithm: if all sensors are activated, the robot needs to slow down and drive straight until it finds the continuation of the usual track.
3. "Road Repair" - There is a missing piece of black pavement on the track, the robot must continue along the track and find the continuation of the road. Example algorithm: sweeping movements on the map.
4. "Dirt Road" - There is a yellow patch on the track that needs to be traversed at a reduced speed.

### LED Matrix
Working with a LED matrix, shift registers.
1. "Team Logo" - What is a LED matrix? How do shift registers work? Connecting the library for controlling the LED matrix. Task: sequentially light up several specific pixels.
**Simple Tasks**
2. "READY, SET, GO" - Displaying a countdown to the robot's start on the matrix // "Animation" - animation of the robot turning on. For example, with an animation, the "power" symbol lights up.
3. "Scrolling Text" - Displaying text as a scrolling message using the library, also provide character codes for the student to display their own message, for example, their name...

### Smart City
Requires a separate field, line sensors, color sensor. High level of difficulty. In these lessons, you can delve into complex algorithms and graphs.

1. "Intersection" - Defining an intersection, how to make decisions when moving at an intersection and drive onto the desired road.
2. "Autoparking" - Writing a function for parking on the street, i.e., the robot drives down the street until it finds a parking space (a colored mark).
3. "Road to Home" - Selection algorithm: the robot is in an unknown location, but it is known that the angle between the robot's direction vector and the direction vector to the point is no more than 90 degrees -> at each intersection, we look at which coordinate has a greater difference, turn in that direction. The task is to reach the point along the lines, choosing the right direction at each intersection.
4. "Circular Movement" - Instructions for the robot when moving in a circle. **Questions in implementation, needs testing**
5. "Gas Stations" - Adding an internal fuel counter to keep track of fuel, if the robot has traveled a lot, it needs to stop at a gas station ("red mark") when passing by.
6. "Navigator" - **can be expanded**
	1. "Data Recovery" - knowing the lengths of all streets except one. Measure the street with the robot and restore the lost data.
	2. *"Graph Construction"* - concept of a graph. examples of different graphs, examples of implementing different graphs. creating a graph from streets and their lengths. **It's better to just have this list.**
	3. *"Optimal Path Construction"* - Dijkstra's algorithm for finding the optimal path. **Interesting, but can be difficult**
	4. "Following the Navigator" - generating commands for the robot to move along the received route from the navigator. Task: travel along the route from the current known position to the specified street.
7. "Pedestrian Zones" - sections of a different color where speed must be reduced.
8. "Taxi" - need to reach a location and pick up a passenger, then take