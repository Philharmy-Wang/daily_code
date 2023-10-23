import os
import json
from PIL import Image

# Initialize dataset
dataset = {
    "images": [],
    "annotations": [],
    "categories": [
        {"id": 0, "name": "fire"},
        {"id": 1, "name": "smoke"}
    ]
}

annotation_id = 0  # for assigning unique IDs to each annotation
image_id = 0  # for assigning unique IDs to each image

image_folder_path = "VOCdevkit-r/images/train/"
label_folder_path = "VOCdevkit-r/labels/train/"

# Iterate over each image and its corresponding label
for filename in os.listdir(image_folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # add other image formats if necessary
        image_path = os.path.join(image_folder_path, filename)
        label_path = os.path.join(label_folder_path, filename.replace(".jpg", ".txt").replace(".png", ".txt"))
        
        # Add image info
        with Image.open(image_path) as img:
            width, height = img.size
            dataset["images"].append({
                "id": image_id,
                "width": width,
                "height": height,
                "file_name": filename
            })

        # Read YOLO labels and convert to COCO format
        with open(label_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split()
                category_id = int(parts[0])
                x_center, y_center, w, h = map(float, parts[1:])

                # Convert YOLO format (center x, center y, width, height) to COCO format (top left x, top left y, width, height)
                x = (x_center - w / 2) * width
                y = (y_center - h / 2) * height
                w *= width
                h *= height

                dataset["annotations"].append({
                    "id": annotation_id,
                    "image_id": image_id,
                    "category_id": category_id,
                    "bbox": [x, y, w, h],
                    "area": w * h,
                    "iscrowd": 0
                })
                annotation_id += 1

        image_id += 1

# Save to COCO format JSON
with open("train.json", "w") as file:
    json.dump(dataset, file)
