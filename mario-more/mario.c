#include <cs50.h>
#include <stdio.h>

int get_height(void);
void print_pyramid(int size);

int main(void)
{
    int height = get_height();
    print_pyramid(height);
}

int get_height(void)
{
    int i;
    do
    {
        i = get_int("Height: ");
    }
    while (i < 1 || i > 8);
    return i;
}

void print_pyramid(int size)
{
    // iterate over equivalent lines
    for (int i = 1; i <= size; i++)
    {
        // print the spaces
        for (int j = 0; j < (size - i); j++)
        {
            printf(" ");
        }
        // print left side bricks
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        // print the divisors
        printf("  ");
        // print right side bricks
        for (int l = 0; l < i; l++)
        {
            printf("#");
        }
        // jump line
        printf("\n");
    }
}
