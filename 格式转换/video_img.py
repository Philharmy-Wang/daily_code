import cv2
import os

def extract_frames(video_path, base_output_folder, frames_per_second=1):
    # 获取视频文件名（不包括扩展名）
    video_filename = os.path.splitext(os.path.basename(video_path))[0]

    # 创建每个视频文件专用的输出文件夹
    output_folder = os.path.join(base_output_folder, video_filename)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created directory: {output_folder}")

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    # 获取视频的帧率和总帧数
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Video FPS: {fps}, Total Frames: {total_frames}")

    # 计算抽取帧的间隔
    interval = int(fps / frames_per_second)
    print(f"Frame interval: {interval}")

    # 初始化帧计数器和保存的帧数
    frame_count = 0
    saved_frame_count = 0

    # 逐帧读取视频
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 如果当前帧数是间隔的倍数，则保存该帧
        if frame_count % interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")
            success = cv2.imwrite(frame_filename, frame)
            if success:
                saved_frame_count += 1
                print(f"Saved: {frame_filename}")
            else:
                print(f"Failed to save: {frame_filename}")

        frame_count += 1

    # 清理工作
    cap.release()
    print(f"Done extracting frames for {video_filename}. Total saved frames: {saved_frame_count}")

# 视频文件路径和基础输出目录
video_path = r"H:\dataset\video\5_ir.MP4"  # 更改为你的视频文件路径
base_output_folder = r"H:\dataset\images"  # 更改为你希望保存帧的基础目录

# 调用函数
extract_frames(video_path, base_output_folder)
