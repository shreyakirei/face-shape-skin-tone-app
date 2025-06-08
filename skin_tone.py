import cv2
import numpy as np

def get_skin_tone(image, landmarks):
    # Take a small patch around cheek point for skin sample
    cheek_point = landmarks[127]  # left cheek approx
    x, y = cheek_point
    patch = image[max(y-10,0):y+10, max(x-10,0):x+10]

    if patch.size == 0:
        return "Unknown"

    avg_color = np.mean(np.mean(patch, axis=0), axis=0)  # BGR average

    # Convert BGR to RGB for easier visualization
    avg_rgb = avg_color[::-1]

    # Simple threshold for skin tone classification (very rough):
    r, g, b = avg_rgb
    if r > 180 and g > 140 and b > 130:
        tone = "Light"
    elif r > 140 and g > 100 and b > 90:
        tone = "Medium"
    else:
        tone = "Dark"
    return tone
