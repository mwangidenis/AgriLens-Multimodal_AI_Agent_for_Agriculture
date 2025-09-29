# app.py
import streamlit as st
from PIL import Image
from image_utils import analyze_image
from text_utils import generate_response

st.set_page_config(page_title="AgriLens", layout="centered")
st.title("🌾 AgriLens: Smart Agriculture Assistant")

uploaded_file = st.file_uploader("Upload a crop image", type=["jpg", "png"])
user_prompt = st.text_input("Enter your question or instruction")

if uploaded_file and user_prompt:
    image = Image.open(uploaded_file)
    image_data = analyze_image(image)
    response = generate_response(user_prompt, image_data)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.subheader("🧠 AgriLens Response")
    st.write(response)