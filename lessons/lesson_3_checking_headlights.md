# Lesson 3. Checking Headlights

## Lesson Objective
Learn how to use the `setup()`, `pinMode()` functions and how to turn on the LEDs on the robot.

## Introduction
In this lesson we will learn about some basic functions in the Wiring programming language for Arduino: `setup()` and `pinMode()`. We will also learn how to control the headlights on our robot.

## Step-by-step Instructions
1. First, copy the code provided below and paste it into the dedicated field of your program.
```
void setup() {
    pinMode(?, OUTPUT); //Initiates first LED pin
    pinMode(?, OUTPUT); //Initiates second LED pin
      
    digitalWrite(?, HIGH); //turn on first LED
    digitalWrite(?, HIGH); //turn on second LED
}
      
void loop() {
}
```
2. Upload the program to the robot by clicking on the "Upload" button.
3. Let's see the result: our robot turned on the headlights. Now let's learn what's happening in this code.

## Explanation of the Program Code
- Every Arduino program has two functions: `setup()` and `loop()`.
- The `setup()` function runs **only once** after the program starts. Inside this function, you can write code to execute other functions or set the pin mode.
- `pinMode(pin, mode)` configures the specified pin to behave either as an input or an output. Instead `pin` you should write the Arduino pin number to set the mode of, and replace `mode` with either `OUTPUT`(to provide voltage) or `INPUT`(to read voltage).
- We have already learned about the `digitalWrite()` function in previous lessons, we need it to apply voltage to the specified pin.

As a result of executing the program, the robot turned on its headlights. Let's do something more interesting.

## Exercise

### Checking Task
- Write a code that will turn on the headlights for 10 seconds and then turn them off.

### Self-checking Task
- Move the code for turning the headlights on and off into the body of the `loop()` function and see what happens.

## Conclusion
Congratulations! Today you learned about the `setup()` and `pinMode()` functions. In the next lesson, we will learn about the `loop()` function and add the ability for our robot to turn on a flashing light.