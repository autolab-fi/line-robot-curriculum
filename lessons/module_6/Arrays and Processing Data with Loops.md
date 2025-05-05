# **Lesson 3: Arrays and Processing Sensor Data with Loops**

## **Lesson Objective**

Understand how to use arrays.

---

## **Introduction**

Arrays allow you to store multiple values under one name. For robotics applications, arrays are perfect for handling multiple sensor readings, motor values, or LED patterns. Instead of creating separate variables for each sensor, arrays group them together, making it easier to loop through and analyze data.

---

## **Theory**

### **What is an Array?**

An array is a fixed-size collection of elements of the same type.  
Example:

```cpp
int sensorValues[8] = {325, 410, 102, 890, 512, 78, 210, 455};
```

### **Accessing Elements**

You can access array items using indexes (starting from 0).  
`sensorValues[0]` → 325 (first sensor)  
`sensorValues[3]` → 890 (fourth sensor)

### **Looping Through Arrays**

Use a `for` loop to process all elements.

```cpp
for (int i = 0; i < 8; i++) {
    Serial.print("Sensor ");
    Serial.print(i);
    Serial.print(": ");
    Serial.println(sensorValues[i]);
}
```

---

## **Example Implementation**

```cpp
#include <Arduino.h>

void setup() {
    Serial.begin(115200);
    Serial.println("Array Example");
}

void loop() {
    // Sample light sensor readings
    int lightLevels[6] = {855, 230, 990, 470, 600, 120};
    int brightCount = 0;

    // Process the array with a loop
    for (int i = 0; i < 6; i++) {
        if (lightLevels[i] > 500) {
            brightCount++;
            Serial.print("Sensor ");
            Serial.print(i);
            Serial.println(" detects bright light");
        }
    }

    Serial.print("Number of bright sensors: ");
    Serial.println(brightCount);

    delay(3000); // Wait 3 seconds before repeating
}
```

---

## **Understanding the Logic**

1. The program has an array of 6 light sensor readings.
2. A loop checks each reading using an `if` condition.
3. If the value is greater than 500, it's considered "bright" and counted.
4. Each bright sensor is reported, and the total count is displayed.
5. This same approach can be used to process any type of sensor data.

---

## **Advanced Array Techniques**

### **Finding the Maximum Value**

```cpp
int maxValue = sensorValues[0];
int maxIndex = 0;

for (int i = 1; i < 8; i++) {
    if (sensorValues[i] > maxValue) {
        maxValue = sensorValues[i];
        maxIndex = i;
    }
}

Serial.print("Highest reading at sensor ");
Serial.println(maxIndex);
```

### **Updating Array Values**

```cpp
// Calibrate by subtracting baseline from all values
int baseline = 100;
for (int i = 0; i < 8; i++) {
    sensorValues[i] -= baseline;
}
```

---

## **Assignment: Line Follower Sensor Array Analysis**

For this assignment, you'll create a program that:

1. Reads all 8 Octoliner sensors and stores the values in an array
2. Processes the array to determine which sensors detect the line
3. Uses printMQTT to report which sensors are over the line

Complete the code below:

```cpp
#include <Octoliner.h>
#include <lineRobot.h>

// I2C Address (default 42)
Octoliner octoliner(42);
// Black threshold for detection
const int BLACK_THRESHOLD = 100;

void setup() {
    Serial.begin(115200);
    octoliner.begin();
    octoliner.setSensitivity(230);  // Adjust sensitivity if needed
    printMQTT("Line Sensor Array Analysis Started");
}

void loop() {
    // YOUR CODE HERE:
    // 1. Create an array with 8 elements
    // 2. Use a for loop to store all sensor readings in the array
    // 3. Use another for loop to check which sensors detect the line
    // 4. Use printMQTT to report which sensors detect the line

}
```

Expected output:
When a sensor detects the line, it should send a message like: "Sensor 3 is ON THE LINE"

---

## **Conclusion**

Arrays are powerful tools for working with multiple related values in your robot programs. By combining arrays with loops and conditional statements, you can efficiently analyze sensor data, detect patterns, and make decisions based on multiple inputs. This approach is essential for more complex robotic behaviors like line following, obstacle avoidance, and sensor fusion.
