from vigenere import encrypt


def verify(plaintext, key, original_ciphertext):
    encrypted = encrypt(plaintext, key)

    return encrypted == original_ciphertext

