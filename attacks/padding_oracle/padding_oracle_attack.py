import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

BLOCK = 16


def pad(data):
    n = BLOCK - len(data) % BLOCK
    return data + bytes([n]) * n


def unpad(data):
    n = data[-1]
    if n < 1 or n > BLOCK or data[-n:] != bytes([n]) * n:
        raise ValueError("Invalid padding")
    return data[:-n]


def encrypt(message, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    enc = cipher.encryptor()
    return enc.update(pad(message)) + enc.finalize()


def create_oracle(key):
    count = [0]

    def oracle(ciphertext, iv):
        count[0] += 1
        try:
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            dec = cipher.decryptor()
            data = dec.update(ciphertext) + dec.finalize()
            unpad(data)
            return True
        except Exception:
            return False

    return oracle, count


def recover_block(block, previous, oracle):
    intermediate = bytearray(BLOCK)
    plaintext = bytearray(BLOCK)
    modified = bytearray(previous)

    for pad_value in range(1, BLOCK + 1):
        pos = BLOCK - pad_value

        for j in range(pos + 1, BLOCK):
            modified[j] = intermediate[j] ^ pad_value

        for guess in range(256):
            modified[pos] = guess

            if oracle(bytes(block), bytes(modified)):
                if pad_value == 1 and pos > 0:
                    test = bytearray(modified)
                    test[pos - 1] ^= 1
                    if not oracle(bytes(block), bytes(test)):
                        continue

                intermediate[pos] = guess ^ pad_value
                plaintext[pos] = intermediate[pos] ^ previous[pos]
                break
        else:
            raise RuntimeError("Could not recover a plaintext byte")

    return bytes(plaintext)


def attack(ciphertext, iv, oracle):
    blocks = [
        ciphertext[i:i + BLOCK]
        for i in range(0, len(ciphertext), BLOCK)
    ]

    result = b""
    previous = iv

    for block in blocks:
        result += recover_block(block, previous, oracle)
        previous = block

    return unpad(result)


def main():
    key = os.urandom(32)
    iv = os.urandom(BLOCK)
    message = input("Enter a test plaintext: ").encode("utf-8")

    ciphertext = encrypt(message, key, iv)

    # The key belongs to the oracle, not to the attack function.
    oracle, count = create_oracle(key)

    recovered = attack(ciphertext, iv, oracle)

    print("IV:", iv.hex())
    print("Ciphertext:", ciphertext.hex())
    print("Recovered plaintext:", recovered.decode())
    print("Oracle queries:", count[0])
    print("Success:", recovered == message)


if __name__ == "__main__":
    main()
