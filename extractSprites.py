from PIL import Image
import os
import glob

def is_empty(sprite):
    return sprite.getextrema() == ((0, 0, 0, 0),)

def extract_sprites_from_folder(folder_path):
    try:
        # List all PNG files in the specified folder
        image_files = glob.glob(os.path.join(folder_path, '*.png'))

        for image_file in image_files:
            # Open the input image
            img = Image.open(image_file)

            # Check if the image has the right dimensions for 16x16 sprites
            if img.width % 16 != 0 or img.height % 16 != 0:
                print(f"Image '{image_file}' dimensions are not compatible with 16x16 pixel sprites.")
                continue

            # Create a directory to save the extracted sprites
            output_directory = os.path.dirname(image_file)
            base_filename = os.path.splitext(os.path.basename(image_file))[0]

            extracted_count = 0  # To keep track of the extracted sprites

            # Loop through and extract 16x16 pixel areas
            for y in range(0, img.height, 16):
                for x in range(0, img.width, 16):
                    sprite = img.crop((x, y, x + 16, y + 16))

                    # Check if the sprite is empty
                    if not is_empty(sprite):
                        sprite_filename = f"{base_filename}-{extracted_count}.png"
                        sprite_path = os.path.join(output_directory, sprite_filename)
                        sprite.save(sprite_path, "PNG")
                        extracted_count += 1

            print(f"{extracted_count} non-empty sprites extracted from '{image_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing PNG images: ")
    extract_sprites_from_folder(folder_path)
