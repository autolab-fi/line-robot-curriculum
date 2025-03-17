# Lesson 1: Relay Controller

## Lesson Objective
Understand relay controllers and their role in open-loop and closed-loop systems.

## Introduction
A controller is a system that manages the behavior of a device or process. Controllers are essential in automation, ensuring that a system functions as desired. There are two main types of control systems:

1. **Open-loop systems**: These operate without feedback. The controller sends commands without knowing the actual output (e.g., turning on a heater for 10 minutes without checking the temperature).
2. **Closed-loop systems**: These use feedback to adjust their behavior, ensuring more precise control (e.g., an air conditioner adjusting cooling based on room temperature).

## Theory

### What is a Relay Controller?
A relay controller is a simple type of control system that switches between two states (ON/OFF) based on a set condition. It works like a basic thermostat, where the system turns ON when the temperature is below a threshold and OFF when it exceeds a limit.

A relay controller follows this rule:

$$
 u(t) = \begin{cases} 
    U_{max}, & \text{if } e(t) > 0 \\
    U_{min}, & \text{if } e(t) \leq 0 
\end{cases} 
$$

where:
- \( u(t) \) is the control output,
- \( e(t) \) is the error (difference between desired and actual value),
- \( U_{max} \) and \( U_{min} \) are the two possible output states.

### Limitations of Relay Controllers
- They can cause oscillations because they switch between extreme values.
- Lack of fine control, leading to inefficiencies.
- Not suitable for smooth adjustments required in robotics.

**Note:** We already implemented a relay controller in the last lesson.

---

# Lesson 2: P-Controller

## Lesson Objective
Learn about P-controllers and their advantages over relay controllers.

## Introduction
In previous lessons, we used relay controllers to control movement. However, relay controllers switch between on and off states, which can cause oscillations and inefficiencies. A P-controller provides a smoother and more stable control by adjusting the output proportionally to the error.

## Theory

### What is a P-Controller?
A Proportional (P) controller is a type of feedback control system that uses a proportional gain to adjust the control output based on the error between the desired and actual values. The control law is given by:

$$
 u(t) = K_p \cdot e(t) 
$$

where:
- \( u(t) \) is the control output,
- \( K_p \) is the proportional gain,
- \( e(t) \) is the error (desired value - actual value).

### Block Diagram
![P Controller](https://github.com/pranavk-2003/line-robot-curriculum/blob/main/images/module_7/p.png)

## Assignment
Write a program that implements a P-controller to turn a robot towards a desired angle.

```cpp
float Kp = 0.5; // Proportional gain
float desired_angle = 90.0;
float current_angle = get_robot_angle();
float error = desired_angle - current_angle;
float turn_speed = Kp * error;
set_motor_speeds(turn_speed);
```

---

# Lesson 3: PI-Controller

## Lesson Objective
Understand the limitations of a P-controller and introduce the integral component to eliminate steady-state error.

## Theory

### Drawbacks of a P-Controller
- A P-controller alone cannot eliminate steady-state error, meaning the system might not reach the exact desired value.
- If the gain is too high, the system may oscillate or become unstable.

### Eliminating Steady-State Error with the Integral Component
The PI (Proportional-Integral) controller addresses the steady-state error by adding an integral term:

$$
 u(t) = K_p \cdot e(t) + K_i \cdot \int e(t) dt 
$$

where:
- \( K_i \) is the integral gain,
- The integral term accumulates past errors to eliminate steady-state error.

### Block Diagram
![PI Controller](https://github.com/pranavk-2003/line-robot-curriculum/blob/main/images/module_7/pi.png)

## Assignment
Write a program that implements a PI-controller for turning a robot.

```cpp
float Kp = 0.5, Ki = 0.1;
float desired_angle = 90.0;
float current_angle = get_robot_angle();
float error = desired_angle - current_angle;
static float integral = 0.0;
integral += error;
float turn_speed = Kp * error + Ki * integral;
set_motor_speeds(turn_speed);
```

---

# Lesson 4: PID-Controller

## Lesson Objective
Introduce the derivative component to reduce overshoot and improve stability.

## Theory

### What is a Differential Component and How Does It Help Eliminate Overshoot?
- The derivative term predicts the system's future behavior and reduces overshoot.
- The control law becomes:

$$
 u(t) = K_p \cdot e(t) + K_i \cdot \int e(t) dt + K_d \cdot \frac{de(t)}{dt} 
$$

where:
- \( K_d \) is the derivative gain,
- The derivative term (\( de(t)/dt \)) reduces rapid changes and dampens oscillations.

### Block Diagram
![PID Controller](https://github.com/pranavk-2003/line-robot-curriculum/blob/main/images/module_7/pid_f.png)

## Assignment
Write a program that implements a PID-controller for turning a robot.

```cpp
float Kp = 0.5, Ki = 0.1, Kd = 0.05;
float desired_angle = 90.0;
float current_angle = get_robot_angle();
float error = desired_angle - current_angle;
static float integral = 0.0;
static float previous_error = 0.0;
integral += error;
float derivative = error - previous_error;
float turn_speed = Kp * error + Ki * integral + Kd * derivative;
previous_error = error;
set_motor_speeds(turn_speed);
```

## Conclusion
You've learned about Relay, P, PI, and PID controllers, their advantages, and how to implement them in robot movement. The next lesson will focus on tuning PID controllers for optimal performance.
