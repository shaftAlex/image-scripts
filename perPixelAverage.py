from PIL import Image
import os

# Function to get a list of all PNG files in the specified directory
def get_png_files(directory):
    png_files = [f for f in os.listdir(directory) if f.endswith('.png')]
    return png_files

# Function to combine and average images pixel-wise
def average_images(directory):
    image_files = get_png_files(directory)

    if not image_files:
        print("No PNG images found in the specified directory.")
        return

    images = [Image.open(os.path.join(directory, file)) for file in image_files]

    # Ensure all images have the same size (16x16 pixels)
    image_size = images[0].size
    for img in images:
        if img.size != image_size:
            print("All images should have the same size (16x16 pixels).")
            return

    # Extract the base name from one of the image files (e.g., "planks" from "planks-10.png")
    base_name = os.path.splitext(image_files[0])[0].split('-')[0]

    # Initialize an empty image to store the average
    average_image = Image.new('RGB', image_size, (0, 0, 0))

    # Iterate through each pixel and calculate the average across all images
    for x in range(image_size[0]):
        for y in range(image_size[1]):
            pixel_values = [img.getpixel((x, y)) for img in images]
            average_pixel = tuple(sum(value[i] for value in pixel_values) / len(pixel_values) for i in range(3))
            average_image.putpixel((x, y), tuple(map(int, average_pixel)))

    # Create the resulting filename using the base name
    result_filename = f"{base_name}-average.png"

    # Save the resulting image with the new filename
    average_image.save(os.path.join(directory, result_filename))
    print(f"Average image saved as '{result_filename}' in the specified directory.")

if __name__ == "__main__":
    directory = input("Please specify the directory containing PNG images: ")
    
    if os.path.exists(directory) and os.path.isdir(directory):
        average_images(directory)
    else:
        print("The specified directory does not exist or is not a directory.")
