#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

void calc_scrabble(string word1, string word2);

int scores[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(void)
{
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");
    calc_scrabble(word1, word2);
}

void calc_scrabble(string word1, string word2)
{
    int sum1 = 0;
    int sum2 = 0;

    // Calculate player 1 score
    for (int i = 0, length = strlen(word1); i < length; i++)
    {
        word1[i] = toupper(word1[i]);
        if (word1[i] >= 65 && word1[i] <= 90)
        {
            sum1 += scores[word1[i] - 'A'];
        }
    }
    // Calculate player 2 score
    for (int i = 0, length = strlen(word2); i < length; i++)
    {
        word2[i] = toupper(word2[i]);
        if (word2[i] >= 65 && word2[i] <= 90)
        {
            sum2 += scores[word2[i] - 'A'];
        }
    }
    // Announce winner
    if (sum1 > sum2)
        printf("Player 1 wins!\n");
    else if (sum2 > sum1)
        printf("Player 2 wins!\n");
    else
        printf("Tie!\n");
}
