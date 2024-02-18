import streamlit as st
from PIL import Image
import cv2 as cv

img = Image.open("aot.jpeg")
aot = st.image(img, width=200)

if st.checkbox("Show/Hide"):
    st.text("Image in camouflage")
    aot.image(img,width=1)

status = st.radio("Select Gender: ", ('Computer', 'English', 'Business'))
st.success(status)