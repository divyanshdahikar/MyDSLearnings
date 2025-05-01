import streamlit as st
from streamlit_drawable_canvas import st_canvas
st.header('This is my ml demo')

st.text_input('Enter your text here')

st.button('Submit')

st.file_uploader('Upload your file')

canvas_output = st_canvas(
    height = 400,
    width = 400,
    stroke_width = 5,
    stroke_color = 'red'
)

if canvas_output and (canvas_output.image_data is not None):

    # print(canvas_output.image_data.shape)
    image = canvas_output.image_data
    st.image(image)