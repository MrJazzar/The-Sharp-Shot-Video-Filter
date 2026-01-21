# Sharp Frame Extraction from Video

## Overview
This project extracts the top 5 sharpest frames from a video using
image sharpness evaluation techniques based on edge detection.
The solution ensures both visual quality and temporal diversity.

---

## Libraries Used
- OpenCV (cv2)
- NumPy
- OS (file handling)

---

## How the Algorithm Works
1. Read the video frame by frame.
2. Convert each frame to grayscale.
3. Compute sharpness scores using Laplacian Variance and Tenengrad methods.
4. Combine both scores into a single sharpness value.
5. Sort frames by sharpness.
6. Select the top 5 sharpest frames from different time seconds.
7. Save the selected frames as images.

---

## 2️⃣ Mathematical Method Explanation (Sharpness)

### 🔹 Laplacian Variance

The Laplacian operator highlights regions of rapid intensity change (edges).
After converting the frame to grayscale, the Laplacian is applied, and the
variance of the result is computed.

- **High variance** → many strong edges → sharp image  
- **Low variance** → few edges → blurry image  

Mathematically:

\[
Sharpness = Var(Laplacian(I))

\]

Where:
- \(Laplacian(I)) is the Laplacian of the image
- \( Var \) denotes variance

---

### 🔹 Tenengrad Method

The Tenengrad method uses Sobel gradients in the horizontal and vertical
directions. It measures the strength of edges by computing the squared
gradient magnitude.

\[
Sharpness = \frac{1}{N} \sum (G_x^2 + G_y^2)
\]

Where:
- \( G_x \) and \( G_y \) are Sobel gradients in x and y directions
- \( N \) is the number of pixels

Higher values indicate sharper images.

---

### 🔹 Combined Sharpness Score

To improve robustness, both methods are combined into a single score:

\[
Final\ Sharpness = 0.6 \times Tenengrad + 0.4 \times LaplacianVariance
\]

This combination balances strong edge detection with overall image detail,
making the sharpness estimation more reliable.

---

## 3️⃣ Ensuring Frames Are Not from the Same Second

To avoid selecting multiple frames from the exact same second, each frame’s
timestamp is calculated using:

\[
Time = FrameID / FPS
\]

During frame selection:
- Frames are grouped by **integer second**
- Only **one frame per second** is allowed
- A set (`used_seconds`) prevents duplicate time selection

This guarantees **temporal diversity**, ensuring the selected frames represent
different moments in the video.

---

## How to Run
1. Install dependencies:
   ```bash
   pip install opencv-python numpy
