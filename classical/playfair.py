# Playfair Cipher - Part 2
# Decryption and Digraph Frequency Analysis


# Find the row and column of a letter in the 5x5 matrix
def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

    return -1, -1


# Playfair Cipher Decryption
def playfair_decrypt(ciphertext, matrix):
    plaintext = ""

    # Process ciphertext two letters at a time
    for i in range(0, len(ciphertext), 2):

        a = ciphertext[i]
        b = ciphertext[i + 1]

        # Find positions of both letters
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same row: move one position LEFT
        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % 5]
            plaintext += matrix[r2][(c2 - 1) % 5]

        # Same column: move one position UP
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1]
            plaintext += matrix[(r2 - 1) % 5][c2]

        # Rectangle rule
        else:
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


# Digraph Frequency Analysis
def digraph_frequency(ciphertext):
    frequency = {}

    # Read ciphertext two letters at a time
    for i in range(0, len(ciphertext), 2):

        digraph = ciphertext[i:i + 2]

        if digraph in frequency:
            frequency[digraph] += 1
        else:
            frequency[digraph] = 1

    return frequency

# Verification
def verify(ciphertext, decrypted_text, create_digraphs, playfair_encrypt, matrix):
    # Convert decrypted text into digraphs
    digraphs = create_digraphs(decrypted_text)

    # Encrypt the decrypted text again
    re_encrypted = playfair_encrypt(digraphs, matrix)

    # Compare with original ciphertext
    if ciphertext == re_encrypted:
        return True
    else:
        return False
# Main program for testing
if __name__ == "__main__":

    # Key matrix for keyword MONARCHY
    matrix = [
        ['M', 'O', 'N', 'A', 'R'],
        ['C', 'H', 'Y', 'B', 'D'],
        ['E', 'F', 'G', 'I', 'K'],
        ['L', 'P', 'Q', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Z']
    ]

    # Test ciphertext
    ciphertext = "GAGAGATL"

    # Decryption
    decrypted = playfair_decrypt(ciphertext, matrix)

    print("Ciphertext:", ciphertext)
    print("Decrypted Text:", decrypted)

    # Digraph frequency analysis
    frequency = digraph_frequency(ciphertext)

    print("\nDigraph Frequency:")

    for digraph, count in frequency.items():
        print(digraph, ":", count)

