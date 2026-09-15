#include <iostream>
#include <fstream>
#include <string>

#include "cipher.h"
#include "analysis.h"


using namespace std;

int main()
{
    // Open plaintext file
    ifstream input("../input/plaintext.txt");

    if (!input)
    {
        cout << "Error: Could not open plaintext.txt" << endl;
        return 1;
    }

    // Read the complete plaintext
    string plaintext;
    string line;

    while (getline(input, line))
    {
        plaintext += line;
        plaintext += "\n";
    }

    input.close();

    // Monoalphabetic substitution key
    string key = "QWERTYUIOPASDFGHJKLZXCVBNM";

    // Encrypt the plaintext
    string ciphertext = encrypt(plaintext, key);

    // Display ciphertext
    cout << "========================================" << endl;
    cout << "       MONOALPHABETIC CIPHER" << endl;
    cout << "========================================" << endl;

    cout << "\nCiphertext:\n\n";
    cout << ciphertext << endl;

    // Save ciphertext to output file
    ofstream output("../output/ciphertext.txt");

    if (!output)
    {
        cout << "Error: Could not create ciphertext.txt" << endl;
        return 1;
    }

    output << ciphertext;

    output.close();

    cout << "\n========================================" << endl;
cout << "Ciphertext saved to output/ciphertext.txt" << endl;
cout << "========================================" << endl;

// Perform frequency analysis
frequency_analysis(ciphertext);

word_frequency_analysis(ciphertext);

pattern_analysis(ciphertext);

return 0;


}
