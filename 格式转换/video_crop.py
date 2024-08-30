import cv2

# 打开视频文件
input_video_path = r"H:\数据标注\#1-7) All Video Pairs\#1) RGB Video 1.MP4"
cap = cv2.VideoCapture(input_video_path)
if not cap.isOpened():
    print("Error: Unable to open video file.")
    exit()

# 获取输入视频的帧率和总帧数
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 设置输出视频参数
output_video_path = 'cropped_visible_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (640, 512))

# 逐帧处理视频
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Completed processing all frames.")
        break

    frame_count += 1

    # 显示处理进度
    progress = (frame_count / total_frames) * 100
    print(f"Processing frame {frame_count}/{total_frames} ({progress:.2f}%)")

    # 获取帧尺寸
    original_height, original_width = frame.shape[:2]

    # 计算裁剪位置
    start_x = (original_width - 640) // 2
    start_y = (original_height - 512) // 2

    # 裁剪帧
    cropped_frame = frame[start_y:start_y + 512, start_x:start_x + 640]

    # 写入新视频
    out.write(cropped_frame)

# 清理工作
cap.release()
out.release()
cv2.destroyAllWindows()
