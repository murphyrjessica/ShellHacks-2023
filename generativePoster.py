import streamlit as st
import openai
import emoji
from PIL import Image, ImageOps, ImageDraw
from io import BytesIO
from dotenv import load_dotenv
import os
import requests


def generate_poster(prompt):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Image.create(
        prompt = prompt,
        n = 1,
        size = '512x512'
    )
    image_url = response['data'][0]['url']
    #st.write(image_url)

    image_data = requests.get(image_url).content
    image = Image.open(BytesIO(image_data))



    border_color = 'white'
    border_width = 40
    image_with_border = ImageOps.expand(image, border=border_width, fill = border_color)
    draw = ImageDraw.Draw(image_with_border)
    
    return image_with_border

st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: #FF6347;
        }
        .stButton>button {
            background-color: #FF4500;
            color: #FFFFFF;
        }
    </style>
    """, unsafe_allow_html=True)

st.title('🎃DALL-E Movie Poster Generator👻')

# Parameters?
# setting, characters, mood, color scheme, text style
#genre = st.selectbox('Select Genre':, [])
genre = st.selectbox('Choose a Genre:', ['Horror'])
setting = st.selectbox('Choose a Setting:', ['Haunted House'])
character = st.selectbox('Choose Characters/Monsters', ['Frankenstein'])
mood = st.selectbox('Choose you Atmosphere',['Graveyard'])
color_scheme = st.selectbox('Choose your color scheme', ['Bright and Vibrant'])
#font = st.selectbox('Choose Font Type', []) ??

# generating poster using model/API do some research?

if st.button('Generate Poster'):
    prompt = f"Create a movie poster for a {genre} movie with a {setting} setting and these character(s): {character},\
    set in this mood/atmosphere: {mood} with a {color_scheme} color scheme"
    poster = generate_poster(prompt)

    # Center Poster
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")
    with col2:
        st.image(poster, use_column_width=True)
        st.markdown('### Movie Premise')    
    with col3:
        st.write("")











# Other group, find something for generating poster title, premise <-- Use Open API, integrate with Streamlit

