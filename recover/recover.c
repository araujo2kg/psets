#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check for correct number of arguments
    if (argc != 2)
    {
        printf("Usage: ./recover filename.\n");
        return 1;
    }

    // Tries to open the file
    FILE *inpt = fopen(argv[1], "r");
    if (inpt == NULL)
    {
        printf("Error opening file.\n");
        return 1;
    }

    int filecount = 0;
    uint8_t block[512];
    FILE *file = NULL;
    while (fread(block, 1, 512, inpt) > 0)
    {
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && ((block[3] & 0xf0) == 0xe0))
        {
            if (file != NULL)
            {
                fclose(file);
                file = NULL;
            }
            char filename[10];
            sprintf(filename, "%03i.jpg", filecount);
            file = fopen(filename, "w");
            fwrite(block, 1, 512, file);
            filecount++;
        }
        else if (file != NULL)
        {
            fwrite(block, 1, 512, file);
        }
    }
    if (file != NULL)
    {
        fclose(file);
        file = NULL;
    }
    fclose(inpt);
}
