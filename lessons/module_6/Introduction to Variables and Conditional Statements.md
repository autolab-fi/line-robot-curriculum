# **Lesson 1: Introduction to Variables and Conditional Statements**

## **Lesson Objective**

Learn how to declare and use variables in ESP32 programming, and apply conditional logic using `if` and `else` statements to make decisions.

---

## **Introduction**

Variables are essential in microcontroller programming for storing information like sensor readings, motor speeds, and system states. In robot programming, we use conditional statements (`if-else`) to make decisions based on these variables, creating intelligent behavior.

---

## **Theory**

### **What are Variables?**

Variables are named storage locations in the ESP32's memory:

- `int motorSpeed = 200;` stores a motor speed value
- `float batteryLevel = 3.7;` stores the battery voltage
- `bool isOnLine = true;` stores whether the robot detects a line

### **What is an If-Else Statement?**

It enables your robot to **make decisions** based on conditions:

```cpp
if (condition) {
    // code runs if condition is true
} else {
    // code runs if condition is false
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

// Define pins
const int ledPin = 2;      // ESP32 onboard LED
const int sensorPin = 36;  // Analog sensor pin

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  
  Serial.println("ESP32 Sensor Monitoring");
}

void loop() {
  // Read sensor value
  int sensorValue = analogRead(sensorPin);
  
  // Make decision based on threshold
  if (sensorValue > 2000) {
    digitalWrite(ledPin, HIGH);
    Serial.println("Sensor value HIGH");
  } else {
    digitalWrite(ledPin, LOW);
    Serial.println("Sensor value LOW");
  }
  
  delay(100);  // Small delay for stability
}
```

---

## **Understanding the Logic**

1. The program reads an analog sensor value.
2. The `if` statement compares this value against a threshold (2000).
3. If the value is above the threshold, the LED turns ON and "HIGH" is printed.
4. Otherwise (`else`), the LED turns OFF and "LOW" is printed.

---

## **Assignment: Line Detection with ESP32**

For this assignment, you'll use the Octoliner sensor to detect whether the robot is on a black line.

Your task is to:
1. Compare the sensor value.(Sensor value is > 200 if its on the line else its <200)
2. Print the appropriate message to the MQTT Dashboard

Complete the code below by adding the `if-else` statement:

```cpp
#include <Octoliner.h>
// I2C Address (default 42)
Octoliner octoliner(42);
// Black threshold for detection
const int MY_BLACK_THRESHOLD = 100;  

void setup() {
    Serial.begin(115200);  // Initialize Serial communication
    octoliner.begin();
    octoliner.setSensitivity(230);  // Adjust sensitivity if needed
    Serial.println("Line Detection Program Started");
}

void loop() {
    int value = octoliner.analogRead(5);
    
    // YOUR CODE HERE:
    // Add an if-else statement to determine if the robot is on the line
    // Print "ON LINE" or "OFF LINE" accordingly
    
    delay(100);  // Small delay between readings
}
```

---

## **Conclusion**

In this lesson, you learned how variables store different types of data and how `if-else` statements make decisions based on those values. These are fundamental concepts for creating responsive robot behavior that reacts to sensor inputs from the environment.
