from PIL import Image
import os
import math

# Function to calculate the lightness of a pixel
def calculate_lightness(pixel):
    r, g, b = pixel
    return (r + g + b) / 3 / 255  # Normalize to a range of 0 to 1

# Function to edit an image to make dark pixels transparent
def edit_image(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Ensure the image has an alpha channel
        img = img.convert("RGBA")

        # Get the pixel data
        pixels = img.load()

        # Define a minimum lightness threshold for logarithmic transformation
        min_lightness = 0.01

        # Loop through each pixel
        for x in range(img.width):
            for y in range(img.height):
                r, g, b, a = pixels[x, y]

                # Check if the pixel is fully transparent
                if a == 0:
                    continue  # Skip adjustment for fully transparent pixels

                # Calculate the lightness of the pixel
                lightness = calculate_lightness((r, g, b))

                # Apply a logarithmic transformation to determine alpha
                alpha = int(255 * math.log(1 + lightness) / math.log(1 + min_lightness))

                # Clamp alpha to the valid range [0, 255]
                alpha = max(0, min(255, alpha))

                # Set the pixel with adjusted alpha
                pixels[x, y] = (r, g, b, alpha)

        # Save the edited image in the same directory
        img.save(image_path, "PNG")

        print(f"Image '{image_path}' edited and saved.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory containing the PNG images you want to edit
image_directory = input("Enter the directory path to process: ")

# Edit all .png images in the directory
for filename in os.listdir(image_directory):
    if filename.endswith(".png"):
        image_path = os.path.join(image_directory, filename)
        edit_image(image_path)
