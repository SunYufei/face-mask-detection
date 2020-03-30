import cv2
import numpy as np


def show(mat: np.ndarray, delay: float = 3.0):
    cv2.imshow('Demo', mat)
    cv2.waitKey(int(delay * 1000))


def animate(mat: np.ndarray, split: int = 8):
    h, w, _ = mat.shape
    height = h // split
    for i in range(height):
        base = mat.copy()
        for s in range(split):
            for j in range(i, height):
                base[s * height + j, :, 0] = 255
                base[s * height + j, :, 1] = 255
                base[s * height + j, :, 2] = 255
        show(base, 0.025)


img = cv2.imread('img/wxx.jpg')
animate(img)
show(img)
