# 1. Ask the user for their name and greet them
name = input("Enter your name: ")
print(f"Hello, {name}! Let's play a quick game.")

# 2. Define a list of secret words
secret_words = ["python", "code", "magic"]

# 3. Check if a specific word is in our list using a loop
print("\nHere are the words we are checking:")
for word in secret_words:
    if word == "python":
        print(f"- {word} (This is an awesome programming language!)")
    else:
        print(f"- {word}")
