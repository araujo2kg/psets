#include "helpers.h"
#include <math.h>

float gx(int color, int position);
float gy(int color, int position);

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
    };
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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of the image so we can work with the original values
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Gradient kernels
    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Line
    for (int i = 0; i < height; i++)
    {
        // Pixel
        for (int j = 0; j < width; j++)
        {
            // Gx sum
            float gxredsum = 0;
            float gxgreensum = 0;
            float gxbluesum = 0;
            // Gy sum
            float gyredsum = 0;
            float gygreensum = 0;
            float gybluesum = 0;
            // Row
            for (int row = -1; row <= 1; row++)
            {
                // Column
                for (int col = -1; col <= 1; col++)
                {
                    // Checks if position is within image bounds
                    if (i + row >= 0 && i + row < height && j + col >= 0 && j + col < width)
                    {
                        gxredsum += copy[i + row][j + col].rgbtRed * gx[row + 1][col + 1];
                        gxgreensum += copy[i + row][j + col].rgbtGreen * gx[row + 1][col + 1];
                        gxbluesum += copy[i + row][j + col].rgbtBlue * gx[row + 1][col + 1];

                        gyredsum += copy[i + row][j + col].rgbtRed * gy[row + 1][col + 1];
                        gygreensum += copy[i + row][j + col].rgbtGreen * gy[row + 1][col + 1];
                        gybluesum += copy[i + row][j + col].rgbtBlue * gy[row + 1][col + 1];
                    }
                }
            }
            // Calculate edge
            float grad_red = round(sqrt(pow(gxredsum, 2) + pow(gyredsum, 2)));
            float grad_green = round(sqrt(pow(gxgreensum, 2) + pow(gygreensum, 2)));
            float grad_blue = round(sqrt(pow(gxbluesum, 2) + pow(gybluesum, 2)));
            // New values for the edge images goes here
            image[i][j].rgbtRed = (grad_red > 255 ? 255 : grad_red);
            image[i][j].rgbtGreen = (grad_green > 255 ? 255 : grad_green);
            image[i][j].rgbtBlue = (grad_blue > 255 ? 255 : grad_blue);
        }
    }
}
