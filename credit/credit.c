// Applies luhn algorithm to check if card number is valid
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int check_length(long card);
string check_type(long card);
int check_sum(long card, int length);

int main(void)
{
    long card = get_long("Number: ");
    int length = check_length(card);
    string type = check_type(card);
    int sum = check_sum(card, length) % 10;
    if (sum == 0 && strcmp(type, "INVALID") != 0)
    {
        printf("%s\n", type);
    }
    else
    {
        printf("INVALID\n");
    }
}

// Get the card number of digits
int check_length(long card)
{
    int length = 0;
    while (card > 0)
    {
        card /= 10;
        length++;
    }
    return length;
}

// Check if card is of correct type based on card number
string check_type(long card)
{
    int length = check_length(card);
    // Get card first digit
    int first_n = (card / (long) pow(10, length - 1));
    // Get card first two digits
    int first_two = (card / (long) pow(10, length - 2));

    if ((length == 15) && (first_two == 37 || first_two == 34))
    {
        return "AMEX";
    }
    else if ((length == 13 || length == 16) && (first_n == 4))
    {
        return "VISA";
    }
    else if ((length == 16) && (first_two == 51 || first_two == 52 || first_two == 53 || first_two == 54 || first_two == 55))
    {
        return "MASTERCARD";
    }
    else
    {
        return "INVALID";
    }
}

// Luhn algorithm to check if card number is valid
int check_sum(long card, int length)
{
    int sum = 0;
    int digit;
    for (int i = 0; i < length; i++)
    {
        // Get a specific digit of the card based on which iteration
        digit = (card / (long) pow(10, i) % 10);
        // Adds the digit to the total sum
        if (i % 2 == 0)
        {
            sum += digit;
        }
        else
        {
            if ((digit * 2) > 9)
            {
                sum += ((digit * 2) - 9);
            }
            else
            {
                sum += (digit * 2);
            }
        }
    }
    return sum;
}
