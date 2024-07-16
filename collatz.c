#include <cs50.h>
#include <stdio.h>

int collatz(int n, int steps);

int main(void)
{
    int counter = 0;
    int value;
    do
    {
        value = get_int("Positive int: ");
    } while(value < 1);

    printf("Collatz of %i = %i\n", value, collatz(value, counter));
}

int collatz(int n, int steps)
{
    if (n < 2)
    {
        return steps;
    }
    if (n % 2 == 0)
    {
        steps++;
        return collatz(n/2, steps);
    }
    else
    {
        steps++;
        return collatz((3 * n) + 1, steps);
    }
}
