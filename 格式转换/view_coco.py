import json
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# 载入COCO标注文件
coco_anno = json.load(open('/home/a1408/wgb/PaddleDetection/dataset/coco/annotations/instances_train2017.json'))

# 创建类别名到颜色的映射
category_info = {
    'fire': {'color': 'red', 'id': 1},
    'smoke': {'color': 'blue', 'id': 2}
}

# 创建类别ID到类别信息的映射
category_id_to_info = {category['id']: {'color': category_info[category['name']]['color'], 'name': category['name']} 
                       for category in coco_anno['categories'] if category['name'] in category_info}

# 创建图像ID到标注的映射
img_id_to_annos = {}
for anno in coco_anno['annotations']:
    img_id = anno['image_id']
    if img_id not in img_id_to_annos:
        img_id_to_annos[img_id] = []
    img_id_to_annos[img_id].append(anno)

# 随机选择30张图像
selected_images = random.sample(coco_anno['images'], 30)

# 准备绘制图像，创建5行6列的子图布局
fig, axs = plt.subplots(5, 6, figsize=(24, 20))  # Adjust the size as needed
axs = axs.flatten()  # Flatten the array for easy iteration

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
            category_id = anno['category_id']
            # 获取该类别的颜色和名称
            category_info = category_id_to_info[category_id]
            color = category_info['color']
            name = category_info['name']
            # 绘制边界框和标签
            rect = patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], linewidth=2, edgecolor=color, facecolor='none')
            ax.add_patch(rect)
            ax.text(bbox[0], bbox[1], name, color=color, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

    ax.axis('off')

plt.tight_layout()
plt.show()
