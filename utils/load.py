import cv2
import numpy as np

from .image import show


def load(image: np.ndarray,
         doctor: np.ndarray,
         delay: bool = True) -> np.ndarray:
    height, width, _ = image.shape
    rows, cols, _ = doctor.shape

    ratio = height / rows
    small = cv2.resize(doctor, (0, 0), None, ratio, ratio)
    r, c, _ = small.shape

    canvas = np.ones((height, width + c, 3), dtype=np.uint8)
    for i in range(3):
        canvas[:, :, i] = 255
    for i in range(c):
        for j in range(r):
            for k in range(3):
                canvas[j, i][k] = small[j, i][k]
    for i in range(width):
        for j in range(height):
            for k in range(3):
                canvas[j, i + c][k] = image[j, i][k]
        if delay and i % 10 == 0:
            show(canvas, 0.001)
    return canvas
