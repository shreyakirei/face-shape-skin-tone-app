import numpy as np

def euclidean_dist(pt1, pt2):
    return np.linalg.norm(np.array(pt1) - np.array(pt2))

def detect_face_shape(landmarks):
    # Landmarks index example from MediaPipe:
    # Chin: 152, Jaw left: 234, Jaw right: 454, Forehead top: 10, Cheek left: 127, Cheek right: 356

    jaw_left = landmarks[234]
    jaw_right = landmarks[454]
    chin = landmarks[152]
    forehead = landmarks[10]

    face_width = euclidean_dist(jaw_left, jaw_right)
    face_length = euclidean_dist(forehead, chin)

    ratio = face_length / face_width

    # Simple heuristic:
    if ratio > 1.5:
        shape = "Oval"
    elif ratio > 1.3:
        shape = "Round"
    elif ratio < 1.2:
        shape = "Square"
    else:
        shape = "Heart"

    return shape
