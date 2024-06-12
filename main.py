import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

upload_image = st.file_uploader("Upload image")
with st.expander("camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    pil_image = Image.open(camera_image)
    gray_image = pil_image.convert("L")
    st.image(gray_image)

if upload_image:
    pil2_image = Image.open(upload_image)
    gray2_image = pil2_image.convert("L")
    st.image(gray2_image)