import cv2
import dlib
import numpy as np


def show(pic: np.ndarray, delay: float = 3.0) -> None:
    cv2.imshow('Demo', pic)
    cv2.waitKey(int(delay * 1000))


def convert_to_gray(image: np.ndarray) -> np.ndarray:
    gray = image.copy()
    if len(image.shape) >= 3:
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    return cv2.equalizeHist(gray)


def draw_location(image: np.ndarray, location: dlib.rectangle,
                  color=(0, 255, 0), thickness=1) -> None:
    cv2.rectangle(image,
                  (location.left(), location.top()),
                  (location.right(), location.bottom()),
                  color, thickness)
