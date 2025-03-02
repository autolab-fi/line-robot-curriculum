# Lesson 9: Line Sensor and Black Line Detection

## Lesson Objective
Learn how to read data from an **Octoliner** sensor and detect black lines using an **ESP32**.

---

## Introduction
In this lesson, we will explore how an **IR line sensor** detects black and white surfaces. We will also write a program to read sensor data and determine whether the robot is on a black line.

---

## Theory

Line sensors use **infrared (IR) reflection** to detect black and white surfaces:

- **White surfaces** reflect more IR light, resulting in a **higher voltage**.
- **Black surfaces** absorb most of the IR light, resulting in a **lower voltage**.

### IR Sensor Working Principle:
![IR Sensor Working](../images/IRs.png)

In a typical **line-following robot**, an **array of IR sensors** detects the black track. The robot then adjusts its movement accordingly.

---

## Challenges
- Not all surfaces reflect IR light in the same way.
- Ambient light can interfere with sensor readings.
- The sensor readings might vary slightly, requiring calibration.

---

## Programming the Line Sensor

Let's write a program that:
1. Reads values from all **7 sensors**.
2. Checks if any sensor detects a **black line**.
3. Sends the sensor data and detection result.

### Example Code (To Be Completed by Students)
```cpp
#include <Octoliner.h>

// I2C Address (default 42)
Octoliner octoliner(42);

// Black threshold for detection
const int MY_BLACK_THRESHOLD = 100;  

void setup() {
    octoliner.begin();
    octoliner.setSensitivity(230);  // Adjust sensitivity if needed
}

void loop() {
    int value1 = octoliner.analogRead(1);
    
    // Complete the program by reading all 7 sensor values and detecting a black line.
}
