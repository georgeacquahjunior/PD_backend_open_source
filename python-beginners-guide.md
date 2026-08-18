# Python for Beginners

## Introduction
Python is a beginner-friendly programming language. It is used for websites, data science, automation, machine learning, and many other tasks.

The goal of this guide is to help you understand the basic ideas behind programming and how they apply to your receipt generator exercise.

---

## 1. What is programming?
Programming means giving instructions to a computer.

A program is a set of steps that the computer follows in order.

Example:
```python
print("Hello, world!")
```

This line tells Python to display text on the screen.

---

## 2. Variables
Variables store information.

```python
name = "Ada"
age = 25
```

You can think of a variable as a labeled box that holds data.

---

## 3. Input and output
Use `print()` to show output.

Use `input()` to ask the user for information.

```python
name = input("What is your name? ")
print("Hello", name)
```

---

## 4. Numbers and math
Python can work with numbers.

```python
price = 10
quantity = 3
subtotal = price * quantity
print(subtotal)
```

You can also use:
- `+` for addition
- `-` for subtraction
- `*` for multiplication
- `/` for division

---

## 5. Decisions with if
The `if` statement lets your program make choices.

```python
age = 18

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
```

---

## 6. Repeating with loops
Loops let you repeat code.

```python
for i in range(3):
    print("Hello")
```

This prints "Hello" three times.

---

## 7. Functions
Functions let you organize code into reusable blocks.

```python
def greet(name):
    print("Hello", name)

greet("Sam")
```

---

## 8. Understanding your receipt generator
Your receipt program uses several important concepts.

### Input
```python
shop_name = input("Enter shop name: ").strip()
```

This asks the user for the shop name and removes extra spaces.

### Number conversion
```python
item_count = int(input("How many different items are you buying? "))
```

This converts user text into an integer.

### Looping through items
```python
for _ in range(item_count):
```

This repeats the code once for each item.

### Calculating totals
```python
line_total = quantity * unit_price
subtotal += line_total
```

This calculates the cost of each item and adds it to the subtotal.

### Tax calculation
```python
tax = subtotal * 0.05
grand_total = subtotal + tax
```

The program calculates tax and the final amount.

---

## 9. Small practice exercise
Try this example:

```python
name = input("What is your name? ")
age = int(input("How old are you? "))

print("Hello", name)
print("Next year you will be", age + 1)
```

---

## 10. Suggested learning order
1. Variables
2. Input and output
3. Numbers and math
4. If statements
5. Loops
6. Functions

---

## 11. Final advice
The best way to learn Python is to:
- write small programs
- test them often
- fix errors one at a time
- practice every day

Programming becomes easier when you practice regularly.
