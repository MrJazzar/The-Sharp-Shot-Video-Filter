import cv2
import os
import numpy as np

# --------- Sharpness Functions ----------

def laplacian_variance(image):
    """
    Measures sharpness using Laplacian variance.
    Higher variance indicates a sharper image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()


def tenengrad(image):
    """
    Measures sharpness using the Tenengrad method
    based on Sobel gradients.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    return np.mean(gx**2 + gy**2)


# --------- Paths ----------
video_path = r"D:\OneDrive - Benha University (Faculty Of Computers & Information Technolgy)\Desktop\The Sharp-Shot Video Filter\input_video.mp4"
output_dir = r"D:\OneDrive - Benha University (Faculty Of Computers & Information Technolgy)\Desktop\The Sharp-Shot Video Filter\sharp_frames"
os.makedirs(output_dir, exist_ok=True)

# --------- Video Capture ----------
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

frame_id = 0
frames_data = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # --------- Combined Sharpness Score ----------
    sharpness = (
        0.6 * tenengrad(frame) +
        0.4 * laplacian_variance(frame)
    )

    time_sec = frame_id / fps

    frames_data.append({
        "frame": frame,
        "sharpness": sharpness,
        "time": time_sec
    })

    frame_id += 1

cap.release()

# --------- Sort Frames by Sharpness ----------
frames_data.sort(key=lambda x: x["sharpness"], reverse=True)

# --------- Select Top 5 Frames from Different Seconds ----------
selected_frames = []
used_seconds = set()

for data in frames_data:
    sec = int(data["time"])
    if sec not in used_seconds:
        selected_frames.append(data)
        used_seconds.add(sec)

    if len(selected_frames) == 5:
        break

# --------- Save Frames ----------
for i, data in enumerate(selected_frames):
    out_path = os.path.join(output_dir, f"sharp_{i+1}.png")
    cv2.imwrite(out_path, data["frame"])

print("✅ Top 5 sharp frames saved successfully.")
