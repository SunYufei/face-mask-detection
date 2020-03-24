import numpy as np

from .image import show


def show_text(image: np.ndarray,
              text: np.ndarray):
    height, width, _ = image.shape
    rows, cols, _ = text.shape

    image = np.ones(image.shape, dtype=np.uint8)
    for i in range(3):
        image[:, :, i] = 255

    x = (width - cols) // 2
    y = (height - rows) // 2
    for i in range(cols):
        for j in range(rows):
            for k in range(3):
                image[y + j, x + i][k] = text[j, i][k]

    show(image, 3.5)
