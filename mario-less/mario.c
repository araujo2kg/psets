#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;
    while (height < 1)
    {
        height = get_int("Height: "); // get_int deals with char/string inputs
    }
    for (int i = 1; i <= height; i++)
    {
        for (int j = 0; j < (height - i); j++)
        {
            printf(" ");
        }
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}
