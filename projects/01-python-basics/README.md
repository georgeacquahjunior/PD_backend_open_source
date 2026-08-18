# Project 1 — Receipt Generator

**Topic:** Python Basics (variables, data types, string formatting, input/output)

## Problem

Build a command-line program that acts like a mini point-of-sale receipt printer for a small shop.

The program should:

1. Ask the user for the **shop name** (text).
2. Ask the user how many **different items** they're buying (a whole number).
3. For each item, ask for:
   - the item name (text)
   - the quantity (whole number)
   - the unit price (decimal number)
4. Calculate, for each item, the **line total** (quantity × unit price).
5. Calculate the **subtotal** (sum of all line totals).
6. Apply a **5% sales tax** to the subtotal to get the **tax amount**.
7. Calculate the **grand total** (subtotal + tax).
8. Print a neatlyf ormatted receipt to the terminal, including the shop name, a line per item (name, quantity, unit price, line total), the subtotal, tax, and grand total — all currency values shown with exactly 2 decimal places and aligned so the numbers line up visually.

## Expected Outcome

Running the program and entering sample data produces output that looks roughly like this:

``` text
========================================
        FRESH MART GROCERY
========================================
Bananas         x3   @  0.50   =   1.50
Bread           x1   @  2.75   =   2.75
Milk            x2   @  1.20   =   2.40
----------------------------------------
Subtotal:                     6.65
Tax (5%):                     0.33
GRAND TOTAL:                  6.98
========================================
```

Exact spacing/formatting is up to you, but numbers must be aligned, currency must show 2 decimal places, and all math must be correct.

## Hint

Look into f-strings and their format specifiers, e.g. `f"{value:>10.2f}"` for right-aligned numbers with 2 decimal places. You'll also need `input()` (which always returns a string) combined with `int()` / `float()` to convert user input into numbers you can do math with. Build up the receipt as a list of items (e.g. a list of small tuples or dictionaries) before printing, rather than printing inside the input loop — it'll make the formatting step much easier.
