import os
import sys

# Allow importing shift_cipher.py from the same src directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shift_cipher import decrypt


# English letter frequencies
ENGLISH_FREQ = {
    'A': 0.0812,
    'B': 0.0149,
    'C': 0.0271,
    'D': 0.0432,
    'E': 0.1202,
    'F': 0.0230,
    'G': 0.0203,
    'H': 0.0592,
    'I': 0.0731,
    'J': 0.0010,
    'K': 0.0069,
    'L': 0.0398,
    'M': 0.0261,
    'N': 0.0695,
    'O': 0.0768,
    'P': 0.0182,
    'Q': 0.0011,
    'R': 0.0602,
    'S': 0.0628,
    'T': 0.0910,
    'U': 0.0288,
    'V': 0.0111,
    'W': 0.0209,
    'X': 0.0017,
    'Y': 0.0211,
    'Z': 0.0007
}


def chi_square_score(text):
    """Calculate chi-square score between text frequencies and English frequencies."""

    text = ''.join(char.upper() for char in text if char.isalpha())

    if len(text) == 0:
        return float('inf')

    counts = {letter: 0 for letter in ENGLISH_FREQ}

    for char in text:
        counts[char] += 1

    total = len(text)
    score = 0

    for letter in ENGLISH_FREQ:
        expected = ENGLISH_FREQ[letter] * total
        observed = counts[letter]

        if expected > 0:
            score += ((observed - expected) ** 2) / expected

    return score


def chi_square_attack(ciphertext):
    """Try all 26 keys and select the key with the lowest chi-square score."""

    results = []

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = chi_square_score(plaintext)

        results.append((score, key, plaintext))

    # Lowest chi-square score is the best match
    results.sort()

    return results


if __name__ == "__main__":

    ciphertext = "KHOOR ZRUOG"

    results = chi_square_attack(ciphertext)

    print("Ciphertext:", ciphertext)
    print("\nTop candidates:")

    for score, key, plaintext in results[:5]:
        print(
            f"Key: {key:2d} | "
            f"Chi-Square: {score:8.2f} | "
            f"Plaintext: {plaintext}"
        )

    print("\nPredicted Key:", results[0][1])
    print("Predicted Plaintext:", results[0][2])