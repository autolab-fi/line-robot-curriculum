Your lesson is already well-structured and clean! I made a few minor refinements for consistency and clarity. Here’s the **cleaned-up version**:

---

# **Lesson 10: Implementing Line Following with an IR Sensor**  

## **Lesson Objective**  
Learn how to program an **ESP32-based robot** to follow a black line using an **Octoliner** IR sensor array.  

---  

## **Introduction**  
In this lesson, we will use an **IR line sensor array** to detect and follow a black line. The robot will read sensor values, determine the line's position, and adjust its movement accordingly.  

---  

## **Theory**  

A **line-following robot** uses an array of **infrared (IR) sensors** to detect the track. These sensors measure reflected IR light, distinguishing between black (low reflection) and white (high reflection).  

- **Middle sensors detect the line** → Robot moves forward.  
- **Left sensors detect the line** → Robot turns left.  
- **Right sensors detect the line** → Robot turns right.  

### **IR Sensor Configuration**  
The **Octoliner** sensor array has **8 sensors**, each providing an analog value indicating the intensity of reflected IR light.  

![IR Sensor Logic](https://github.com/pranavk-2003/line-robot-curriculum/blob/main/images/module_6/IR_sensor_array.png)  

In this lesson:  
- **Central sensors (3 & 4)** → Move straight  
- **Left sensors (0,1,2)** → Guide left turns  
- **Right sensors (5,6,7)** → Guide right turns  

---  

## **Challenges**  
- **Sensor calibration**: The black line's reflectivity can vary, affecting detection accuracy.  
- **Speed balancing**: The robot must maintain smooth turns without jerking.  
- **Noise filtering**: Some sensors may provide fluctuating readings, requiring stability checks.  

---  

## **Programming the Line Following Algorithm**  

This code will:  
1. **Read** sensor values from all 8 sensors.  
2. **Decide** the robot's movement based on sensor readings.  
3. **Move** forward, turn left, turn right, or stop.  

### **Code Implementation**
```cpp
#include <Octoliner.h>
#include <lineRobot.h>

// I2C Address (default 42)
Octoliner octoliner(42);

// Black threshold for detection
const int MY_BLACK_THRESHOLD = 100;  
int fwdspeed = 30;
int turnspeed = 40;

void setup() {
    digitalWrite(15, HIGH);
    octoliner.begin();
    octoliner.setSensitivity(230);  // Adjust sensitivity if needed
    robot.moveBackwardDistance(15); // Initial backward movement
    robot.turnLeft(); // Initial turn to position robot
}

void loop() {
    int sensorvalues[8];

    // Read all sensor values
    for (uint8_t i = 0; i < 8; i++) {
        sensorvalues[i] = octoliner.analogRead(i);
        printMQTT(sensorvalues[i]);  // Send data for debugging
    }

    // Move forward if the middle sensors detect the line
    if (sensorvalues[3] > MY_BLACK_THRESHOLD || sensorvalues[4] > MY_BLACK_THRESHOLD) {
        robot.runMotorSpeedRight(fwdspeed);
        robot.runMotorSpeedLeft(fwdspeed);
    }
    // Turn left if the left sensors detect the line
    else if (sensorvalues[0] > MY_BLACK_THRESHOLD || sensorvalues[1] > MY_BLACK_THRESHOLD || sensorvalues[2] > MY_BLACK_THRESHOLD) {
        robot.runMotorSpeedLeft(turnspeed);
        robot.runMotorSpeedRight(fwdspeed / 2);
    }
    // Turn right if the right sensors detect the line
    else if (sensorvalues[5] > MY_BLACK_THRESHOLD || sensorvalues[6] > MY_BLACK_THRESHOLD || sensorvalues[7] > MY_BLACK_THRESHOLD) {
        robot.runMotorSpeedLeft(fwdspeed / 2);
        robot.runMotorSpeedRight(turnspeed);
    }
    // Stop if no sensors detect the line
    else {
        robot.runMotorSpeedRight(0);
        robot.runMotorSpeedLeft(0);
    }
}
```

---

## **Understanding the Logic**  

### **Sensor Detection and Movement**  

The robot determines movement based on which sensors detect the black line.  
Below is a flowchart for a clear understanding:  

![Flow](https://github.com/pranavk-2003/line-robot-curriculum/blob/main/images/module_7/FC.png)  

1. **If middle sensors (3 OR 4) detect the line** → Move forward.  
2. **If left sensors (0 OR 1 OR 2) detect the line** → Turn left.  
3. **If right sensors (5 OR 6 OR 7) detect the line** → Turn right.  
4. **If no sensor detects the line** → Stop.  

---

## **Assignment**  
Modify the program to:  
1. **Fine-tune** motor speeds for smoother movement.  
2. **Add debugging messages** to print which sensors detect the line.  
3. **Experiment with different thresholds** to improve accuracy.  

---

## **Conclusion**  
Congratulations! You have successfully programmed a **line-following robot** using an **Octoliner IR sensor**. 🚀  

In the next lesson, we will optimize the robot’s movement using **PID control** for precise line tracking! 🔥  

---

This version keeps everything **clear, consistent, and structured**, with better spacing and readability. 🚀
