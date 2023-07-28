# Lesson 1. Test drive

## Lesson objective
Get started with the robot and get it moving immediately.

## Introduction
In this lesson we will show you how to make our robot go forward.

## Step-by-step Instructions
1. Copy the code provided below and paste it into the dedicated field of your program.
```
void setup() {
  
  //Setup Channel A
  pinMode(12, OUTPUT); //Initiates Motor Channel A pin
  pinMode(9, OUTPUT); //Initiates Brake Channel A pin

  //Setup Channel B
  pinMode(13, OUTPUT); //Initiates Motor Channel A pin
  pinMode(8, OUTPUT);  //Initiates Brake Channel A pin

  //Motor A forward
  digitalWrite(12, LOW); //Establishes forward direction of Channel A
  digitalWrite(9, LOW);   //Disengage the Brake for Channel A
  analogWrite(3, 180);   //Spins the motor on Channel A at full speed

  //Motor B forward
  digitalWrite(13, LOW);  //Establishes backward direction of Channel B
  digitalWrite(8, LOW);   //Disengage the Brake for Channel B
  analogWrite(11, 180);    //Spins the motor on Channel B at half speed

  delay(3000); //pause between executing commands

  digitalWrite(9, HIGH); //Engage the Brake for Channel A
  digitalWrite(8, HIGH); //Engage the Brake for Channel B
}

void loop(){
 
}
```
2. Upload the program to the robot by clicking on the "Upload" button.
3. Our robot will go straight for 3 seconds. Now, let's take a closer look at the program code.

## Explanation of the Program Code
- Next, we see the scary sequence of characters: "void setup()". In the next lesson, we will explain what `void setup()`, `void loop()`, `pinMode()` and `analogWrite()` mean, but now let's learn about `digitalWrite()` and `delay()`.
- `digitalWrite()` is a function that sets the signal sent to a pin. In the brackets, we first specify the pin to which the signal should be sent, and then the signal value. The signal can be either HIGH or LOW.
- In the comments of the code, you can read that we are using `digitalWrite()` to control the motor brakes and the motor's direction of movement.
- `delay()` is a function that introduces a pause between executing commands. Inside this function, you need to specify the duration of the pause. The time is given in milliseconds, so 3000 milliseconds is 3 seconds.
- The result of the program execution is the movement of the robot for 3 seconds.

## Exercise

### Exercise

### Verification exercise
- Try writing code for the robot to move forward for 5 seconds.

### Task for self-testing
- Now, you can try sending a LOW signal to both motors or just one. See what happens.

## Conclusion
Congratulations! You have successfully learned how to make the robot move!


