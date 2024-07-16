#include <cs50.h>
#include <stdio.h>

int get_change(void);
int number_coins(int cents);

int main(void)
{
    int cents = get_change();
    printf("%i\n", number_coins(cents));
}

int get_change(void)
{
    int i;
    do
    {
        i = get_int("Change owed: ");
    }
    while (i < 0);
    return i;
}

int number_coins(int cents)
{
    int quarters = (cents - (cents % 25)) / 25;
    cents %= 25;
    int dimes = (cents - (cents % 10)) / 10;
    cents %= 10;
    int nickels = (cents - (cents % 5)) / 5;
    cents %= 5;
    int pennies = (cents - (cents % 1)) / 1;
    cents %= 1;
    int coins = quarters + dimes + nickels + pennies;
    return coins;
}
