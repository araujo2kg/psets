import os
import re

# Function to find all images referenced in HTML files
def find_images_in_html(html_folder):
    img_files = set()
    img_pattern = re.compile(r'<img\s+[^>]*src="([^"]+)"', re.IGNORECASE)

    for root, _, files in os.walk(html_folder):
        for file in files:
            if file.endswith('.html') or file.endswith('.htm'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = img_pattern.findall(content)
                    for match in matches:
                        img_files.add(os.path.basename(match))
    return img_files

# Function to list all images in the project folder
def list_all_images(image_folder):
    img_files = set()
    for root, _, files in os.walk(image_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.avif')):
                img_files.add(file)
    return img_files

# Paths to your HTML files and image folder
html_folder = '.'
image_folder = './images'

# Find images in HTML files and all images in the project folder
used_images = find_images_in_html(html_folder)
all_images = list_all_images(image_folder)

# Identify unused images
unused_images = all_images - used_images

# Print the list of unused images
print("Unused images:")
for img in unused_images:
    print(img)

# Remove the unused images
for img in unused_images:
     os.remove(os.path.join(image_folder, img))
