from collections import Counter
import os


def analyze_file():
    filename = input("Enter the filename (example: sample1.txt): ").strip()

    filepath = os.path.join("datasets", filename)

    if not os.path.exists(filepath):
        print("Error: File not found!")
        return

    with open(filepath, "r") as file:
        text = file.read()

    characters = len(text)
    words = len(text.split())
    lines = len(text.splitlines())
    unique_characters = len(set(text))

    # Count only alphabetic letters (case-insensitive)
    letters = [char.lower() for char in text if char.isalpha()]
    frequency = Counter(letters)

    print("\n========== File Analysis ==========")
    print(f"Characters        : {characters}")
    print(f"Words             : {words}")
    print(f"Lines             : {lines}")
    print(f"Unique Characters : {unique_characters}")

    print("\nLetter Frequency:")
    for letter in sorted(frequency):
        print(f"{letter} : {frequency[letter]}")
