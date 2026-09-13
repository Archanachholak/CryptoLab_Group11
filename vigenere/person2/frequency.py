def frequency_analysis(groups):
    all_frequencies = []

    for group in groups:
        frequency = {letter: 0 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

        for ch in group:
            frequency[ch] += 1

        all_frequencies.append(frequency)

    return all_frequencies


def display_frequency(all_frequencies):
    for i, frequency in enumerate(all_frequencies):
        print(f"\nGroup {i + 1}:")

        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print(f"{letter} : {frequency[letter]}")


def find_shift(frequency):
    english_frequency = {
        'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253,
        'E': 12.702, 'F': 2.228, 'G': 2.015, 'H': 6.094,
        'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025,
        'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929,
        'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
        'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
        'Y': 1.974, 'Z': 0.074
    }

    total = sum(frequency.values())

    if total == 0:
        return 0

    best_shift = 0
    best_score = float('inf')

    for shift in range(26):
        score = 0

        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            cipher_letter = chr(
                (ord(letter) - ord('A') - shift) % 26 + ord('A')
            )

            observed = frequency[cipher_letter]
            expected = total * english_frequency[letter] / 100

            if expected > 0:
                score += (observed - expected) ** 2 / expected

        if score < best_score:
            best_score = score
            best_shift = shift

    return best_shift


def find_key(all_frequencies):
    key = ""

    for frequency in all_frequencies:
        shift = find_shift(frequency)
        key += chr(ord('A') + shift)

    return key


def get_shifts(all_frequencies):
    shifts = []

    for frequency in all_frequencies:
        shifts.append(find_shift(frequency))

    return shifts
