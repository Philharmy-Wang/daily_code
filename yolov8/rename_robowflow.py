import os

# 指定文件夹路径
folder_path = r'I:\FLAME2_dt_rgb_ir\RGB\labels\5_rgb'

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 遍历所有文件
for file_name in files:
    # 检查文件名是否符合指定格式
    if file_name.startswith('5_frame') and file_name.endswith('.txt'):
        # 提取新的文件名
        new_name = file_name.split('_jpg')[0] + '.txt'
        
        # 构造完整的旧文件路径和新文件路径
        old_file = os.path.join(folder_path, file_name)
        new_file = os.path.join(folder_path, new_name)
        
        # 重命名文件
        os.rename(old_file, new_file)
        print(f'Renamed: {old_file} to {new_file}')

print("文件重命名完成。")
