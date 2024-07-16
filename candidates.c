#include <cs50.h>
#include <stdio.h>
#define NCANDIDATES 4

typedef struct
{
    string name;
    int votes;
} candidate;

int main(void)
{
    candidate candidates[NCANDIDATES];

    candidates[0].name = "Joe";
    candidates[0].votes = 1;

    candidates[1].name = "Trum";
    candidates[1].votes = 2;

    candidates[2].name = "Lul";
    candidates[2].votes = 3;

    candidates[3].name = "Bol";
    candidates[3].votes = 4;

    string biggest;

    // linear search
    for (int i = 0; i < 3; i++)
    {
        if (candidates[i].votes > candidates[i + 1].votes)
        {
            biggest = candidates[i].name;
        }
        else
        {
            biggest = candidates[i + 1].name;
        }
    }
    printf("%s\n", biggest);
}
