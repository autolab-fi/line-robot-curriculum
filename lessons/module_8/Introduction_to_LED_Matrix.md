# **Lesson 1: Arrays and LED Matrix Display with Loops**

## **Lesson Objective**

Learn how to use arrays to create and display patterns on an 8x8 LED matrix using I2C.

---

## **Introduction**

LED matrices are grids of LEDs arranged in rows and columns. Controlling an LED matrix efficiently often involves using arrays to represent patterns. With I2C communication, sending data to the matrix is simple and requires only a few wires.

---

## **Theory: Representing LED Patterns with Arrays**

### **8x8 Grid as an Array**

Each row of the LED matrix can be represented by a byte (`uint8_t`), where each bit corresponds to an LED:

- `0` = OFF
- `1` = ON

```cpp
uint8_t smiley[8] = {
    0b00111100,
    0b01000010,
    0b10100101,
    0b10000001,
    0b10100101,
    0b10011001,
    0b01000010,
    0b00111100
};
```

This creates a smiley face.

---

## **Required Library**

Use the **MD_MAX72XX** library. Below is a simplified example using a generic I2C library interface:

```cpp
#include <Wire.h>
#define LED_MATRIX_ADDR 0x70

void sendPattern(uint8_t pattern[8]) {
    Wire.beginTransmission(LED_MATRIX_ADDR);
    for (int i = 0; i < 8; i++) {
        Wire.write(i);         // Row address
        Wire.write(pattern[i]); // Pattern for that row
    }
    Wire.endTransmission();
}
```

---

## **Example Implementation**

```cpp
#include <Wire.h>

#define MATRIX_ADDR 0x70

uint8_t Xpattern[8] = {
    0b10000001,
    0b01000010,
    0b00100100,
    0b00011000,
    0b00011000,
    0b00100100,
    0b01000010,
    0b10000001
};

void setup() {
    Wire.begin();
    printMQTT("LED Matrix Pattern Display");
}

void loop() {
    displayPattern(Xpattern);
}

void displayPattern(uint8_t pattern[8]) {
    Wire.beginTransmission(MATRIX_ADDR);
    for (int i = 0; i < 8; i++) {
        Wire.write(i);          // Row index
        Wire.write(pattern[i]); // Binary row data
    }
    Wire.endTransmission();
}
```

---

## **Assignment: Design and Display Your Own Pattern**

## **Conclusion**

By using arrays, loops, and I2C communication, we can create complex LED patterns and even simple animations. This builds the foundation for visual indicators, pixel art, and games on embedded systems.

---
