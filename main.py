from face import *
from utils import *

# step 0: load contents
pic1 = cv2.imread('img/demo_unmask.png')
pic2 = cv2.imread('img/demo_mask.jpg')
doctor = cv2.imread('img/doctor.jpg')
mask = cv2.imread('img/mask_blue.png', cv2.IMREAD_UNCHANGED)
text_unmask = cv2.imread('img/text_unmask.jpg')
text = cv2.imread('img/text.jpg')

# part 1
base = load(pic1, doctor)
canvas = base.copy()
show(canvas, 1)
gray = convert_to_gray(canvas)
loc = location(gray)
landmark = landmarks(gray, loc)
draw_location(canvas, loc, (0, 0, 255), 2)
show(canvas, 1.5)
show_mask(base.copy(), mask, landmark)
show_text(canvas, text_unmask)
show_text(canvas, text)

# part 2
base = load(pic2, doctor)
canvas = base.copy()
show(canvas, 1)
cv2.rectangle(canvas, (290, 60), (445, 210), (0, 255, 0), 2)
show(canvas, 1.5)
# show_text(canvas, text_unmask)
# show_text(canvas, text)
cv2.destroyAllWindows()
