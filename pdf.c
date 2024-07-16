#include <stdint.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
        return 1;

    FILE *src = fopen(argv[1], "r");
    if (src == NULL)
    {
        printf("File not available\n");
        return 1;
    }
    uint8_t buffer[4];
    if (fread(buffer, sizeof(uint8_t), 4, src) == 4)
    {
        printf("Success\n");
    }

    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", buffer[i]); // %x can be used as placeholder to print the hex equivalent.
    }
    fclose(src);
}
