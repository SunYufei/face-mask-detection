import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def draw(pic: str, font_size: int = 10):
    img = cv2.imread(pic)
    img = img[:, :, (2, 1, 0)]
    blank = Image.new('RGB', [len(img[0]), len(img)], 'white')
    draw_obj = ImageDraw.Draw(blank)
    font = ImageFont.truetype('C:/Windows/Fonts/Microsoft YaHei UI/msyhbd.ttc', size=font_size - 1)
    for i in range(0, len(img), font_size):
        for j in range(0, len(img[i]), font_size):
            text = '中国加油'
            draw_obj.ink = img[i][j][0] + img[i][j][1] * 256 + img[i][j][2] * 256 * 256
            draw_obj.text([j, i], text[j // font_size % len(text)], font=font)
    cv2.imshow('Demo', np.asarray(blank))


cv2.imshow('Demo', cv2.imread('img/cyf.jpg'))
cv2.waitKey(1500)
draw('img/cyf.jpg', 10)
cv2.waitKey(3000)
