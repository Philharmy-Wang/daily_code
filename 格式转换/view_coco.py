# 可视化查看转换后的coco数据集的标注是否准确

import json
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# 加载COCO标注文件
coco_anno = json.load(open('/home/a1408/wgb/PaddleDetection/dataset/coco/annotations/instances_train2017.json'))

# 创建图像ID到标注的映射
img_id_to_annos = {}
for anno in coco_anno['annotations']:
    img_id = anno['image_id']
    if img_id not in img_id_to_annos:
        img_id_to_annos[img_id] = []
    img_id_to_annos[img_id].append(anno)

# 随机选择10张图像
selected_images = random.sample(coco_anno['images'], 10)

# 准备绘制图像
fig, axs = plt.subplots(2, 5, figsize=(20, 8))
axs = axs.flatten()

for img_info, ax in zip(selected_images, axs):
    img_id = img_info['id']
    img_path = f"/home/a1408/wgb/PaddleDetection/dataset/coco/train2017/{img_info['file_name']}"
    img = Image.open(img_path)

    # 绘制图像
    ax.imshow(img)

    # 绘制所有该图像的标注
    if img_id in img_id_to_annos:
        for anno in img_id_to_annos[img_id]:
            # COCO的bbox格式：[x, y, width, height]
            bbox = anno['bbox']
            rect = patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

    ax.axis('off')

plt.tight_layout()
plt.show()
