import cv2
import os

frames_dir = r"D:\OneDrive - Benha University (Faculty Of Computers & Information Technolgy)\Desktop\The Sharp-Shot Video Filter\video_1"
output_video = r"D:\OneDrive - Benha University (Faculty Of Computers & Information Technolgy)\Desktop\The Sharp-Shot Video Filter\input_video.mp4"

fps = 30  # عدد الفريمات في الثانية

images = sorted(os.listdir(frames_dir))

# اقرأ أول صورة عشان تعرف الحجم
first_frame = cv2.imread(os.path.join(frames_dir, images[0]))
height, width, _ = first_frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

for img_name in images:
    img_path = os.path.join(frames_dir, img_name)
    frame = cv2.imread(img_path)
    if frame is None:
        continue
    video.write(frame)

video.release()
print("✅ Video created successfully.")
