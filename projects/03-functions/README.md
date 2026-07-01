# Project 3 — Text Analysis Toolkit

**Topic:** Functions (parameters, return values, default arguments, function composition)

## Problem

Build a small library of functions that analyze a block of text (e.g. a paragraph, an essay, a tweet draft), plus a simple command-line interface that ties them together. This mimics a real tool a writer or student might use to check their draft before submitting it.

Write the following functions (you decide exact names/signatures, but each must **take input and return a value** — none should just `print()` inside them):

1. `count_words(text)` — returns the number of words in the text.
2. `count_sentences(text)` — returns the number of sentences (hint: sentences typically end in `.`, `!`, or `?`).
3. `count_characters(text, include_spaces=True)` — returns the character count; if `include_spaces` is `False`, spaces should not be counted. This function must have a **default argument**.
4. `average_word_length(text)` — returns the average number of characters per word, rounded to 2 decimal places. This function should **reuse** `count_words` and `count_characters` internally rather than recalculating from scratch.
5. `most_common_word(text)` — returns the word that appears most frequently in the text (case-insensitive, ignoring punctuation).
6. `longest_sentence(text)` — returns the full text of the longest sentence (by word count).

Then write a `main()` function that:

- Asks the user to paste/type in a block of text.
- Calls each of the above functions on that text.
- Prints a clean summary report of all the results.

## Expected Outcome

Given an input like:

```text
Python is fun. Python is also powerful! Do you enjoy learning Python?
```

Your program should output a report similar to:

```text
--- Text Analysis Report ---
Word count: 11
Sentence count: 3
Character count (with spaces): 64
Character count (no spaces): 54
Average word length: 4.91
Most common word: python
Longest sentence: "Do you enjoy learning Python?"
```

(Exact numbers depend on your counting rules — the important part is that every value is produced by a dedicated function, not computed inline in `main()`.)

## Hint

Use `str.split()` to break text into words, and consider using the `re` module (`re.split` with a pattern like `[.!?]`) to split into sentences cleanly. For `most_common_word`, strip punctuation with `str.strip(string.punctuation)` on each word and lowercase everything before counting — a `dict` or `collections.Counter` works well for tallying frequencies. Keep each function doing **one job only**; if you find yourself copy-pasting word-splitting logic into three different functions, that's a sign one function should be calling another instead.
