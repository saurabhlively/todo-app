import streamlit as st
from PIL import Image


with st.expander("Start Camera"):
    #Start the camera
    camera_photo = st.camera_input("Camera")

if camera_photo:
    #Create pillow instance
    img=Image.open(camera_photo)

    #Converted pillow image to grey image
    gray_img = img.convert("L")

    #Render greyscale image on webpage
    st.image(gray_img)

