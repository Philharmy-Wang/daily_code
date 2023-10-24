import os
import json
from PIL import Image

def convert_yolo_to_coco(yolo_label_dir, image_dir, output_path):
    coco_output = {
        "images": [],
        "annotations": [],
        "categories": [
            {"id": 0, "name": "fire"},
            {"id": 1, "name": "smoke"}
        ]
    }

    image_id = 0
    annotation_id = 0

    for root, dirs, files in os.walk(yolo_label_dir):
        for file in files:
            if file.endswith('.txt'):
                image_file = file.replace('.txt', '.jpg')  # Assuming images are in jpg format
                image_path = os.path.join(image_dir, image_file)
                image = Image.open(image_path)
                width, height = image.size

                coco_output["images"].append({
                    "file_name": image_file,
                    "height": height,
                    "width": width,
                    "id": image_id
                })

                with open(os.path.join(root, file), 'r') as label_file:
                    lines = label_file.readlines()
                    for line in lines:
                        class_id, x_center, y_center, box_width, box_height = map(float, line.strip().split())
                        x_min = (x_center - box_width / 2) * width
                        y_min = (y_center - box_height / 2) * height
                        b_width = box_width * width
                        b_height = box_height * height

                        coco_output["annotations"].append({
                            "id": annotation_id,
                            "image_id": image_id,
                            "category_id": int(class_id),
                            "bbox": [x_min, y_min, b_width, b_height],
                            "area": b_width * b_height,
                            "iscrowd": 0,
                            "segmentation": []  # This script does not support segmentation
                        })
                        annotation_id += 1

                image_id += 1

    with open(output_path, 'w') as output_file:
        json.dump(coco_output, output_file)

if __name__ == '__main__':
    train_yolo_label_dir = r'C:\Users\12715\Documents\GitHub\mmdetection\dataset\VOCdevkit-rs\labels\train'
    train_image_dir = r'C:\Users\12715\Documents\GitHub\mmdetection\dataset\VOCdevkit-rs\images\train'
    val_yolo_label_dir = r'C:\Users\12715\Documents\GitHub\mmdetection\dataset\VOCdevkit-rs\labels\val'
    val_image_dir = r'C:\Users\12715\Documents\GitHub\mmdetection\dataset\VOCdevkit-rs\images\val'

    convert_yolo_to_coco(train_yolo_label_dir, train_image_dir, 'train_coco.json')
    convert_yolo_to_coco(val_yolo_label_dir, val_image_dir, 'val_coco.json')
