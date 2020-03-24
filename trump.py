from face import *
from utils import *

# step 0: load contents
pic = cv2.imread('img/trump.jpg')
doctor = cv2.imread('img/doctor.jpg', cv2.IMREAD_UNCHANGED)
mask = cv2.imread('img/mask_blue.png', cv2.IMREAD_UNCHANGED)
text = cv2.imread('img/trump_text.jpg')

# step 1: load picture
base = load(pic, doctor)
canvas = base.copy()
show(canvas, 1)

# step 2: mask detection
gray = convert_to_gray(canvas)
location = location(gray)
landmarks = landmarks(gray, location)

draw_location(canvas, location, (0, 0, 255), 2)
show(canvas, 1.5)

# step 3: draw mask
show_mask(base.copy(), mask, landmarks, True)

# step 4: end
show_text(canvas, text)

cv2.destroyAllWindows()
