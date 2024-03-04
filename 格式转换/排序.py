import re
import os

# 转换中文数字到阿拉伯数字
def chinese_to_arabic(cn):
    cn_num = {
        '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
        '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
        '十一': 11, '十二': 12, '十三': 13, '十四': 14, '十五': 15,
        '十六': 16, '十七': 17, '十八': 18, '十九': 19, '二十': 20,
        '二十一': 21, '二十二': 22, '二十三': 23, '二十四': 24, '二十五': 25,
        '二十六': 26, '二十七': 27, '二十八': 28, '二十九': 29, '三十': 30,
    }
    # 直接返回映射中的数字
    return cn_num.get(cn, cn)

# 文件夹路径
folder_path = 'H:/爱奇艺/坑王驾到第4季音频'  # 修改为您的文件夹路径

# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    # 清理文件名中的“-帧绮映画 ”及其后面的内容
    new_name = re.sub(r'-帧绮映画 .*', '', file_name)
    
    # 替换文件名中的中文数字
    new_name = re.sub(r'（[^）]+）', lambda match: str(chinese_to_arabic(match.group()[1:-1])), new_name)
    
    # 获取原始文件的完整路径
    original_file_path = os.path.join(folder_path, file_name)
    
    # 获取新文件名的完整路径
    new_file_path = os.path.join(folder_path, new_name)
    
    # 重命名文件
    if original_file_path != new_file_path:  # 防止重命名为相同的文件名
        os.rename(original_file_path, new_file_path)
        print(f'重命名文件：{file_name} -> {new_name}')

print('所有文件名已更新。')
