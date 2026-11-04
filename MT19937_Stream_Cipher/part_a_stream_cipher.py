
import random

# Generate keystream and perform encryption/decryption
def stream_cipher(data, seed):

    # Initialize MT19937 with the given seed
    rng = random.Random(seed)

    result = bytearray()

    # Generate one 8-bit keystream value per byte
    for byte in data:
        key_byte = rng.getrandbits(8)

        # XOR data byte with keystream byte
        result.append(byte ^ key_byte)

    return bytes(result)


def recover_seed(ciphertext):

    known_pattern = b"A" * 14

    candidates_tested = 0

    # Try every possible 16-bit seed
    for candidate_seed in range(65536):

        candidates_tested += 1

        # Decrypt ciphertext using candidate seed
        decrypted = stream_cipher(ciphertext, candidate_seed)

        # Check whether the known pattern exists
        if known_pattern in decrypted:

            return candidate_seed, decrypted, candidates_tested

    return None, None, candidates_tested



# Test the stream cipher

    

if __name__ == "__main__":

    import string

    # Generate random printable prefix
    prefix_length = random.randint(5, 20)

    prefix = ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(prefix_length)
    )

    # Generate plaintext
    plaintext_message = prefix + "A" * 14
    plaintext = plaintext_message.encode()

    # Generate random 16-bit seed
    seed = random.randint(0, 65535)

    # Encrypt plaintext
    ciphertext = stream_cipher(plaintext, seed)

    print("\n========== ENCRYPTION ==========")
    print("Original Plaintext:", plaintext_message)
    print("Original Seed:", seed)
    print("Ciphertext (Hex):", ciphertext.hex())

    # Attacker attempts to recover seed
    print("\n========== SEED RECOVERY ATTACK ==========")

    recovered_seed, recovered_plaintext, tested = recover_seed(ciphertext)

    print("Total Candidates Tested:", tested)

    if recovered_seed is not None:

        print("Recovered Seed:", recovered_seed)
        print("Recovered Plaintext:", recovered_plaintext.decode())

        print("\n========== VERIFICATION ==========")

        print("Seed Matches:", recovered_seed == seed)
        print("Plaintext Matches:", recovered_plaintext == plaintext)
        print("Known Pattern Found:", b"A" * 14 in recovered_plaintext)

        if recovered_seed == seed and recovered_plaintext == plaintext:
            print("Attack Successful!")
        else:
            print("Verification Failed!")

    else:
        print("No matching seed found.")


