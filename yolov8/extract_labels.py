import os
import shutil

# 更新后正确的路径
rgb_path = r'E:\Visible and Infrared Images.v1i.yolov8\train\RGB'
ir_path = r'E:\Visible and Infrared Images.v1i.yolov8\train\IR'  # 确保这个路径是正确的
labels_path = r'E:\Visible and Infrared Images.v1i.yolov8\train\labels'
rgb_labels_path = r'E:\Visible and Infrared Images.v1i.yolov8\train\RGB_labels'
ir_labels_path = r'E:\Visible and Infrared Images.v1i.yolov8\train\IR_labels'

# 创建目标文件夹
os.makedirs(rgb_labels_path, exist_ok=True)
os.makedirs(ir_labels_path, exist_ok=True)

# 读取所有RGB和IR图像的文件名，保留整个名称，不包括.jpg后缀
rgb_files = {file.rsplit('.', 1)[0] for file in os.listdir(rgb_path) if file.endswith('.jpg')}
ir_files = {file.rsplit('.', 1)[0] for file in os.listdir(ir_path) if file.endswith('.jpg')}

# 遍历标签文件夹，根据文件名将标签文件复制到对应的新文件夹
for label in os.listdir(labels_path):
    label_base = label.rsplit('.', 1)[0]  # Remove the .jpg extension for comparison
    if label_base in rgb_files:
        shutil.copy(os.path.join(labels_path, label), rgb_labels_path)
    elif label_base in ir_files:
        shutil.copy(os.path.join(labels_path, label), ir_labels_path)
