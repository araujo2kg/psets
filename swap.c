#include <stdio.h>

void swap(int *i, int *j);

int main(void)
{
    int a = 11;
    int b = 22;

    printf("a = %i and b = %i\n", a, b);
    swap(&a, &b);
    printf("a = %i and b = %i\n", a, b);


}

void swap(int *i, int *j)
{
    int tmp = *i;
    *i = *j;
    *j = tmp;
}
