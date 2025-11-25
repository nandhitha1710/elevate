import os
from PIL import Image

# Input & Output folders
input_folder = "images"
output_folder = "output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Desired size (Width, Height)
new_size = (400, 400)

# Desired format (optional): "JPEG", "PNG", etc.
output_format = "JPEG"

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith((".jpg", ".jpeg", ".png")):

        img_path = os.path.join(input_folder, file_name)
        img = Image.open(img_path)

        # Resize
        resized_img = img.resize(new_size)

        # Create new file name
        base_name = os.path.splitext(file_name)[0]
        new_file = f"{base_name}_resized.jpg"

        # Save resized image
        resized_img.save(os.path.join(output_folder, new_file), output_format)

        print(f"Resized & saved: {new_file}")

print("✔ All images processed successfully!")
