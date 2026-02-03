import streamlit as st
from PIL import Image

def image_assistance():
    img = st.file_uploader("Upload injury image", type=["jpg","png"])
    if img:
        image = Image.open(img)
        st.image(image)
        st.info("Clean the area, apply antiseptic, and observe for swelling.")
