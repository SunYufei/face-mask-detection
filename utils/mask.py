import cv2
import numpy as np

from .image import show


def show_mask(image: np.ndarray,
              mask: np.ndarray,
              landmarks: list,
              spec: bool = False) -> None:
    if spec:
        x = landmarks[0][0]
        y = min(landmarks[19][1], landmarks[24][1])
        w = landmarks[16][0] - x
        h = landmarks[33][1] - y
    else:
        x = landmarks[2][0]
        y = landmarks[29][1]
        w = landmarks[13][0] - x
        h = landmarks[8][1] - y

    rows, cols, _ = mask.shape

    r_ratio = h / rows * 2
    c_ratio = w / cols * 1.6
    small = cv2.resize(mask, (0, 0), None, c_ratio, r_ratio)
    r, c, _ = small.shape

    sx = x + (w - c) // 2
    sy = y + (h - r) // 2

    for j in range(r):
        for i in range(c):
            if small[j, i][3]:
                for k in range(3):
                    image[sy + j, sx + i][k] = small[j, i][k]
        show(image, 0.02)
    show(image, 1)
