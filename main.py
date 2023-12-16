from PIL import Image
import os

def convert_heic_to_jpg(heic_path, jpg_output_path):
    try:
        # Open the HEIC image
        with Image.open(heic_path) as img:
            # Save as JPG
            img.convert("RGB").save(jpg_output_path, "JPEG")
            print(f"Conversion successful: {heic_path} -> {jpg_output_path}")
    except Exception as e:
        print(f"Error converting {heic_path}: {e}")

def batch_convert_heic_to_jpg(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through HEIC files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(input_folder, filename)
            jpg_output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
            convert_heic_to_jpg(heic_path, jpg_output_path)

# Example Usage:
# Specify your input and output folders
input_folder = "/path/to/heic_files"
output_folder = "/path/to/jpg_output"

# Convert HEIC files to JPG
#batch_convert_heic_to_jpg(input_folder, output_folder)
print("done")
