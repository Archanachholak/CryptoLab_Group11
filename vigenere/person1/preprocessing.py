import re


def clean_ciphertext(ciphertext):
    """
    Remove spaces and special characters
    and convert ciphertext to uppercase.
    """
    cleaned = re.sub(r'[^A-Za-z]', '', ciphertext)
    return cleaned.upper()
