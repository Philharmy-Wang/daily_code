import os
def check_and_remove_unmatched_files(images_path, labels_path):
    # Iterate over each subfolder ('train' and 'val')
    for subfolder in ['train', 'val']:
        # Create full paths for image and label subfolders
        img_subfolder = os.path.join(images_path, subfolder)
        label_subfolder = os.path.join(labels_path, subfolder)

        # Get the set of image and label filenames without extension
        img_files = {os.path.splitext(f)[0] for f in os.listdir(img_subfolder) if os.path.isfile(os.path.join(img_subfolder, f))}
        label_files = {os.path.splitext(f)[0] for f in os.listdir(label_subfolder) if os.path.isfile(os.path.join(label_subfolder, f))}

        # Find and remove unmatched label files
        unmatched_labels = label_files - img_files
        for label_file in unmatched_labels:
            os.remove(os.path.join(label_subfolder, label_file + '.txt'))
            print(f"Removed label file: {label_file}.txt")

        # Find and report unmatched image files
        unmatched_images = img_files - label_files
        for img_file in unmatched_images:
            print(f"Unmatched image file (no label): {img_file}.jpg or .png")

        # Check for count consistency
        img_count = len(img_files)
        label_count = len(label_files - unmatched_labels)
        if img_count != label_count:
            print(f"Mismatch in counts for {subfolder}: Images = {img_count}, Labels = {label_count}")
        else:
            print(f"{subfolder} folder is consistent: {img_count} images and labels")

# Paths to your images and labels directories
images_path = "D:/code/GitHub/datasets/VOCdevkit-r-clean/images"
labels_path = "D:/code/GitHub/datasets/VOCdevkit-r-clean/labels"

# Call the function
check_and_remove_unmatched_files(images_path, labels_path)
