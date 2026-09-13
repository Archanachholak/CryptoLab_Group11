from shift_cipher import encrypt
from brute_force_dictionary import load_dictionary, brute_force_attack
from chi_square_attack import chi_square_attack

import os


# Get dictionary path
dictionary_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "dictionary",
    "english_words.txt"
)

dictionary = load_dictionary(dictionary_path)


# Test cases: (plaintext, actual key)
test_cases = [
    ("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 3),
    ("THIS IS A SIMPLE ENGLISH MESSAGE FOR TESTING", 7),
    ("CRYPTOGRAPHY IS USED TO PROTECT INFORMATION", 12),
    ("ATTACK AT DAWN AND RETREAT AFTER THE MISSION", 18),
    ("MEET ME AT THE TRAIN STATION TOMORROW MORNING", 22)
]


print("=" * 70)
print("SHIFT CIPHER CRYPTANALYSIS RESULTS")
print("=" * 70)


for i, (plaintext, actual_key) in enumerate(test_cases, start=1):

    # Encrypt plaintext
    ciphertext = encrypt(plaintext, actual_key)

    # Dictionary attack
    dictionary_results = brute_force_attack(ciphertext, dictionary)
    dictionary_key = dictionary_results[0][1]

    # Chi-Square attack
    chi_results = chi_square_attack(ciphertext)
    chi_square_key = chi_results[0][1]

    # Check correctness
    dictionary_correct = dictionary_key == actual_key
    chi_square_correct = chi_square_key == actual_key

    print(f"\nTest Case {i}")
    print("-" * 70)
    print("Plaintext          :", plaintext)
    print("Ciphertext         :", ciphertext)
    print("Actual Key         :", actual_key)
    print("Dictionary Key     :", dictionary_key)
    print("Chi-Square Key     :", chi_square_key)
    print("Dictionary Correct?:", "Yes" if dictionary_correct else "No")
    print("Chi-Square Correct?:", "Yes" if chi_square_correct else "No")


print("\n" + "=" * 70)
print("RESULTS TABLE")
print("=" * 70)

print(
    f"{'Test':<8}"
    f"{'Actual':<10}"
    f"{'Dictionary':<13}"
    f"{'Chi-Square':<13}"
    f"{'Dict Correct':<15}"
    f"{'Chi Correct':<12}"
)

print("-" * 70)


for i, (plaintext, actual_key) in enumerate(test_cases, start=1):

    ciphertext = encrypt(plaintext, actual_key)

    dictionary_results = brute_force_attack(ciphertext, dictionary)
    dictionary_key = dictionary_results[0][1]

    chi_results = chi_square_attack(ciphertext)
    chi_square_key = chi_results[0][1]

    dictionary_correct = "Yes" if dictionary_key == actual_key else "No"
    chi_square_correct = "Yes" if chi_square_key == actual_key else "No"

    print(
        f"{'TC' + str(i):<8}"
        f"{actual_key:<10}"
        f"{dictionary_key:<13}"
        f"{chi_square_key:<13}"
        f"{dictionary_correct:<15}"
        f"{chi_square_correct:<12}"
    )