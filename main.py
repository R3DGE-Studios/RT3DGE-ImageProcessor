import ctypes
import numpy as np

# Load the DLL
image_processor = ctypes.CDLL('ImageProcessor.dll')

# Define the function signature
image_processor.GetPixelValues.restype = ctypes.POINTER(ctypes.c_int * 10000)  # Assuming max image size of 100x100

def get_pixel_values(image_path, width, height):
    # Call the C# function
    pixel_values_ptr = image_processor.GetPixelValues(image_path.encode(), width, height)
    
    # Convert the pointer to a numpy array
    pixel_values_flat = np.ctypeslib.as_array(pixel_values_ptr.contents)
    
    # Reshape the flat array into a 2D array
    pixel_values = pixel_values_flat.reshape(height, width)
    
    return pixel_values

# Example usage
image_path = "path_to_your_image.png"  # Change this to your image file path
width = 100  # Change this to desired width
height = 100  # Change this to desired height

pixels = get_pixel_values(image_path, width, height)
print(pixels)
