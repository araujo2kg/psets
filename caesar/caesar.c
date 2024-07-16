#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string rotate(string text, int key);

int main(int argc, string argv[])
{
    // Assures just 1 argument given
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    // Assures argument is numeric
    if (argc == 2)
    {
        for (int i = 0, length = strlen(argv[1]); i < length; i++)
        {
            if (isdigit(argv[1][i]) == 0)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
    }
    // Convert key to int
    int key = atoi(argv[1]);
    string plaintext = get_string("plaintext:  ");
    // Apply cipher to input
    string ciphertext = rotate(plaintext, key);
    printf("ciphertext: %s\n", ciphertext);
}

// Apply encryption based on key input
string rotate(string text, int key)
{
    for (int i = 0, length = strlen(text); i < length; i++)
    {
        if (isupper(text[i]))
        {
            text[i] -= 'A';
            text[i] = (text[i] + key) % 26;
            text[i] += 'A';
        }
        else if (islower(text[i]))
        {
            text[i] -= 'a';
            text[i] = (text[i] + key) % 26;
            text[i] += 'a';
        }
    }
    return text;
}
