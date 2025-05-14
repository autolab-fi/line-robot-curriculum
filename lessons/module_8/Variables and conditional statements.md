# **Lesson 1: Introduction to Variables and Conditional Statements**

## **Lesson Objective**

## Learn how to declare and use variables in C++, and apply conditional logic using `if`, `else if`, and `else`.

## **Introduction**

Variables are the building blocks of any program. They store information like numbers, characters, and true/false values. Once we store values in variables, we can apply logic to make decisions using conditional statements.

---

## **Theory**

### **What are Variables?**

Variables are named storage locations in memory.  
Examples:

- `int age = 20;` stores a whole number
- `float pi = 3.14;` stores a decimal
- `char grade = 'A';` stores a character
- `bool isActive = true;` stores true/false

### **What is an If-Else Statement?**

It helps the program **make decisions** based on conditions.  
Syntax:

```cpp
if (condition) {
    // code runs if condition is true
} else {
    // code runs if condition is false
}
```

---

## **Code Implementation**

```cpp
#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Enter your age: ";
    cin >> age;

    if (age >= 18) {
        cout << "You are an adult." << endl;
    } else {
        cout << "You are a minor." << endl;
    }

    return 0;
}
```

---

## **Understanding the Logic**

1. The program asks the user for their age.
2. If the age is 18 or more, it prints **"You are an adult."**
3. Otherwise, it prints **"You are a minor."**

---

## **Assignment**

1. Write a program that takes a number as input.
2. If the number is greater than 0 → Print "Positive"
3. If the number is less than 0 → Print "Negative"
4. Otherwise → Print "Zero"

---

## **Conclusion**

In this lesson, you learned how to declare and use variables in C++. You also used `if-else` conditions to make your program react based on input.

---

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
