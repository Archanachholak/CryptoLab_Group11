#include "cipher.h"

#include <cctype>

using namespace std;

string encrypt(const string& plaintext, const string& key)
{
    string ciphertext = plaintext;

    for (int i = 0; i < (int)plaintext.length(); i++)
    {
        char ch = plaintext[i];

        // Check whether the character is a letter
        if (isalpha(static_cast<unsigned char>(ch)))
        {
            // Convert lowercase letters to uppercase
            char upper = toupper(static_cast<unsigned char>(ch));

            // Find position of the letter in A-Z
            int position = upper - 'A';

            // Replace using substitution key
            ciphertext[i] = key[position];
        }
        else
        {
            // Keep spaces, numbers and punctuation unchanged
            ciphertext[i] = ch;
        }
    }

    return ciphertext;
}
