import dlib
import numpy as np


class Face:
    def __init__(self):
        self._face_detector = dlib.get_frontal_face_detector()
        self._predictor = dlib.shape_predictor('face/shape_predictor_68_face_landmarks.dat')

    def locations(self, gray: np.ndarray, number_of_times_to_up_sample=0):
        return self._face_detector(gray, number_of_times_to_up_sample)

    def landmarks(self, gray: np.ndarray, location: dlib.rectangle):
        if location is None:
            location = self.locations(gray)[0]
        shape = self._predictor(gray, location)
        return [(shape.part(i).x, shape.part(i).y) for i in range(shape.num_parts)]
