# Course lesson plan

Bolded items introduce new concepts in the lesson.

Italicized lessons are currently not considered due to reasons such as high complexity, limited significance, or implementation difficulties.

There are a total of 53 lessons. The average duration of lessons - ?

1) Introduction to the Robot
	- 1.1) "Test Drive" - Brief introduction and robot movement forward using **digitalWrite()**
	- 1.2) "Car Showroom" - Understanding the components of the robot, robot images with indicated main components.

2) Basics of Robot Programming
	- 2.1) "Headlight Check" - Controlling an LED, turning it on and off. **setup()** **pinMode()**
	- 2.2) "Emergency Signal" - Blinking an LED. **loop()**
	- 2.3) "Morse Code Message" - Transmitting an SOS signal. **int**

3) Robot Motion Control
	- 3.1) "Reversing" - Explanation of how to change the motor rotation direction. Forward and backward movement.
	- 3.2) "Maneuvering" -  Right and Left Turns.
	- 3.3) "Speed Record" - controlling robot speed and results displayed on camera **analogWrite()**

4) Functions
	- 4.1) "Turn Signals, Brake Lights, and Fog Lights" - Writing functions to control LEDs. **void**, **function**
	- 4.2) "Steering Wheel and Pedals" - Writing functions with arguments to control robot movement. **function arguments**

5) Encoders and Console Output
	- 5.1) "Odometer" - Measuring the distance traveled and displaying the result in the console. **Serial.print()**, **analogRead()**, **DOUBLE**, **Mathematical operations**
	- 5.2) "Speedometer" - Measuring the robot's speed and displaying it in the console.
	- 5.3) "Wheel alignment" - Measuring the steering angle and calibration to 90 degrees.

6) Conditional Statements and Time-based Operations
	- 6.1) "Fuel Indicator" - f the distance traveled reaches a certain value, an indicator turns on. When the robot has traveled some more, it stops.
	- 6.2) "The Route is Built" - Follow a specific route. For example travel a certain distance straight, then turn right, then turn left...
	- 6.3) "Compliance with the speed limit" - The robot gradually accelerates to a certain speed.
	- 6.4) "Drawing Lesson" - A trace is left behind the robot over the camera image. Instructions for drawing a certain figure.

7) Real-time Robot Control
	- 7.1) "Real-time Control" - Reading from the console and turning on the headlights based on the received messages.
	- 7.2) "Parking" - Reading from the console to control the robot. Task: park in a specific square.
		- *7.2.1) "Speed Parking"* - Sequentially park in three random squares within a specified time.
	- 7.3) "Drawing Lesson 2" - Free time to draw something without validation, but student have to write specific functions for drawing in real-time.

8) LED Matrix
	- 8.1) "Team Logo" - Display the team logo or sponsor advertisement on the LED matrix. Multiple logo options can be provided for selection. **Library Usage**
	- 8.2) "READY, SET, GO" - Countdown display on the matrix before the robot starts.
	- 8.3) "Animation" - Animation of the robot powering up. For example, the "power symbol" lights up with animation.
	- 8.4) "Scrolling Text" - Displaying text as a scrolling message using a library functions, and providing character codes so that the student can output their own message, like their name.

9) Line Sensor
	- 9.1) "Stop Line" - if Robot reaches the line then it should stop
	- 9.2) "Potholes in the Road" - If an obstacle is on the road, the robot should avoid it.
	- 9.3) "get on the track" - Automatic gitting onto the track, meaning if a track is encountered, the robot positions itself on the track.

10) Line Following
	- 10.1) "Relay Controller" - Relay controller function for correcting the position on the track to align perfectly.
	- 10.2) "First Lap" - Driving the track using the relay controller to stay on the track.
	- 10.3) "Home Competitions" - Adjusting parameters to beat the best home racer (just as a goal): completing the lap faster than the opponent.

11) Proportional (P) Controller
	- 11.1) "Proportional (P) Controller" - Proportional controller function for staying on the track, completing a lap using the P-controller
	- 11.2) "City Competitions" - Completing a lap in a specific time to secure a sponsor or join the best team. For example, choosing their emblem and displaying it on an LED matrix or something similar, displayed in the student's profile. It may be something else for the purpose of winning competitions.


12) PID Controller
	- 12.1) "PID Controller" - Working principle, function for staying on the track using a PID controller, completing a lap using the PID controller
	- 12.2) "World Championship" - Completing a lap in the best time to win the Best Racer Cup

13) Challenging Sections
	- 13.1) "Night Road" - Moving on the inverted map.
	- 13.2) "24-Hour Journey" - Moving first on the regular track and then automatically switching to the inverted map, then back.
	- 13.3) "Speed Bumps" - The road is interrupted, and several transverse lines appear; the task is to overcome this section.
	- 13.4) "Road Repair" - A piece of black surface is missing on the track, and the robot must continue moving along the track and find the continuation of the road.
	- 13.5) "Dangerous Turn" - Making a turn at an acute angle, finding the continuation of the route.
	- 13.6) "Color Sensor" - Reaching a yellow-colored road segment and checking the color sensor's output in the console.
	- 13.7) "Dirt Road" - A yellow patch on the track that needs to be traversed at a reduced speed.
	- 13.8) "Challenging Route" - Completing the entire route altogether.
		- *13.8.1) "Now for Speed"* - Completing the entire route within a specified time.

14) Smart City and Color Sensor
	- 14.1) "Learning Colors" - Using real-time control, drive to different color marks and record the results for verification.
	- 14.2) "Crossroads" - Decision-making at crossroads
	- 14.3) "Automated Parking" - Writing a parking function for the street, meaning the robot moves along the street until it finds a green mark (parking spot).
	- 14.4) "Way Home" - The task is to reach a point using lines, choosing the correct direction at the intersection. Simply recording the point's x and y coordinates and, therefore, choosing the next turn.
	- 14.5) "Circular Movement" - Instructions for the robot when moving in a circle.
	- 14.6) "Gas Stations" - Adding an internal counter for indicating fuel, and stopping at the gas station (red mark), if it needs.
	- 14.7) "Navigation"
		- 14.7.1) "Restoring Data" - All street lengths are known except one. The robot needs to measure the street using the robot and restore the lost data.
		- *14.7.2) "Building a Graph"* - Creating a graph from streets and their lengths. Better to write a library.
		- *14.7.3) "Finding the Optimal Path"* - Dijkstra's algorithm to find the optimal path. Better to write a library.
		- 14.7.4) "Following the Navigator" - Generating commands for the robot to follow the route obtained from the navigator.
		- 14.7.5) "Real-time Command Input" - Console input for moving from point A to point B.
		- *14.7.6) "GPS-based Localization"* - Not sure if this can be implemented. 
	- 14.8) "Pedestrian Zones" - Sections of a different color where the robot needs to reduce speed.
	- 14.9) "Taxi" - The task is to reach a location and pick up a passenger, then take them to their destination. The robot should follow all the above-mentioned rules: stop at gas stations, and reduce speed in pedestrian zones.
