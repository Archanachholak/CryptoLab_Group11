def encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0

    for ch in plaintext:
        shift = ord(key[key_index % len(key)]) - ord('A')

        encrypted = chr(
            (ord(ch) - ord('A') + shift) % 26 + ord('A')
        )

        ciphertext += encrypted
        key_index += 1

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0

    for ch in ciphertext:
        shift = ord(key[key_index % len(key)]) - ord('A')

        decrypted = chr(
            (ord(ch) - ord('A') - shift) % 26 + ord('A')
        )

        plaintext += decrypted
        key_index += 1

    return plaintext
