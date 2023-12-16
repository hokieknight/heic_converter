"""Module to convert HEIC to JPG files"""
import os
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def convert_heic_to_jpg(heic_path, jpg_output_path):
    """convert one file from heic to jpg"""
    try:
        # Open the HEIC image
        img = Image.open(heic_path)
        # Save as JPG
        img.convert("RGB").save(jpg_output_path, "JPEG")
        print(f"Conversion successful: {heic_path} -> {jpg_output_path}")
    except Exception as e:
        print(f"Error converting {heic_path}: {e}")
    return True

def batch_convert_heic_to_jpg(input_folder, output_folder):
    """convert all heic files in a folder"""
    # Create the output folder if it doesn't exist
    print(output_folder)
    os.makedirs(output_folder, exist_ok=True)

    count = 0
    # Iterate through HEIC files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(input_folder, filename)
            jpg_output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
            if convert_heic_to_jpg(heic_path, jpg_output_path):
                count += 1
            #print(f"{heic_path} => {jpg_output_path}")
    print (f"{count} files converted")

# Example Usage:
# Specify your input and output folders
input_folder = ".\\test"
output_folder = ".\\test\\jpg_output"

# Convert HEIC files to JPG
batch_convert_heic_to_jpg(input_folder, output_folder)
print("done")
