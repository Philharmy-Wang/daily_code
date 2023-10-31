from rembg import remove
from PIL import Image
import numpy as np

def change_background_to_blue(input_path, output_path):
    # 读取图像
    input_image = Image.open(input_path)
    
    # 将图像大小调整为480x640像素
    resized_image = input_image.resize((480, 640))

    # 使用rembg去除背景
    output_data = remove(np.array(resized_image))
    no_bg_image = Image.open(io.BytesIO(output_data))

    # 创建蓝色背景图像
    blue_background = Image.new('RGBA', (480, 640), (0, 0, 255, 255))
    
    # 将无背景图像与蓝色背景合并
    final_image = Image.alpha_composite(blue_background, no_bg_image.convert('RGBA'))
    
    # 保存结果图像
    final_image.save(output_path)

# # 使用函数
# change_background_to_blue('/path/to/your/input.jpg', '/path/to/your/output.png')


# 使用函数
change_background_to_blue('/home/gb/下载/photo.jpeg', '/home/gb/下载/output.jpg')
