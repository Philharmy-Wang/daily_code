import os
import pandas as pd
from tqdm import tqdm

# 设置路径
labels_dir = r"H:\FLAME2_dt\RGB_IR_fuse_labels\RGB_IR_fuse_labels\labels\val"
output_excel = r"H:\FLAME2_dt\RGB_IR_fuse_labels\RGB_IR_fuse_labels\RGB_IR_fuse_labels_val_statistics.xlsx"

# 初始化统计信息
fire_count = 0
smoke_count = 0

# 用于宽高和中心点分布统计
fire_bbox = []
smoke_bbox = []
fire_centers = []
smoke_centers = []

# 遍历标注文件
for label_file in tqdm(os.listdir(labels_dir)):
    if label_file.endswith(".txt"):
        file_path = os.path.join(labels_dir, label_file)
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                elements = line.strip().split()
                class_label = int(elements[0])
                x_center = float(elements[1])
                y_center = float(elements[2])
                width = float(elements[3])
                height = float(elements[4])

                # 根据类别进行统计
                if class_label == 0:  # fire
                    fire_count += 1
                    fire_bbox.append((width, height))
                    fire_centers.append((x_center, y_center))
                elif class_label == 1:  # smoke
                    smoke_count += 1
                    smoke_bbox.append((width, height))
                    smoke_centers.append((x_center, y_center))

# 生成统计数据
summary_df = pd.DataFrame({
    "Category": ["fire", "smoke"],
    "Count": [fire_count, smoke_count]
})

fire_bbox_df = pd.DataFrame(fire_bbox, columns=["Width", "Height"])
smoke_bbox_df = pd.DataFrame(smoke_bbox, columns=["Width", "Height"])
fire_centers_df = pd.DataFrame(fire_centers, columns=["X_center", "Y_center"])
smoke_centers_df = pd.DataFrame(smoke_centers, columns=["X_center", "Y_center"])

# 写入Excel
with pd.ExcelWriter(output_excel) as writer:
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
    fire_bbox_df.to_excel(writer, sheet_name="Fire_BBox", index=False)
    smoke_bbox_df.to_excel(writer, sheet_name="Smoke_BBox", index=False)
    fire_centers_df.to_excel(writer, sheet_name="Fire_Centers", index=False)
    smoke_centers_df.to_excel(writer, sheet_name="Smoke_Centers", index=False)

print(f"统计完成，结果已保存到 {output_excel}")
