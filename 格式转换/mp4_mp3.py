from pydub import AudioSegment
import os

# 要处理的根目录
root_dir = '/Volumes/老毛桃U盘/爱奇艺/'

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".mp4"):
            # 构建完整的文件路径
            file_path = os.path.join(subdir, file)
            # 加载视频文件
            video = AudioSegment.from_file(file_path, "mp4")
            
            # 创建一个新的子目录来存放音频文件
            audio_subdir = f"{subdir}音频"
            if not os.path.exists(audio_subdir):
                os.makedirs(audio_subdir)
            
            # 构建音频文件的完整路径
            audio_file_path = os.path.join(audio_subdir, os.path.splitext(file)[0] + '.flac')
            # 导出音频
            video.export(audio_file_path, format='flac')
            print(f"Exported {audio_file_path}")
