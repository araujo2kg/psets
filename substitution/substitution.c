#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

string encrypt(string text, string key);

int main(int argc, string argv[])
{
    // Check for one argument
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    // Argument contains 26 chars
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    // Argument is alphabetical and do not repeat itself
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Key must be alphabetical.\n");
            return 1;
        }
        for (int j = 0; j < 26; j++)
        {
            if ((toupper(argv[1][i]) == toupper(argv[1][j])) && (i != j))
            {
                printf("Key must not repeat itself.\n");
                return 1;
            }
        }
    }
    string key = argv[1];
    string plaintext = get_string("plaintext:  ");
    string ciphertext = encrypt(plaintext, key);
    printf("ciphertext: %s\n", ciphertext);
}

string encrypt(string text, string key)
{
    int uindex;
    int lindex;
    for (int i = 0, length = strlen(text); i < length; i++)
    {
        if (isupper(text[i]))
        {
            uindex = text[i] - 'A';
            text[i] = toupper(key[uindex]);
        }
        else if (islower(text[i]))
        {
            lindex = text[i] - 'a';
            text[i] = tolower(key[lindex]);
        }
    }
    return text;
}
