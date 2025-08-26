import cv2
import os

# 指定原始RGB图像和目标文件夹的路径
rgb_src_folder = r"H:\dataset\images\7_rgb"
rgb_dst_folder = r"H:\dataset\images\7_rgb_cropped"

# 创建目标文件夹，如果不存在
if not os.path.exists(rgb_dst_folder):
    os.makedirs(rgb_dst_folder)

# 缩放后的尺寸和裁剪像素
scale_size = (919, 524)
crop_top = 9
crop_bottom = 3
crop_left = 152
crop_right = 127

# 遍历文件夹中的所有图像文件
for file_name in os.listdir(rgb_src_folder):
    # 构建完整的文件路径
    file_path = os.path.join(rgb_src_folder, file_name)

    # 读取图像
    image = cv2.imread(file_path)
    if image is None:
        print(f"Could not read image {file_name}")
        continue

    # 首先缩放图像
    scaled_image = cv2.resize(image, scale_size, interpolation=cv2.INTER_AREA)

    # 然后裁剪图像
    cropped_image = scaled_image[crop_top:-crop_bottom, crop_left:-crop_right]

    # 构建裁剪后图像的完整保存路径
    dst_file_path = os.path.join(rgb_dst_folder, file_name)

    # 保存裁剪后的图像
    cv2.imwrite(dst_file_path, cropped_image)
    print(f"Cropped image saved as {dst_file_path}")

print("Finished processing all images.")
