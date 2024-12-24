import os
import shutil
import random

# 设置随机种子（可选）
random.seed(42)

# 定义源和目标路径
source_images = r'I:\IR+IR_labels\IR\images'
source_labels = r'I:\IR+IR_labels\IR\labels'

train_images_dest = r'I:\IR+IR_labels\images\train'
val_images_dest = r'I:\IR+IR_labels\images\val'

train_labels_dest = r'I:\IR+IR_labels\labels\train'
val_labels_dest = r'I:\IR+IR_labels\labels\val'

# 创建目标文件夹，如果不存在则创建
os.makedirs(train_images_dest, exist_ok=True)
os.makedirs(val_images_dest, exist_ok=True)
os.makedirs(train_labels_dest, exist_ok=True)
os.makedirs(val_labels_dest, exist_ok=True)

# 获取所有图片文件列表
all_images = [f for f in os.listdir(source_images) if f.lower().endswith('.jpg')]

# 打乱并划分数据集
random.shuffle(all_images)
num_train = int(len(all_images) * 0.8)
train_images = all_images[:num_train]
val_images = all_images[num_train:]

# 复制训练集图片和标签
for img_name in train_images:
    img_src = os.path.join(source_images, img_name)
    img_dst = os.path.join(train_images_dest, img_name)
    shutil.copyfile(img_src, img_dst)

    label_name = os.path.splitext(img_name)[0] + '.txt'
    label_src = os.path.join(source_labels, label_name)
    label_dst = os.path.join(train_labels_dest, label_name)
    if os.path.exists(label_src):
        shutil.copyfile(label_src, label_dst)
    else:
        print(f"警告：标签文件 {label_name} 不存在。")

# 复制验证集图片和标签
for img_name in val_images:
    img_src = os.path.join(source_images, img_name)
    img_dst = os.path.join(val_images_dest, img_name)
    shutil.copyfile(img_src, img_dst)

    label_name = os.path.splitext(img_name)[0] + '.txt'
    label_src = os.path.join(source_labels, label_name)
    label_dst = os.path.join(val_labels_dest, label_name)
    if os.path.exists(label_src):
        shutil.copyfile(label_src, label_dst)
    else:
        print(f"警告：标签文件 {label_name} 不存在。")
