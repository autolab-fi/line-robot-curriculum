# **Lesson 1: Introduction to Variables and Conditional Statements**

## **Lesson Objective**

Learn how to declare and use variables in programming, and apply conditional logic using `if`, `else if`, and `else` statements to make decisions.

---

## **Introduction**

Variables are essential in microcontroller programming for storing information like sensor readings, motor speeds, and system states. In robot programming, we use conditional statements to make decisions based on these variables, creating intelligent behavior.

---

## **Theory**

### **What are Variables?**

Variables are named storage locations in the memory:

- `int motorSpeed = 200;` stores a motor speed value
- `float batteryLevel = 3.7;` stores the battery voltage
- `bool isOnLine = true;` stores whether the robot detects a line

### **What is an If-Else Statement?**

It enables your robot to **make decisions** based on conditions:

```cpp
if (condition1) {
    // code runs if condition1 is true
} else if (condition2) {
    // code runs if condition1 is false but condition2 is true
} else {
    // code runs if all conditions above are false
}
```

### **Comparison Operators**

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

---

## **Example Implementation**

```cpp
#include <Arduino.h>
#include <lineRobot.h>  // Includes printMQTT function

// Define pins
const int ledPin = 2;
const int sensorPin = 36;  // Analog sensor pin

void setup() {
  pinMode(ledPin, OUTPUT);

  printMQTT("Sensor Monitoring Started");
}

void loop() {
  // Read sensor value
  int sensorValue = analogRead(sensorPin);

  // Make decision based on threshold
  if (sensorValue > 2000) {
    digitalWrite(ledPin, HIGH);
    printMQTT("Sensor value HIGH");
  } else {
    digitalWrite(ledPin, LOW);
    printMQTT("Sensor value LOW");
  }

  delay(100);  // Small delay for stability
}
```

---

## **Understanding the Logic**

1. The program reads an analog sensor value.
2. The `if` statement compares this value against a threshold (2000).
3. If the value is above the threshold, the LED turns ON and "Sensor value HIGH" is sent.
4. Otherwise (`else`), the LED turns OFF and "Sensor value LOW" is sent.

---

## **Assignment: Dual-Sensor Line Detection**

In this assignment, you'll use two of the Octoliner sensors to detect line positions and send appropriate messages to the MQTT dashboard.

Your task is to:

1. Compare both sensor values (value_1 and value_2)
2. Use if-else if-else logic to determine different conditions
3. Send different messages based on which sensors detect the line

Complete the code below by adding the conditional logic:

```cpp
#include <Octoliner.h>
#include <lineRobot.h>

// I2C Address (default 42)
Octoliner octoliner(42);

void setup() {
    octoliner.begin();
    octoliner.setSensitivity(230);
}

void loop() {
    // Read values from two sensors
    int value_1 = octoliner.analogRead(5);
    int value_2 = octoliner.analogRead(6);

    // YOUR CODE HERE:
    // Add if-else if-else statements to determine which sensor(s) detect the line
    // Remember: Values greater than 200 indicate the sensor is on the line
    // Send appropriate messages via printMQTT

}
```

### Expected Output

Your code should detect and report one of the following condition:

- If only sensor 5 is on the line: "SENSOR 5 ON LINE & SENSOR 6 OFF LINE"
- If only sensor 6 is on the line: "SENSOR 6 ON LINE & SENSOR 5 OFF LINE"

---

## **Conclusion**

In this lesson, you learned how variables store different types of data and how conditional statements make decisions based on those values. The `if-else if-else` structure lets you create more complex logic for your robot to respond to different sensor combinations, which is essential for creating responsive robot behavior.
