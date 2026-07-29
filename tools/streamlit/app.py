import streamlit as st

st.title("Hello Streamlit")
st.header("Welcome to Streamlit")
st.subheader("This is Subheader")
st.write("This is my first Streamlit App")
st.text("This is plain text")

# Buttons, checkboxes and Sliders
if st.button("Click me"):
    st.write("button clicked")

agree= st.checkbox("I agree")
if agree:
    st.write("You agreed")

level = st.slider("Select a level :", 1, 10, 6)
st.write(f"selected level: {level}")
