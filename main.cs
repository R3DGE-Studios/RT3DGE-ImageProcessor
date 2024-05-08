using System;
using System.Drawing;

namespace ImageProcessor
{
    public class ImageProcessor
    {
        public static int[,] GetPixelValues(string imagePath, int width, int height)
        {
            // Load the image
            Bitmap image = new Bitmap(imagePath);

            // Resize the image to desired resolution
            Bitmap resizedImage = new Bitmap(image, new Size(width, height));

            // Initialize the array to store pixel values
            int[,] pixelValues = new int[height, width];

            // Iterate over each pixel and get its color
            for (int y = 0; y < resizedImage.Height; y++)
            {
                for (int x = 0; x < resizedImage.Width; x++)
                {
                    Color pixelColor = resizedImage.GetPixel(x, y);

                    // Store the RGB values in the array
                    pixelValues[y, x] = pixelColor.ToArgb();
                }
            }

            // Dispose of the images
            image.Dispose();
            resizedImage.Dispose();

            return pixelValues;
        }
    }
}
