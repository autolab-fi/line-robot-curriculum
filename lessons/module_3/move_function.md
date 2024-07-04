# Lesson 9: Movement Function

## Lesson Objective
Learn how to write your own functions.

## Introduction
In this lesson, you will learn how to write your own functions in Arduino Wiring.

## Theory

In Lesson 2, "License to Drive," you were introduced to the concept of functions. Now, you can write your own functions to make your code more compact and readable.

### Types of Functions

Functions can return values, such as numbers, characters, strings, etc. To specify the type of data a function returns, you need to indicate the function's type. Let's explore functions that return values and those that do not.

### Functions Returning Values

Example of an **int** function:

```cpp
int sum(int num1, int num2){
    return num1 + num2;
}
void setup(){
    int a = 10;
    int b = 5;
    int result = sum(a, b);
}
...
```

The **sum(a, b)** function in the example takes numbers **num1** and **num2** as parameters and returns their sum, which can be stored in a variable. Thus, the variable **result** will hold the value 15.

Functions that return values must have a **return** statement, which ends the function's execution and returns the specified value.
Examples:
```cpp
...
return 0;
```
This function returns 0.
```cpp
...
return 'L';
```
This function returns a **char** data type, specifically the character **'L'**.

### Functions Not Returning Values

In the previous section, you learned about functions that return values. However, there are also functions that do not return anything. These functions use the special type **void**. A void function does not require a return statement since it returns nothing.

Example:
```cpp
...
void moveRobotForwardBackward(int secondsMove, int secondsPause){
    int milliSeconds = secondsPause * 1000;
    robot.moveForwardSeconds(secondsMove);
    delay(milliSeconds);
    robot.moveBackwardSeconds(secondsMove);
}
void setup(){
    moveRobotForwardBackward(3, 1);
    moveRobotForwardBackward(5, 10);
}
...
```

The **moveRobotForwardBackward** function takes the parameter **secondsMove**, which tells the robot how long to move forward and backward, and the parameter **secondsPause**, which specifies the pause before the robot moves backward.

## Assignment
Write a program that makes the robot turn approximately 180 degrees.

You can use the functions **startMotorSpeedLeft(speed)**, **startMotorSpeedRight(speed)**, **stopMotorRight()**, and **stopMotorLeft()**. The functions **moveForwardDistance**, **moveBackwardDistance**, **turnLeft**, **turnRight**, **moveForwardSeconds**, and **moveBackwardSeconds** will not work.

### Hint
We recommend writing your own movement function. You can design it to accept several parameters, such as separate speeds for the motors and time, or just the execution time with fixed speeds.

## Conclusion
Congratulations! In this lesson, you learned how to write your own function, allowing you to organize your code more efficiently.