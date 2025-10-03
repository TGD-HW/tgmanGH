import os
import shutil

def rename_and_copy_images(root_dir):
    # First pass: Rename images
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if 'schematic' in filename and filename.endswith('.webp'):
                # Form new name
                new_name = 'schematic.webp'
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, new_name)

                # Rename the image if it exists
                if not os.path.exists(new_path):
                    os.rename(old_path, new_path)
                    print(f'Renamed: {old_path} to {new_path}')

    # Second pass: Create copy with new name format
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'schematic.webp':
                original_path = os.path.join(dirpath, filename)
                copy_name = filename.replace('schematic.webp', 'schematic.en.webp')
                copy_path = os.path.join(dirpath, copy_name)

                # Copy the file
                if not os.path.exists(copy_path):
                    shutil.copyfile(original_path, copy_path)
                    print(f'Copied: {original_path} to {copy_path}')

if __name__ == '__main__':
    root_folder = os.path.dirname(os.path.abspath(__file__))  # Folder where the script resides
    rename_and_copy_images(root_folder)
