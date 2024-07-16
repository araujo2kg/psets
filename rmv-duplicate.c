#include <stdio.h>

int removeDuplicates(int* nums, int numsSize);

int main(int argc, char* argv[])
{
    int non_decreasing_n[] = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5};
    int size = sizeof(non_decreasing_n) / sizeof(int);
    printf("Unique numbers: %i\n", removeDuplicates(non_decreasing_n, size));

}

int removeDuplicates(int* nums, int numsSize) {
    int index = 1;

    for (int i = 1; i < numsSize; i++)
    {
        if (nums[i] != nums[i - 1])
        {
            nums[index] = nums[i];
            index++;
        }
    }
    return index;
}
