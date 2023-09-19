---
index: 0
module: module_1
task: draw
previous: None
next: test_drive
---
# Lesson Draw.


# Description
Hello! This is the sandbox mode, where you can test your programs. Moreover, you can run the task check, and a blue trail will be left behind the robot for 20 seconds.


# Code example
```
#include <lineRobot.h>
void setup(){
   robot.turnRight();
   robot.turnRightAngle(45);
   robot.moveForwardDistance(20);
   robot.turnRight();
   robot.moveForwardDistance(20);
   robot.turnRight();
   robot.moveForwardDistance(20);
   robot.turnRight();
   robot.moveForwardDistance(20);
}
void loop(){
}
```