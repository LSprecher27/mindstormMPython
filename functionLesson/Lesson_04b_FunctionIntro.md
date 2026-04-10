# Lesson 04b Follow On – Functions
### EV3 MicroPython Robotics

---

## What You'll Learn
By the end of this lesson you will:
- Write your own Python functions using `def`
- Understand the difference between functions that **print**, functions that **return a value**, and functions that **return True/False**
- Organize a robot program so the `while` loop reads like plain English
- Use the ultrasonic sensor and/or color sensor inside functions

**What you need:** You should be set up already with these parts assembled: EV3 Brick, 2x Large Motors, Ultrasonic Sensor (Port S4), Color Sensor (Port S3), driving base build, Mini-USB cable, Computer

---

## Background – Why Write Functions?

You've been *calling* functions all year — `print()`, `robot.drive()`, `wait()`. Today you write your own.

A function is a **named block of code** you can run whenever you need it. Instead of repeating the same logic in three places, you write it once and call it by name.

Here's the point for robot programming:

```python
# Without functions — hard to read
while True:
    if obstacle_sensor.distance() < 100:
        robot.stop()
        ev3.speaker.beep(880, 300)
    else:
        robot.drive(200, 0)
    wait(10)

# With functions — reads like English
while True:
    if is_too_close():
        stop_and_beep()
    else:
        robot.drive(200, 0)
    wait(10)
```

Same behavior. The second version helps you "tell a story" so to speak, by defining functions that are easy to understand.

---

## Part 1 – Three Kinds of Functions

Before touching the robot, make sure you understand what these functions are doing.

### Kind 1 — Does something (no return value)

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Alex")
greet("Robot")
```

### Kind 2 — Returns a value you can use

```python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
```

### Kind 3 — Returns True or False

```python
def is_big(number):
    return number > 100

print(is_big(200))   # True
print(is_big(50))    # False

if is_big(200):
    print("That's big!")
```

**Key rule:** `return` sends a value *back* to whoever called the function. `print` just displays something — it doesn't hand anything back.

**Quick experiment:** What does this print for `x`? Figure it out, then run it.

```python
def add_with_print(a, b):
    print(a + b)

x = add_with_print(3, 5)
print("x is:", x)
```

---

## Part 2 – Sensor Functions

Sensor readings are just numbers. The ultrasonic sensor returns millimeters. The color sensor returns a reflection percentage (0–100). That means you can wrap them in functions exactly like the examples above.

**Ultrasonic — returning a boolean:**

```python
def is_too_close():
    return obstacle_sensor.distance() < 100

if is_too_close():
    robot.stop()
    ev3.speaker.beep()
```

**Color — returning the reading:**

```python
def get_reflection():
    return color_sensor.reflection()

light = get_reflection()
if light < 20:
    ev3.screen.print("Dark")
else:
    ev3.screen.print("Light")
```

**Notice:** `is_too_close()` takes no parameters — it reads the sensor itself. That's fine. Not every function needs inputs.

---

## Part 3 – Your Project

Now you design a robot program that uses **at least 3 of your own functions**. Your robot must use the **ultrasonic sensor**, the **color sensor**, or **both**.

### The Rules

1. Your program must define at least **3 functions** using `def`
2. At least one function must **return a boolean** (`True`/`False`) and be used in an `if` statement
3. At least one function must involve a **sensor reading** (ultrasonic or color)
4. Your `while True` loop should be **clean and readable** — move the details into functions
5. You decide what your robot's goal is

### Some Ideas

- **Line follower lite** — drives forward but stops when the color sensor detects a dark line
- **Nervous robot** — uses the ultrasonic sensor to back away from anything that gets too close, beeps faster the closer it gets
- **Surface reporter** — sits still, reads the color sensor repeatedly, displays "Dark" / "Medium" / "Light" and also beeps once if something is too close
- **Guard dog** — patrols forward and backward; the color sensor detects the edge of a mat and reverses; the ultrasonic sensor detects an intruder and sounds an alarm
- **Your own idea** — describe it in the planning checklist below

---

### Your Planning Checklist

Answer these before you write any code. Turn in this file with the answers filled in.

**1. What is your robot's goal?** (one sentence)

The robot drives forward while avoiding obstacles detected by the ultrasonic sensor.

**2. List the 3+ functions you plan to write.** For each one, write: its name, what it takes in (or "nothing"), and what it returns or does.

| Function name | Parameters | Returns / Does |
|---|---|---|
| `check_obstacle_and_avoid()` | threshold_mm=150 | returns True if obstacle detected and performs avoidance: stops, backs up, turns 180°, resumes forward |
| `display_status()` | nothing | displays current distance on EV3 screen |
| `main()` | nothing | runs the main loop for robot operation |

**3. Which sensor(s) are you using?**

ultrasonic only

**4. What distance or reflection thresholds will you use?** (you can adjust these when testing)

Distance threshold: 300 mm for obstacle detection.

**5. Pseudocode** — write your `while True` logic in plain English:

```
Loop forever:
    display_status()
    if check_obstacle_and_avoid(300):
        continue
    wait(100)
```

---

### Write Your Code

Create a new project called `legoMs05.py`. Define all your functions **above** the `while True` loop.

**Requirements checklist:**

- [ ] At least 3 functions defined with `def`
- [ ] At least 1 function returns a boolean and is used in an `if`
- [ ] At least 1 function reads from a sensor
- [ ] `while True` loop is clean — logic is inside functions
- [ ] Comments explain what each function does
- [ ] Something useful displays on the EV3 screen

---

### Test and Iterate

Your thresholds (distances, reflection values) will need tuning. Start by printing sensor readings to the screen to see what numbers you're actually getting in your environment, then adjust your function conditions from there.

---

## What to Turn In

1. **Post your code** to GitHub as `legoMs05.py`
2. **Turn in this markdown file** with the Planning Checklist filled in (also on GitHub)
3. **Demo the robot** to Mr M — show it working
4. **Explain your functions** — for each `def`, tell me what it does, what it returns, and why you chose to wrap that code in a function

---

## Quick Reference

| Command | What it does |
|---|---|
| `def name():` | Define a function with no parameters |
| `def name(a, b):` | Define a function with parameters |
| `return value` | Send a value back to the caller |
| `return a > b` | Return a boolean (True or False) |
| `obstacle_sensor.distance()` | Ultrasonic: distance in mm (Port S4) |
| `color_sensor.reflection()` | Color: reflection % 0–100 (Port S3) |
| `robot.drive(speed, 0)` | Drive straight continuously |
| `robot.stop()` | Stop |
| `wait(10)` | Short pause inside the loop |

---

