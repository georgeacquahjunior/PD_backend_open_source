import re
from collections import Counter


def count_words(text):
    words = re.findall(r"\b\w+\b", text)
    return len(words)


def count_sentences(text):
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    return len(sentences)


def count_characters(text, include_spaces=True):
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def average_word_length(text):
    words = re.findall(r"\b\w+\b", text)
    if not words:
        return 0.0
    total_length = sum(len(word) for word in words)
    return round(total_length / len(words), 2)


def most_common_word(text):
    words = [re.sub(r"[^a-zA-Z0-9]", "", word).lower() for word in re.findall(r"\b\w+\b", text)]
    words = [word for word in words if word]
    if not words:
        return ""
    counts = Counter(words)
    return counts.most_common(1)[0][0]


def longest_sentence(text):
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    if not sentences:
        return ""
    longest = max(sentences, key=lambda sentence: count_words(sentence))
    return longest


def main():
    text = input("Enter a block of text: ")

    print("\n--- Text Analysis Report ---")
    print(f"Word count: {count_words(text)}")
    print(f"Sentence count: {count_sentences(text)}")
    print(f"Character count (with spaces): {count_characters(text, True)}")
    print(f"Character count (no spaces): {count_characters(text, False)}")
    print(f"Average word length: {average_word_length(text):.2f}")
    print(f"Most common word: {most_common_word(text)}")
    print(f"Longest sentence: \"{longest_sentence(text)}\"")


if __name__ == "__main__":
    main()
