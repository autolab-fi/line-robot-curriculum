---
index: 7
module: module_2
task: alarm
previous: headlights
next: None
---
# Lesson 7: Robot's alarm system

## Lesson objective
Strengthen your understanding of the gpio interface.

## Introduction
In this lesson, you will write a classic program to make an LED blink. This will help you become more confident in working with the gpio interface.

## Theory
In the previous lesson, you learned about gpio and LEDs. Now, let's take a closer look at how LEDs are connected.

<img src="https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/long_distance_race.png?raw=true" alt="led image" style="width:180px;"/>


An LED has two contacts - anode and cathode. The anode is the longer one and it is connected to pin 32, while the cathode is connected to the ground. Electric current can only flow through the LED in one direction, from the anode to the cathode. When we send a high signal to pin 32, electric current flows through the LED from the anode to the cathode. When we send a low signal, the electric current doesn't flow. Remember, current flows through the LED only from the anode to the cathode.

You already know how to turn on an LED using the **digitalWrite()** function. In this lesson, let's write a more advanced program. We'll not only turn on the LEDs on the robot but also turn them off by sending a low logic signal to the pin. To make the LEDs blink, you need to create pauses between switching signals on the LED pins so that the microcontroller doesn't execute them instantly. Remember, you can create pauses in different ways, and the simplest one is using the **delay()** function. For more information, you can review working with time functions in Arduino.

## Assignment
Write a program for the robot to turn on the LEDs for 1 second, then turn them off for 1 second, and repeat this indefinitely.

Remember, the LEDs are connected to pins 32 and 33.

## Conclusion
Congratulations! Now you know how to control logical signals using the GPIO interface in a more complex manner!