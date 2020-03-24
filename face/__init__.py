from .face import Face

_face = Face()


def location(gray):
    ret = _face.locations(gray)
    return ret[0] if len(ret) else None


def landmarks(gray, face_location):
    return _face.landmarks(gray, face_location)
