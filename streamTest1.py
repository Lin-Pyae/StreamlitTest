import streamlit as st

esub = st.selectbox("Elective,",["Japan","Korea","Music"])

st.write("Your elective subject is:" , esub)



hobbies = st.multiselect("Hobbies",["Painting", "Swimming", "Music"])
st.write(f"You selected {hobbies}")


if(st.button("Click me")):
    st.text("Hello world")

name = st.text_input("Enter you name", "Type Here")

if(st.button('Submit')):
    result=name.title()
    st.write(f"Hello {name}")

level = st.slider("Select the level", 1, 10)

st.text(f'Selected level is {level}')