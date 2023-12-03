import os

def remove_real_duplicates(real_path, rsy_path):
    # Iterate over each type ('images', 'labels') and each subfolder ('train', 'val')
    for folder_type in ['images', 'labels']:
        for subfolder in ['train', 'val']:
            # Create full paths for real and rsy subfolders
            real_subfolder = os.path.join(real_path, folder_type, subfolder)
            rsy_subfolder = os.path.join(rsy_path, folder_type, subfolder)

            # List all files in the real and rsy subfolders
            real_files = set(os.listdir(real_subfolder))
            rsy_files = set(os.listdir(rsy_subfolder))

            # Find the intersection of files (duplicates)
            duplicates = real_files & rsy_files

            # Remove the duplicate files from the rsy subfolder
            for file in duplicates:
                file_path = os.path.join(rsy_subfolder, file)
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Removed {file} from {rsy_subfolder}")

# Paths to the real and rsy datasets
real_path = "D:/code/GitHub/datasets/VOCdevkit-r"
rsy_path = "D:/code/GitHub/datasets/VOCdevkit-rsy-clean"

# Call the function
remove_real_duplicates(real_path, rsy_path)
