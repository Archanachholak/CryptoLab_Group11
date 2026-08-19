import os
import sys

# Allow importing shift_cipher.py from the same src directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shift_cipher import decrypt


def load_dictionary(dictionary_path):
    """Load English words from the dictionary file."""
    with open(dictionary_path, "r", encoding="utf-8") as file:
        words = {line.strip().lower() for line in file if line.strip()}

    return words


def dictionary_score(text, dictionary):
    """Count how many words in the text appear in the dictionary."""
    words = text.lower().split()
    score = 0

    for word in words:
        # Remove punctuation
        clean_word = word.strip(".,!?;:'\"()[]{}")

        if clean_word in dictionary:
            score += 1

    return score


def brute_force_attack(ciphertext, dictionary):
    """Try all 26 Shift Cipher keys and rank them by dictionary score."""
    results = []

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = dictionary_score(plaintext, dictionary)

        results.append((score, key, plaintext))

    # Highest dictionary score is considered the best result
    results.sort(reverse=True)

    return results


if __name__ == "__main__":
    dictionary_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "dictionary",
        "english_words.txt"
    )

    dictionary = load_dictionary(dictionary_path)

    ciphertext = "KHOOR ZRUOG"

    results = brute_force_attack(ciphertext, dictionary)

    print("Ciphertext:", ciphertext)
    print("\nTop candidates:")

    for score, key, plaintext in results[:5]:
        print(f"Key: {key:2d} | Score: {score:2d} | Plaintext: {plaintext}")
