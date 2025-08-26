# import os

# # 定义文件夹路径
# ir_images_folder = r'I:\FLAME2_dt_rgb_ir\IR\images'
# ir_labels_folder = r'I:\FLAME2_dt_rgb_ir\IR\labels'
# rgb_images_folder = r'I:\FLAME2_dt_rgb_ir\RGB\images'
# rgb_labels_folder = r'I:\FLAME2_dt_rgb_ir\RGB\labels'

# # 获取IR文件的基础名称（不含后缀）
# ir_image_files = {os.path.splitext(f)[0] for f in os.listdir(ir_images_folder) if f.endswith('.jpg')}
# ir_label_files = {os.path.splitext(f)[0] for f in os.listdir(ir_labels_folder) if f.endswith('.txt')}

# # 获取RGB文件的完整路径
# rgb_image_files = [os.path.join(rgb_images_folder, f) for f in os.listdir(rgb_images_folder) if f.endswith('.jpg')]
# rgb_label_files = [os.path.join(rgb_labels_folder, f) for f in os.listdir(rgb_labels_folder) if f.endswith('.txt')]

# # 删除多余的RGB图像文件
# for rgb_image_file in rgb_image_files:
#     base_name = os.path.splitext(os.path.basename(rgb_image_file))[0]
#     if base_name not in ir_image_files:
#         os.remove(rgb_image_file)
#         print(f'Deleted RGB image: {rgb_image_file}')

# # 删除多余的RGB标注文件
# for rgb_label_file in rgb_label_files:
#     base_name = os.path.splitext(os.path.basename(rgb_label_file))[0]
#     if base_name not in ir_label_files:
#         os.remove(rgb_label_file)
#         print(f'Deleted RGB label: {rgb_label_file}')

# print("同步完成。")
import os

# 定义文件夹路径
ir_images_folder = r'I:\FLAME2_dt_rgb_ir\IR\images'
ir_labels_folder = r'I:\FLAME2_dt_rgb_ir\IR\labels'
rgb_images_folder = r'I:\FLAME2_dt_rgb_ir\RGB\images'
rgb_labels_folder = r'I:\FLAME2_dt_rgb_ir\RGB\labels'

# 获取IR文件的基础名称（不含后缀）
ir_image_files = {os.path.splitext(f)[0] for f in os.listdir(ir_images_folder) if f.endswith('.jpg')}
ir_label_files = {os.path.splitext(f)[0] for f in os.listdir(ir_labels_folder) if f.endswith('.txt')}

# 获取RGB文件的基础名称（不含后缀）
rgb_image_files = {os.path.splitext(f)[0] for f in os.listdir(rgb_images_folder) if f.endswith('.jpg')}
rgb_label_files = {os.path.splitext(f)[0] for f in os.listdir(rgb_labels_folder) if f.endswith('.txt')}

# 找出IR目录中存在但RGB目录中不存在的文件
extra_ir_images = ir_image_files - rgb_image_files
extra_ir_labels = ir_label_files - rgb_label_files

print("IR图像目录中存在但RGB图像目录中不存在的文件:")
for file in extra_ir_images:
    print(file + '.jpg')

print("\nIR标注目录中存在但RGB标注目录中不存在的文件:")
for file in extra_ir_labels:
    print(file + '.txt')

# 如果需要同步RGB目录，可以输出建议操作
if extra_ir_images or extra_ir_labels:
    print("\n建议：")
    if extra_ir_images:
        print("在IR图像目录中删除这些文件，以保持与RGB图像目录同步：")
        for file in extra_ir_images:
            print(file + '.jpg')

    if extra_ir_labels:
        print("在IR标注目录中删除这些文件，以保持与RGB标注目录同步：")
        for file in extra_ir_labels:
            print(file + '.txt')
else:
    print("IR和RGB目录中的文件完全一致。")
