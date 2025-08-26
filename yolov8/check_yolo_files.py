import os

def check_yolo_files(input_path):
    invalid_files = []

    for file_name in os.listdir(input_path):
        if file_name.endswith(".txt"):
            input_file = os.path.join(input_path, file_name)
            with open(input_file, 'r') as infile:
                for line_number, line in enumerate(infile, 1):
                    parts = line.strip().split()
                    if len(parts) != 5:
                        invalid_files.append((input_file, line_number, line.strip()))
    
    return invalid_files

# 定义文件路径
train_input_path = r"E:\Visible and Infrared Images.v1i.yolov8\train\hebing_labels"
val_input_path = r"E:\Visible and Infrared Images.v1i.yolov8\train\hebing_labels"

# 检查train和val目录中的文件
train_invalid_files = check_yolo_files(train_input_path)
val_invalid_files = check_yolo_files(val_input_path)

# 输出有问题的文件和行
if train_invalid_files or val_invalid_files:
    print("发现格式错误的文件和行：")
    for file, line_number, line in train_invalid_files + val_invalid_files:
        print(f"文件: {file}, 行号: {line_number}, 内容: '{line}'")
else:
    print("所有文件格式正确。")
