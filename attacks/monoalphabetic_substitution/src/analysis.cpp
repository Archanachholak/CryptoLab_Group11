#include "analysis.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

// Structure to store information about one letter
struct LetterFrequency
{
    char letter;
    int count;
    double percentage;
};


void frequency_analysis(const string& ciphertext)
{
    // Array to store frequency of A-Z
    int count[26] = {0};

    // Total number of alphabetic characters
    int totalLetters = 0;

    // Count every alphabetic character
    for (char ch : ciphertext)
    {
        if (isalpha(static_cast<unsigned char>(ch)))
        {
            char upper = toupper(static_cast<unsigned char>(ch));

            count[upper - 'A']++;

            totalLetters++;
        }
    }

    // Create a vector containing letter frequency information
    vector<LetterFrequency> frequency;

    for (int i = 0; i < 26; i++)
    {
        double percentage = 0.0;

        if (totalLetters > 0)
        {
            percentage =
                (count[i] * 100.0) / totalLetters;
        }

        LetterFrequency item;

        item.letter = static_cast<char>('A' + i);
        item.count = count[i];
        item.percentage = percentage;

        frequency.push_back(item);
    }

    // Sort from highest frequency to lowest frequency
    sort(
        frequency.begin(),
        frequency.end(),
        [](const LetterFrequency& a,
           const LetterFrequency& b)
        {
            return a.count > b.count;
        }
    );

    // Display results
    cout << "\n========================================\n";
    cout << "       LETTER FREQUENCY ANALYSIS\n";
    cout << "========================================\n";

    cout << "\nTotal alphabetic characters: "
         << totalLetters << "\n\n";

    cout << "Letter\tCount\tPercentage\n";
    cout << "----------------------------------------\n";

    for (const auto& item : frequency)
    {
        cout << item.letter
             << "\t"
             << item.count
             << "\t"
             << item.percentage
             << "%\n";
    }

    // Display most frequent letters
    cout << "\n========================================\n";
    cout << "       MOST FREQUENT LETTERS\n";
    cout << "========================================\n";

    int numberToDisplay = 5;

    for (int i = 0; i < numberToDisplay; i++)
    {
        cout << i + 1 << ". "
             << frequency[i].letter
             << " -> "
             << frequency[i].count
             << " occurrences ("
             << frequency[i].percentage
             << "%)\n";
    }

    // Save frequency analysis to a file
    ofstream output("../output/frequency.txt");

    if (!output)
    {
        cout << "\nError: Could not create frequency.txt\n";
        return;
    }

    output << "LETTER FREQUENCY ANALYSIS\n";
    output << "=========================\n\n";

    output << "Total alphabetic characters: "
           << totalLetters
           << "\n\n";

    output << "Letter\tCount\tPercentage\n";
    output << "----------------------------------------\n";

    for (const auto& item : frequency)
    {
        output << item.letter
               << "\t"
               << item.count
               << "\t"
               << item.percentage
               << "%\n";
    }

    output << "\nMOST FREQUENT LETTERS\n";
    output << "=====================\n";

    for (int i = 0; i < numberToDisplay; i++)
    {
        output << i + 1 << ". "
               << frequency[i].letter
               << " -> "
               << frequency[i].count
               << " occurrences ("
               << frequency[i].percentage
               << "%)\n";
    }

    output.close();

    cout << "\nFrequency analysis saved to:"
         << " output/frequency.txt\n";
}


// Temporary functions.
// We will implement these in the next steps.
void word_frequency_analysis(const string& ciphertext)
{
    vector<string> words;
    string currentWord = "";

    // Extract words manually
    for (int i = 0; i < (int)ciphertext.length(); i++)
    {
        char ch = ciphertext[i];

        if (isalpha(static_cast<unsigned char>(ch)))
        {
            currentWord +=
                toupper(static_cast<unsigned char>(ch));
        }
        else
        {
            if (currentWord.length() > 0)
            {
                words.push_back(currentWord);
                currentWord = "";
            }
        }
    }

    // Add final word if necessary
    if (currentWord.length() > 0)
    {
        words.push_back(currentWord);
    }

    cout << "\n========================================\n";
    cout << "       WORD FREQUENCY ANALYSIS\n";
    cout << "========================================\n";

    // ------------------------------------
    // One-letter words
    // ------------------------------------

    cout << "\nONE-LETTER WORDS\n";
    cout << "----------------\n";

    for (int i = 0; i < (int)words.size(); i++)
    {
        if (words[i].length() == 1)
        {
            cout << words[i] << " ";
        }
    }

    cout << "\n";

    // ------------------------------------
    // Two-letter words
    // ------------------------------------

    cout << "\nTWO-LETTER WORDS\n";
    cout << "----------------\n";

    for (int i = 0; i < (int)words.size(); i++)
    {
        if (words[i].length() == 2)
        {
            cout << words[i] << " ";
        }
    }

    cout << "\n";

    // ------------------------------------
    // Three-letter words
    // ------------------------------------

    cout << "\nTHREE-LETTER WORDS\n";
    cout << "------------------\n";

    for (int i = 0; i < (int)words.size(); i++)
    {
        if (words[i].length() == 3)
        {
            cout << words[i] << " ";
        }
    }

    cout << "\n";

    // ------------------------------------
    // Count repeated words
    // ------------------------------------

    vector<string> uniqueWords;
    vector<int> wordCounts;

    for (int i = 0; i < (int)words.size(); i++)
    {
        bool found = false;

        for (int j = 0; j < (int)uniqueWords.size(); j++)
        {
            if (words[i] == uniqueWords[j])
            {
                wordCounts[j]++;
                found = true;
                break;
            }
        }

        if (!found)
        {
            uniqueWords.push_back(words[i]);
            wordCounts.push_back(1);
        }
    }

    cout << "\nREPEATED WORDS\n";
    cout << "--------------\n";

    for (int i = 0; i < (int)uniqueWords.size(); i++)
    {
        if (wordCounts[i] > 1)
        {
            cout << uniqueWords[i]
                 << " -> "
                 << wordCounts[i]
                 << " times\n";
        }
    }

    // ------------------------------------
    // Save results
    // ------------------------------------

    ofstream output("../output/word_frequency.txt");

    if (!output)
    {
        cout << "\nError: Could not create word_frequency.txt\n";
        return;
    }

    output << "WORD FREQUENCY ANALYSIS\n";
    output << "=======================\n\n";

    output << "ONE-LETTER WORDS\n";
    output << "----------------\n";

    for (int i = 0; i < (int)words.size(); i++)
    {
        if (words[i].length() == 1)
        {
            output << words[i] << " ";
        }
    }

    output << "\n\n";

    output << "TWO-LETTER WORDS\n";
    output << "----------------\n";

    for (int i = 0; i < (int)words.size(); i++)
    {
        if (words[i].length() == 2)
        {
            output << words[i] << " ";
        }
    }

    output << "\n\n";

    output << "THREE-LETTER WORDS\n";
    output << "------------------\n";

    for (int i = 0; i < (int)words.size(); i++)
    {
        if (words[i].length() == 3)
        {
            output << words[i] << " ";
        }
    }

    output << "\n\n";

    output << "REPEATED WORDS\n";
    output << "--------------\n";

    for (int i = 0; i < (int)uniqueWords.size(); i++)
    {
        if (wordCounts[i] > 1)
        {
            output << uniqueWords[i]
                   << " -> "
                   << wordCounts[i]
                   << " times\n";
        }
    }

    output.close();

    cout << "\nWord frequency analysis saved to:"
         << " output/word_frequency.txt\n";
}

string get_pattern(const string& word)
{
    string pattern = "";
    
    int nextNumber = 0;

    // Store the letters that have already appeared
    vector<char> letters;

    for (int i = 0; i < (int)word.length(); i++)
    {
        char current = word[i];

        int position = -1;

        // Check whether this letter has appeared before
        for (int j = 0; j < (int)letters.size(); j++)
        {
            if (letters[j] == current)
            {
                position = j;
                break;
            }
        }

        if (position == -1)
        {
            // New letter
            letters.push_back(current);

            pattern += to_string(nextNumber);

            nextNumber++;
        }
        else
        {
            // Repeated letter
            pattern += to_string(position);
        }
    }

    return pattern;
}

void pattern_analysis(const string& ciphertext)
{
    vector<string> words;
    string currentWord = "";

    // ----------------------------------------
    // Extract words from ciphertext
    // ----------------------------------------

    for (int i = 0; i < (int)ciphertext.length(); i++)
    {
        char ch = ciphertext[i];

        if (isalpha(static_cast<unsigned char>(ch)))
        {
            currentWord +=
                toupper(static_cast<unsigned char>(ch));
        }
        else
        {
            if (currentWord.length() > 0)
            {
                words.push_back(currentWord);
                currentWord = "";
            }
        }
    }

    // Add final word
    if (currentWord.length() > 0)
    {
        words.push_back(currentWord);
    }

    cout << "\n========================================\n";
    cout << "          PATTERN ANALYSIS\n";
    cout << "========================================\n";

    // ----------------------------------------
    // Display pattern of every word
    // ----------------------------------------

    cout << "\nWORD PATTERNS\n";
    cout << "-------------\n";

    for (int i = 0; i < (int)words.size(); i++)
    {
        string pattern = get_pattern(words[i]);

        cout << words[i]
             << " -> "
             << pattern
             << "\n";
    }

    // ----------------------------------------
    // Find repeated patterns
    // ----------------------------------------

    vector<string> uniquePatterns;
    vector<int> patternCounts;

    for (int i = 0; i < (int)words.size(); i++)
    {
        string pattern = get_pattern(words[i]);

        bool found = false;

        for (int j = 0; j < (int)uniquePatterns.size(); j++)
        {
            if (uniquePatterns[j] == pattern)
            {
                patternCounts[j]++;
                found = true;
                break;
            }
        }

        if (!found)
        {
            uniquePatterns.push_back(pattern);
            patternCounts.push_back(1);
        }
    }

    // ----------------------------------------
    // Display repeated patterns
    // ----------------------------------------

    cout << "\nREPEATED PATTERNS\n";
    cout << "-----------------\n";

    for (int i = 0; i < (int)uniquePatterns.size(); i++)
    {
        if (patternCounts[i] > 1)
        {
            cout << uniquePatterns[i]
                 << " -> "
                 << patternCounts[i]
                 << " occurrences\n";

            cout << "Words: ";

            for (int j = 0; j < (int)words.size(); j++)
            {
                if (get_pattern(words[j]) ==
                    uniquePatterns[i])
                {
                    cout << words[j] << " ";
                }
            }

            cout << "\n\n";
        }
    }

    // ----------------------------------------
    // Save results
    // ----------------------------------------

    ofstream output("../output/pattern_analysis.txt");

    if (!output)
    {
        cout << "\nError: Could not create pattern_analysis.txt\n";
        return;
    }

    output << "PATTERN ANALYSIS\n";
    output << "================\n\n";

    output << "WORD PATTERNS\n";
    output << "-------------\n";

    for (int i = 0; i < (int)words.size(); i++)
    {
        output << words[i]
               << " -> "
               << get_pattern(words[i])
               << "\n";
    }

    output << "\nREPEATED PATTERNS\n";
    output << "-----------------\n";

    for (int i = 0; i < (int)uniquePatterns.size(); i++)
    {
        if (patternCounts[i] > 1)
        {
            output << uniquePatterns[i]
                   << " -> "
                   << patternCounts[i]
                   << " occurrences\n";

            output << "Words: ";

            for (int j = 0; j < (int)words.size(); j++)
            {
                if (get_pattern(words[j]) ==
                    uniquePatterns[i])
                {
                    output << words[j] << " ";
                }
            }

            output << "\n\n";
        }
    }

    output.close();

    cout << "\nPattern analysis saved to:"
         << " output/pattern_analysis.txt\n";
}

