#include "helpers.h"
#include <math.h>

int get_smaller(int a, int b);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calculates average of rgb
            average = round(
                ((float) image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3);
            // When rgb is equal we have a shade of gray
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int red;
    int green;
    int blue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Algorithm returns the sepia value, if sepia value > 255(8bit) > get smaller returns
            // 255 Color value stored in uint8_t/byte(0 to 255)
            red = get_smaller(round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen +
                                    .189 * image[i][j].rgbtBlue),
                              255);
            green = get_smaller(round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen +
                                      .168 * image[i][j].rgbtBlue),
                                255);
            blue = get_smaller(round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen +
                                     .131 * image[i][j].rgbtBlue),
                               255);

            image[i][j].rgbtRed = red;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtBlue = blue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int temp;
    for (int i = 0; i < height; i++)
    {
        // (width / 2) iterate over half the row, because the operation swaps the left row to the
        // right, no need to iterate over entire row
        for (int j = 0; j < (width / 2); j++)
        {
            // Swap image[row][column] to its equivalent image[row][column]
            temp = image[i][j].rgbtRed;
            image[i][j].rgbtRed = image[i][(width - 1) - j].rgbtRed;
            image[i][(width - 1) - j].rgbtRed = temp;

            temp = image[i][j].rgbtGreen;
            image[i][j].rgbtGreen = image[i][(width - 1) - j].rgbtGreen;
            image[i][(width - 1) - j].rgbtGreen = temp;

            temp = image[i][j].rgbtBlue;
            image[i][j].rgbtBlue = image[i][(width - 1) - j].rgbtBlue;
            image[i][(width - 1) - j].rgbtBlue = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Creates a copy of the image, so we can work with the original values in the blurred image.
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Applies the blur in a 3x3 box around the j pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redsum = 0;
            int greensum = 0;
            int bluesum = 0;
            float counter = 0;
            for (int row = -1; row <= 1; row++)
            {
                for (int col = -1; col <= 1; col++)
                {
                    // Checks if position is within image bounds
                    if (i + row >= 0 && i + row < height && j + col >= 0 && j + col < width)
                    {
                        // Adds color value to sums
                        redsum += copy[i + row][j + col].rgbtRed;
                        greensum += copy[i + row][j + col].rgbtGreen;
                        bluesum += copy[i + row][j + col].rgbtBlue;
                        counter++;
                    }
                }
            }
            image[i][j].rgbtRed = round(redsum / counter);
            image[i][j].rgbtGreen = round(greensum / counter);
            image[i][j].rgbtBlue = round(bluesum / counter);
        }
    }
}

// Return the smaller integer
int get_smaller(int a, int b)
{
    if (a > b)
        return b;
    else
        return a;
}
