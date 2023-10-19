import os
from PIL import Image
import math

def create_image_grid(directory_path, output_file):
    # List all PNG files in the directory
    image_files = [f for f in os.listdir(directory_path) if f.endswith(".png")]

    if not image_files:
        print("No PNG files found in the specified directory.")
        return

    # Sort the image files to maintain order
    image_files.sort()

    # Calculate the number of rows and columns in the grid
    num_images = len(image_files)
    # Calculate the number of columns to make the resulting image closer to a square
    num_columns = int(math.sqrt(num_images)) if num_images > 0 else 1
    num_rows = (num_images + num_columns - 1) // num_columns

    # Ensure the output file has the ".png" extension
    if not output_file.lower().endswith(".png"):
        output_file += ".png"

    # Calculate the size of the resulting image
    image_size = (num_columns * 16, num_rows * 16)

    # Create a new blank image to assemble the tiles
    result_image = Image.new("RGBA", image_size, (255, 255, 255, 0))

    # Iterate over the image files and paste them into the result image
    for i, image_file in enumerate(image_files):
        image = Image.open(os.path.join(directory_path, image_file))
        x = (i % num_columns) * 16
        y = (i // num_columns) * 16
        result_image.paste(image, (x, y))

    # Save the resulting image in the source directory
    output_path = os.path.join(directory_path, output_file)
    result_image.save(output_path)

    print(f"Created {output_path} with {num_images} images tiled in a {num_columns}x{num_rows} grid.")

if __name__ == "__main__":
    directory_path = input("Enter the directory path containing PNG images: ")
    output_file = input("Enter the output file name (e.g., result): ")

    create_image_grid(directory_path, output_file)
