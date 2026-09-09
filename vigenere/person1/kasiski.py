from collections import Counter


def find_repeated_patterns(ciphertext, pattern_length=3):
    """
    Find repeated sequences of a given length
    and their starting positions.
    """

    patterns = {}

    for i in range(len(ciphertext) - pattern_length + 1):
        pattern = ciphertext[i:i + pattern_length]

        if pattern not in patterns:
            patterns[pattern] = []

        patterns[pattern].append(i)

    # Keep only patterns that occur more than once
    repeated = {
        pattern: positions
        for pattern, positions in patterns.items()
        if len(positions) > 1
    }

    return repeated


def calculate_distances(repeated_patterns):
    """
    Calculate distances between consecutive
    occurrences of repeated patterns.
    """

    distances = []

    for pattern, positions in repeated_patterns.items():

        for i in range(len(positions) - 1):
            distance = positions[i + 1] - positions[i]

            distances.append((pattern, distance))

    return distances


def find_factors(number):
    """
    Find factors of a distance.
    """

    factors = []

    for i in range(2, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors

def kasiski_analysis(ciphertext):
    """
    Perform Kasiski examination and suggest
    probable key lengths.
    """

    all_distances = []

    # Check repeated sequences of length 3, 4 and 5
    for pattern_length in [3, 4, 5]:

        repeated = find_repeated_patterns(
            ciphertext,
            pattern_length
        )

        distances = calculate_distances(repeated)

        all_distances.extend(distances)

    factor_counter = Counter()

    for pattern, distance in all_distances:

        factors = find_factors(distance)

        for factor in factors:

            # Ignore very small key lengths
            if 3 <= factor <= 20:
                factor_counter[factor] += 1

    return factor_counter.most_common()



def calculate_ic(text):
    """
    Calculate Index of Coincidence.
    """

    n = len(text)

    if n <= 1:
        return 0.0

    frequency = Counter(text)

    numerator = sum(
        count * (count - 1)
        for count in frequency.values()
    )

    denominator = n * (n - 1)

    return numerator / denominator


def split_into_groups(ciphertext, key_length):
    """
    Divide ciphertext into groups according to
    the candidate key length.
    """

    groups = []

    for i in range(key_length):
        group = ciphertext[i::key_length]
        groups.append(group)

    return groups
def average_group_ic(ciphertext, key_length):
    """
    Calculate the average Index of Coincidence
    across all groups for a candidate key length.
    """

    groups = split_into_groups(ciphertext, key_length)

    ics = []

    for group in groups:
        ics.append(calculate_ic(group))

    if not ics:
        return 0.0

    return sum(ics) / len(ics)

