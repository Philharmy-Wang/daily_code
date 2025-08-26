# 帮我写个python代码，参考yolov5训练时生成的label.jpg，统计一下数据集。具体如下：
# 1. 数据集为yolov5格式的数据，数据集标注文件的路径为"D:\code\GitHub\datasets\VOCdevkit-r-clean\labels\all_labels"。所有的标注文件都存放在all_labels文件夹下。
# 2. 数据集有两个类别，分别为'fire', 'smoke'。标注文件中的0是fire，1是smoke。
# 3. 读取所有txt文件的所有行的以下数据：
#   a. 第一个数字的数量和分布（标注框的类别数量分布）； 
#   b. 第二个和第三个数字（标注框的中心点坐标分布）；
#   c. 第四个和第五个数字（标注框的宽高相比于整张图片的宽高比例）；
#   d. 带有第一个数字的第二个和第三个数字（标注框的中心点坐标分布）；
#   e. 带有第一个数字的第四个和第五个数字（标注框的宽高相比于整张图片的宽高比例）。
# 4. 将上述五组数据分布写入excel的5个sheet。

import os
import pandas as pd

def parse_label_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        values = [float(v) for v in line.strip().split()]
        if len(values) == 5:
            data.append(values)
    return data

def process_data(data):
    category_count = {0: 0, 1: 0}
    center_points = []
    size_ratios = []
    center_points_with_category = []
    size_ratios_with_category = []

    for entry in data:
        category, x, y, w, h = entry
        category_count[category] += 1
        center_points.append([x, y])
        size_ratios.append([w, h])
        center_points_with_category.append([category, x, y])
        size_ratios_with_category.append([category, w, h])

    return category_count, center_points, size_ratios, center_points_with_category, size_ratios_with_category

# Path to the directory containing label files
label_dir = "D:\code\GitHub\datasets\Yuxi_fire_yolo_pytorch\\all_labels"
all_data = []

# Read all label files
for filename in os.listdir(label_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(label_dir, filename)
        all_data.extend(parse_label_file(file_path))

# Process the data
category_count, center_points, size_ratios, center_points_with_category, size_ratios_with_category = process_data(all_data)

# Convert data to Pandas DataFrames
df_category_count = pd.DataFrame(list(category_count.items()), columns=['Category', 'Count'])
df_center_points = pd.DataFrame(center_points, columns=['Center_X', 'Center_Y'])
df_size_ratios = pd.DataFrame(size_ratios, columns=['Width_Ratio', 'Height_Ratio'])
df_center_points_with_category = pd.DataFrame(center_points_with_category, columns=['Category', 'Center_X', 'Center_Y'])
df_size_ratios_with_category = pd.DataFrame(size_ratios_with_category, columns=['Category', 'Width_Ratio', 'Height_Ratio'])

# Write to Excel
with pd.ExcelWriter('dataset_analysis.xlsx') as writer:
    df_category_count.to_excel(writer, sheet_name='Category Count', index=False)
    df_center_points.to_excel(writer, sheet_name='Center Points', index=False)
    df_size_ratios.to_excel(writer, sheet_name='Size Ratios', index=False)
    df_center_points_with_category.to_excel(writer, sheet_name='Center Points with Category', index=False)
    df_size_ratios_with_category.to_excel(writer, sheet_name='Size Ratios with Category', index=False)
