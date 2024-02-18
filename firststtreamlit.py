import streamlit as st
import pandas as pd
from PIL import Image

st.write("My First Stremlit app")
data={"sales":[30,40,50,20,10,40]}
df=pd.DataFrame(data)
st.line_chart(df)


#Opening Image file 
image = Image.open('aot.jpeg')

#displaying the image on streamlit app
st.image(image, caption='Display aot Image')

st.exception("Error Tat Nay P")