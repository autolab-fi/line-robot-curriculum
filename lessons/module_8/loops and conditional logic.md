# **Lesson 2: Loops and Conditional Logic**

## **Lesson Objective**

Learn how to repeat actions using `for` and `while` loops, and combine them with `if-else` statements for decision-making.

---

## **Introduction**

Loops allow you to execute a block of code **multiple times**. You can control how many times the loop runs using conditions. Combined with `if-else`, you can build intelligent programs that respond to different values inside loops.

---

## **Theory**

### **For Loop**

Runs code a fixed number of times.

```cpp
for (int i = 1; i <= 5; i++) {
    cout << i << endl;
}
```

### **While Loop**

Runs code **while a condition is true**.

```cpp
int i = 1;
while (i <= 5) {
    cout << i << endl;
    i++;
}
```

### **Combining Loops with If-Else**

You can make decisions inside a loop using `if-else`. For example, print only even numbers in a loop.

---

## **Code Implementation**

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) {
            cout << i << " is even" << endl;
        } else {
            cout << i << " is odd" << endl;
        }
    }

    return 0;
}
```

---

## **Understanding the Logic**

1. The `for` loop runs 10 times.
2. Each time, it checks whether `i` is even or odd.
3. It prints a message accordingly.

---

## **Assignment**

---

## **Conclusion**

In this lesson, you learned how to use loops to repeat code and combine them with `if-else` for making decisions. This sets the foundation for processing lists and patterns in programming.
