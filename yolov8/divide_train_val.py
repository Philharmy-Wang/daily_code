import os
import shutil
import random

# 设置种子以确保可重复性
random.seed(42)

# 源文件夹路径
# rgb_images_src = r'E:\FLAME2_dt_rgb_ir_origin_data\RGB\images'
# ir_images_src = r'E:\FLAME2_dt_rgb_ir_origin_data\IR\images'
# labels_src = r'E:\FLAME2_dt_rgb_ir_origin_data\labels'

rgb_images_src = r'E:\FLAME2_dt\RGB+RGB_IR_labels\RGB+RGB_IR_labels\images'
# ir_images_src = r'E:\FLAME2_dt_rgb_ir_origin_data\IR\images'
labels_src = r'E:\FLAME2_dt\RGB+RGB_IR_labels\RGB+RGB_IR_labels\labels'

# 目标文件夹路径
train_rgb_dest = r'E:\FLAME2_dt\RGB+RGB_IR_labels\images\train'
val_rgb_dest = r'E:\FLAME2_dt\RGB+RGB_IR_labels\images\val'
# train_ir_dest = r'E:\FLAME2_dt\image\train'
# val_ir_dest = r'E:\FLAME2_dt\image\val'
train_labels_dest = r'E:\FLAME2_dt\RGB+RGB_IR_labels\labels\train'
val_labels_dest = r'E:\FLAME2_dt\RGB+RGB_IR_labels\labels\val'

# 创建所需的目录
for path in [train_rgb_dest, val_rgb_dest, train_labels_dest, val_labels_dest]:
    os.makedirs(path, exist_ok=True)

# 获取所有RGB图像的文件名
rgb_images = [f for f in os.listdir(rgb_images_src) if f.endswith('.jpg')]
random.shuffle(rgb_images)

# 计算80%的训练集大小
split_index = int(0.8 * len(rgb_images))
train_rgb_files = rgb_images[:split_index]
val_rgb_files = rgb_images[split_index:]

# 复制文件到新位置
def copy_files(files, src, dest):
    for file in files:
        shutil.copy2(os.path.join(src, file), os.path.join(dest, file))

# 复制RGB图像到训练集和验证集
copy_files(train_rgb_files, rgb_images_src, train_rgb_dest)
copy_files(val_rgb_files, rgb_images_src, val_rgb_dest)

# 复制对应的IR图像到训练集和验证集
# copy_files(train_rgb_files, ir_images_src, train_ir_dest)
# copy_files(val_rgb_files, ir_images_src, val_ir_dest)

# 复制对应的标签文件到训练集和验证集
copy_files([f.replace('.jpg', '.txt') for f in train_rgb_files], labels_src, train_labels_dest)
copy_files([f.replace('.jpg', '.txt') for f in val_rgb_files], labels_src, val_labels_dest)

print("文件处理完成。")