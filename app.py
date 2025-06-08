import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Import your utils here (make sure you have these files in utils/ folder)
from utils.face_detection import detect_face_landmarks
from utils.face_shape import detect_face_shape
from utils.skin_tone import get_skin_tone
from utils.suggestions import get_suggestions

st.title("Face Shape & Skin Tone Suggestion")

# File uploader accepts only image files
uploaded_file = st.file_uploader("Upload a clear face image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image and convert to BGR for OpenCV processing
    image = np.array(Image.open(uploaded_file).convert("RGB"))
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Detect landmarks
    landmarks = detect_face_landmarks(image_bgr)

    if landmarks is None:
        st.error("No face detected. Please upload a clear face image with a visible face.")
    else:
        # Detect face shape and skin tone
        face_shape = detect_face_shape(landmarks)
        skin_tone = get_skin_tone(image_bgr, landmarks)

        # Get suggestions
        suggestions = get_suggestions(face_shape, skin_tone)

        # Show uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Show detected features
        st.write(f"**Detected Face Shape:** {face_shape}")
        st.write(f"**Detected Skin Tone:** {skin_tone}")

        # Show suggestions
        st.subheader("Suggestions")
        st.markdown(f"**Makeup:** {suggestions['makeup']}")
        st.markdown(f"**Hairstyle:** {suggestions['hairstyle']}")
        st.markdown(f"**Skincare:** {suggestions['skincare']}")

else:
    st.info("Please upload an image file to get suggestions.")
