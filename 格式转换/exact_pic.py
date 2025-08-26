import os
import shutil

# 输入和输出文件夹的路径
rgb_src_folder = r"H:\FLAME2\#9) 254p Frame Pairs\254p RGB Images"
ir_src_folder = r"H:\FLAME2\#9) 254p Frame Pairs\254p Thermal Images"
rgb_dst_folder = r"H:\dataset\rgb"
ir_dst_folder = r"H:\dataset\ir"

# 确保输出文件夹存在
os.makedirs(rgb_dst_folder, exist_ok=True)
os.makedirs(ir_dst_folder, exist_ok=True)

# 提取间隔和起始编号
frame_interval = 30
start_number = 1

# 提取并重新编号图像
new_rgb_number = start_number
new_ir_number = start_number

# 总图片数量
total_images = 53451
for i in range(1, total_images + 1, frame_interval):
    # 构建源文件名
    rgb_src_filename = f"254p RGB Frame ({i}).jpg"
    ir_src_filename = f"254p Thermal Frame ({i}).jpg"

    # 构建目标文件名
    rgb_dst_filename = f"rgb{new_rgb_number}.jpg"
    ir_dst_filename = f"ir{new_ir_number}.jpg"
    
    # 完整的源文件和目标文件路径
    rgb_src_path = os.path.join(rgb_src_folder, rgb_src_filename)
    ir_src_path = os.path.join(ir_src_folder, ir_src_filename)
    rgb_dst_path = os.path.join(rgb_dst_folder, rgb_dst_filename)
    ir_dst_path = os.path.join(ir_dst_folder, ir_dst_filename)
    
    # 如果源文件存在，则复制并重新编号
    if os.path.isfile(rgb_src_path):
        shutil.copy(rgb_src_path, rgb_dst_path)
        new_rgb_number += 1
    if os.path.isfile(ir_src_path):
        shutil.copy(ir_src_path, ir_dst_path)
        new_ir_number += 1

print("Finished extracting and renumbering images.")
