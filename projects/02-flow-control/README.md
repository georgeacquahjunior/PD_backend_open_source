# Project 2 — ATM Simulator

**Topic:** Flow Control (if/elif/else, while loops, for loops, break/continue)

## Problem

Build a command-line ATM simulator with a login system and a banking menu.

The program should:

1. Store a **PIN** (e.g. `"4321"`) and a starting **balance** (e.g. `1000.00`) as variables at the top of the program.
2. Ask the user to enter their PIN.
   - Give the user **up to 3 attempts** to enter the correct PIN.
   - If they succeed, move on to the main menu.
   - If they fail all 3 attempts, print a "card locked" message and end the program.
3. Once logged in, show a repeating menu:

   ```text
   1. Check balance
   2. Deposit
   3. Withdraw
   4. Exit
   ```

4. Handle each option:
   - **Check balance** — display the current balance.
   - **Deposit** — ask for an amount, reject it (with a message, no crash) if it's zero or negative, otherwise add it to the balance.
   - **Withdraw** — ask for an amount, reject it if it's zero or negative, or if it **exceeds the current balance** (insufficient funds), otherwise subtract it from the balance.
   - **Exit** — print a goodbye message and end the program.
5. The menu should keep showing after every action until the user chooses Exit.
6. If the user enters something that isn't a valid menu option (e.g. `9` or `"hello"`), show an error message and re-show the menu, without crashing.

## Expected Outcome

- Entering the wrong PIN 3 times locks the user out and ends the program cleanly.
- Entering the correct PIN (on attempt 1, 2, or 3) grants access to a menu loop.
- The menu keeps running until the user explicitly chooses Exit.
- Balance never goes negative — withdrawals larger than the balance are rejected with a clear message.
- Invalid input (wrong menu number, non-numeric deposit/withdrawal amount) is handled gracefully — the program never crashes, it just re-prompts.

## Hint

Use a `while` loop for the PIN attempts, with a counter you increment on each wrong try, and `break` out of the loop as soon as the PIN is correct. Use another (outer) `while True` loop for the menu so it keeps repeating, with `break` triggered only by the Exit option. For non-numeric input, look into wrapping your `int()`/`float()` conversion in a `try/except ValueError` block so a bad input doesn't crash the program — you can `continue` back to the top of the menu loop when that happens.
