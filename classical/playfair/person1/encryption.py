def generate_key_matrix(keyword):
    """
    Generate a 5x5 Playfair key matrix.

    I and J are treated as the same character.
    """

    keyword = keyword.upper().replace("J", "I")

    # Remove anything that isn't a letter
    keyword = "".join(
        char for char in keyword
        if char.isalpha()
    )

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    sequence = ""

    # Add keyword characters first
    for char in keyword:
        if char not in sequence:
            sequence += char

    # Add remaining alphabet characters
    for char in alphabet:
        if char not in sequence:
            sequence += char

    # Convert to 5x5 matrix
    matrix = []

    for i in range(0, 25, 5):
        matrix.append(list(sequence[i:i + 5]))

    return matrix


def find_position(matrix, letter):
    """
    Find the row and column of a letter in the key matrix.
    """

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col

    raise ValueError(f"Letter {letter} not found in matrix")


def playfair_encrypt(digraphs, matrix):
    """
    Encrypt prepared Playfair digraphs.
    """

    ciphertext = ""

    for digraph in digraphs:

        first = digraph[0]
        second = digraph[1]

        row1, col1 = find_position(matrix, first)
        row2, col2 = find_position(matrix, second)

        # Same row
        if row1 == row2:
            encrypted_first = matrix[row1][(col1 + 1) % 5]
            encrypted_second = matrix[row2][(col2 + 1) % 5]

        # Same column
        elif col1 == col2:
            encrypted_first = matrix[(row1 + 1) % 5][col1]
            encrypted_second = matrix[(row2 + 1) % 5][col2]

        # Rectangle rule
        else:
            encrypted_first = matrix[row1][col2]
            encrypted_second = matrix[row2][col1]

        ciphertext += encrypted_first + encrypted_second

    return ciphertext


if __name__ == "__main__":
    matrix = generate_key_matrix("MONARCHY")

    print("Key Matrix:")

    for row in matrix:
        print(" ".join(row))