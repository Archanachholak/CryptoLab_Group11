import re


def prepare_plaintext(plaintext):
    """
    Prepare plaintext for the Playfair cipher.

    Steps:
    1. Convert text to uppercase.
    2. Remove spaces and special characters.
    3. Replace J with I because Playfair uses a 5x5 matrix.
    """

    plaintext = plaintext.upper()

    # Keep only alphabetic characters
    plaintext = re.sub(r"[^A-Z]", "", plaintext)

    # Combine I and J
    plaintext = plaintext.replace("J", "I")

    return plaintext


def create_digraphs(plaintext):
    """
    Divide prepared plaintext into pairs of letters.

    If two identical letters occur in a pair,
    insert X between them.

    If one letter is left at the end,
    append X.
    """

    digraphs = []
    i = 0

    while i < len(plaintext):

        first = plaintext[i]

        # Last character has no pair
        if i + 1 >= len(plaintext):
            digraphs.append(first + "X")
            i += 1

        else:
            second = plaintext[i + 1]

            # Repeated letters
            if first == second:
                digraphs.append(first + "X")
                i += 1

            else:
                digraphs.append(first + second)
                i += 2

    return digraphs
if __name__ == "__main__":
    plaintext = "INSTRUMENTS"

    prepared = prepare_plaintext(plaintext)
    digraphs = create_digraphs(prepared)

    print("Prepared Plaintext:")
    print(prepared)

    print("\nDigraphs:")
    print(" ".join(digraphs))