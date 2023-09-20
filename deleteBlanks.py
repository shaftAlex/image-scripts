import os
from PIL import Image

def is_completely_black(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        width, height = img.size

        for x in range(width):
            for y in range(height):
                pixel = img.getpixel((x, y))
                if pixel != (0, 0, 0):
                    return False
        return True

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return False

def delete_black_png_files(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(".png"):
                file_path = os.path.join(root, file)
                if is_completely_black(file_path):
                    print(f"Deleting {file_path}")
                    os.remove(file_path)

if __name__ == "__main__":
    directory_path = input("Enter the directory path to process: ")
    delete_black_png_files(directory_path)