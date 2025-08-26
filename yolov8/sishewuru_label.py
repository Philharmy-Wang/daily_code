import os

def round_coordinates(input_path, output_path):
    # 确保输出目录存在
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for file_name in os.listdir(input_path):
        if file_name.endswith(".txt"):
            input_file = os.path.join(input_path, file_name)
            output_file = os.path.join(output_path, file_name)

            with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
                for line in infile:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        class_index = parts[0]
                        coords = [round(float(coord), 3) for coord in parts[1:]]
                        outfile.write(f"{class_index} {' '.join(map(str, coords))}\n")
                    else:
                        print(f"Skipping invalid line in {input_file}: {line}")

# 定义文件路径
train_input_path = r"E:\FLAME2_dt\RGB_IR_fuse_labels\RGB_IR_fuse_labels\labels\train"
train_output_path = r"E:\FLAME2_dt\RGB_IR_fuse_labels\RGB_IR_fuse_labels\label\train"
val_input_path = r"E:\FLAME2_dt\RGB_IR_fuse_labels\RGB_IR_fuse_labels\labels\val"
val_output_path = r"E:\FLAME2_dt\RGB_IR_fuse_labels\RGB_IR_fuse_labels\label\val"

# 处理train和val目录中的文件
round_coordinates(train_input_path, train_output_path)
round_coordinates(val_input_path, val_output_path)

print("完成坐标四舍五入并保存到新文件。")
