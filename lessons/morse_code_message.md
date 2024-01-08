---
index: 8
module: module_2 
task: morse_code_message
previous: emergency_light
next: turn_signals
---
# Lesson 8. Morse Code Message

## Objective
Reinforce the acquired knowledge of working with the **setup()** and **loop()** functions.

## Introduction
In previous lessons, you learned two fundamental functions of the Arduino Wiring language - **setup()** and **loop()**. Additionally, you acquired skills in working with LEDs using the lineRobot library. Let's apply this knowledge in a practical example - encoding messages using LED.

## Theory

### Morse Code
Morse code is a method of encoding textual characters using only two signals - short and long.

In Morse code, each letter of the alphabet and each digit is represented by a unique combination of short signals (dots: ".") and long signals (dashes: "-"). For example, the letter "A" is represented as ".-" (one short signal and one long signal), the letter "B" as "-..." (one long signal and three short signals), and so on.

<details>
<summary>Morse code history</summary>

Morse code was developed in the 1830s and 1840s by Samuel Morse and Alfred Vail for use with their newly invented telegraph. It was historically used for long-distance communication through telegraphy, where electrical signals were used to transmit messages over wires. It played a crucial role in maritime communication, aviation, and more. While Morse code is no longer widely used for practical communication due to the advent of more advanced technologies, it still has some applications.

</details>

## Assignment 
Write a program that first outputs the word "**BOT**" and then continuously outputs the digit "**3**".

- Short signal duration: 500 milliseconds
- Long signal duration: 1 second
- Pause between characters: 1 second

<details>
<summary>Morse code conversion table</summary>

- "**.**": short signal
- "**-**": long signal

| Character | Morse Code | Character | Morse Code |
|-----------|------------|-----------|------------|
| A         | .-         | N         | -.         |
| B         | -...       | O         | ---        |
| C         | -.-.       | P         | .--.       |
| D         | -..        | Q         | --.-       |
| E         | .          | R         | .-.        |
| F         | ..-.       | S         | ...        |
| G         | --.        | T         | -          |
| H         | ....       | U         | ..-        |
| I         | ..         | V         | ...-       |
| J         | .---       | W         | .--        |
| K         | -.-        | X         | -..-       |
| L         | .-..       | Y         | -.--       |
| M         | --         | Z         | --..       |
| 0         | -----      | 5         | .....      |
| 1         | .----      | 6         | -....      |
| 2         | ..---      | 7         | --...      |
| 3         | ...--      | 8         | ---..      |
| 4         | ....-      | 9         | ----.      |

</details>

<details>
<summary>Examples</summary>

"ONDROID": "**--- -. -.. .-. --- .. -..**"

"123HELLO!": "**.---- ..--- ...-- .... . .-.. .-.. --- -.-.--**"

Each space before the next character corresponds to a 1-second pause.

</details>

## Conclusion
Congratulations! You have gained knowledge about two basic Arduino functions, and you've also learned about Morse code!