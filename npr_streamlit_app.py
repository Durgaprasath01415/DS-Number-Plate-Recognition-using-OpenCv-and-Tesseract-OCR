
import streamlit as st
import cv2
import pytesseract
import numpy as np
from PIL import Image

st.set_page_config(page_title="NPR Streamlit App", layout="centered")
st.title("🚗Number Plate Recognition (NPR)")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update for Windows if needed

uploaded_file = st.file_uploader("Upload an image with a license plate", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_np = np.array(image.convert('RGB'))

    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocessing
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    edged = cv2.Canny(gray, 100, 200)

    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    plate_contour = None
    for c in contours:
        approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
        if len(approx) == 4:
            plate_contour = approx
            break

    if plate_contour is not None:
        mask = np.zeros(gray.shape, dtype=np.uint8)
        cv2.drawContours(mask, [plate_contour], -1, 255, -1)
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        cropped = gray[topx:bottomx+1, topy:bottomy+1]

        # OCR
        text = pytesseract.image_to_string(cropped, config='--psm 8 --psm 12')
        st.subheader("🔍 Detected License Plate Number:")
        st.success(text.strip())

        # Show ROI
        st.image(cropped, caption="Detected Plate Region", use_column_width=False, channels="GRAY")
    else:
        st.warning("No license plate detected in the image.")
