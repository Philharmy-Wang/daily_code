import os

# 定义文件夹路径
base_folder = r'E:\Visible and Infrared Images.v1i.yolov8\train'
ir_labels_folder = os.path.join(base_folder, 'IR_labels')
rgb_labels_folder = os.path.join(base_folder, 'RGB_labels')
merged_labels_folder = os.path.join(base_folder, 'hebing_labels')

# 创建输出目录
if not os.path.exists(merged_labels_folder):
    os.makedirs(merged_labels_folder)
    print(f"Created directory: {merged_labels_folder}")

# 获取所有IR和RGB的标注文件名
ir_files = os.listdir(ir_labels_folder)
rgb_files = os.listdir(rgb_labels_folder)

# 合并文件
for ir_file in ir_files:
    if ir_file in rgb_files:  # 确保RGB目录中有对应的文件
        # 读取IR和RGB文件内容
        with open(os.path.join(ir_labels_folder, ir_file), 'r') as file:
            ir_data = file.readlines()
        with open(os.path.join(rgb_labels_folder, ir_file), 'r') as file:
            rgb_data = file.readlines()
        
        # 删除空白行
        ir_data = [line for line in ir_data if line.strip()]
        rgb_data = [line for line in rgb_data if line.strip()]
        
        # 合并内容
        merged_data = ir_data + rgb_data
        
        # 删除合并后多余的空白行
        merged_data = [line for line in merged_data if line.strip()]
        
        # 写入合并后的文件
        with open(os.path.join(merged_labels_folder, ir_file), 'w') as file:
            file.writelines(merged_data)
        print(f"Merged file written: {ir_file}")

print("All eligible files have been merged and written.")
