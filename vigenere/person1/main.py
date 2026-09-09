from preprocessing import clean_ciphertext
from kasiski import (
    kasiski_analysis,
    calculate_ic,
    split_into_groups,
    average_group_ic
)


def load_ciphertext():
    """
    Read ciphertext from data/data.txt.
    """

    with open("../data/data.txt", "r") as file:
        return file.read()


def main():

    # Load original ciphertext
    ciphertext = load_ciphertext()

    # Step 1: Clean ciphertext
    cleaned = clean_ciphertext(ciphertext)

    print("=" * 60)
    print("VIGENERE CIPHER CRYPTANALYSIS")
    print("=" * 60)

    print("\nOriginal ciphertext length:", len(ciphertext))
    print("Cleaned ciphertext length:", len(cleaned))

    print("\nCleaned ciphertext:")
    print(cleaned)

    # Calculate overall IC
    ic = calculate_ic(cleaned)

    print("\nOverall Index of Coincidence:", round(ic, 4))

    # Step 2: Kasiski analysis
    candidates = kasiski_analysis(cleaned)

    print("\nKasiski candidate key lengths:")

    for length, score in candidates:
        print(
            "Key length:",
            length,
            "Score:",
            score
        )

    if candidates:

        print("\nCandidate key lengths with average IC:")

        candidate_results = []

        for length, score in candidates:

            avg_ic = average_group_ic(
                cleaned,
                length
            )

            candidate_results.append(
                (length, score, avg_ic)
            )

            print(
                f"Key length: {length:2d} | "
                f"Kasiski score: {score:2d} | "
                f"Average IC: {avg_ic:.4f}"
            )

        # Select candidate with highest average IC
        estimated_key_length = max(
            candidate_results,
            key=lambda x: x[2]
        )[0]

        print(
            "\nEstimated key length:",
            estimated_key_length
        )

        # Step 3: Split ciphertext into groups
        groups = split_into_groups(
            cleaned,
            estimated_key_length
        )

        print("\nCiphertext Groups:")

        for i, group in enumerate(groups, start=1):
            print(f"Group {i}: {group}")

    else:

        print("\nCould not determine key length.")


if __name__ == "__main__":
    main()
