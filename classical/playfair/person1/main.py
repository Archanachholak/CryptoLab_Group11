from preprocessing import prepare_plaintext, create_digraphs
from encryption import generate_key_matrix, playfair_encrypt


def main():
    keyword = "MONARCHY"
    plaintext = "INSTRUMENTS"

    # Generate key matrix
    matrix = generate_key_matrix(keyword)

    print("Key Matrix:")
    for row in matrix:
        print(" ".join(row))

    # Prepare plaintext
    prepared = prepare_plaintext(plaintext)

    # Create digraphs
    digraphs = create_digraphs(prepared)

    print("\nPrepared Digraphs:")
    print(" ".join(digraphs))

    # Encrypt
    ciphertext = playfair_encrypt(digraphs, matrix)

    print("\nCiphertext:")
    print(ciphertext)


if __name__ == "__main__":
    main()