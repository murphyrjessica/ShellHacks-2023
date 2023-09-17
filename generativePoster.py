import streamlit as st
import openai
import emoji
from PIL import Image, ImageOps, ImageDraw, ImageFont
from io import BytesIO
from dotenv import load_dotenv
import os
import requests


def generate_poster(prompt):
    response = openai.Image.create(
        prompt = prompt,
        n = 1,
        size = '512x512'
    )
    image_url = response['data'][0]['url']

    image_data = requests.get(image_url).content
    image = Image.open(BytesIO(image_data))

    border_color = 'black'
    border_width = 50
    image_with_border = ImageOps.expand(image, border=border_width, fill = border_color)
    draw = ImageDraw.Draw(image_with_border)
    
    return image_with_border

def overlay(title, poster, user_font):
    
    draw = ImageDraw.Draw(poster)
    font_size = int(poster.size[0] * 0.05)

    if user_font == 'Impact':
        font_path = 'fonts/Impact.TTF'
    elif user_font == 'Trajan Pro':
        font_path = 'fonts/TrajanPro.ttf'
    elif user_font == 'Helvetica Neue':
        font_path = 'fonts/HelveticaNeue.ttf'
    elif user_font == 'Futura':
        font_path = 'fonts/Futura.ttf'
    elif user_font == 'Bank Gothic':
        font_path = 'fonts/BankGothic.ttf'
    elif user_font == 'Franklin Gothic':
        font_path = 'fonts/FranklinGothic.TTF'
    else:
        font_path = 'fonts/Avenir.ttf'

    if os.path.isfile(font_path):
        font = ImageFont.truetype(font_path,font_size)

    text_width, text_height = draw.textsize(title,font)

    position = ((poster.width - text_width) / 2, 50 / 4 )

    draw.text(position, title, font=font, fill = 'white')

    return poster

# Parameters
def user_input():
    params = {}
    genre = st.selectbox('Choose a Genre:', ['Horror', 'Adventure', 'Science Fiction'])
    params['genre'] = genre

    setting = st.text_input('Input a Setting:')
    params['setting'] = setting

    character = st.text_input('Input Characters/Monsters')
    params['character'] = character
    
    mood = st.text_input('Input the Atmosphere')
    params['mood'] = mood

    color_scheme = st.selectbox('Choose your color scheme', ['monochromatic', 'analogous', 'complementary', 'triadic', 'tetradic'])
    params['color_scheme'] = color_scheme

    user_font = st.selectbox("Select Poster Font: ", ['Impact','Trajan Pro', 'Helvetica Neue', 'Futura', 'Bank Gothic', 'Franklin Gothic', 'Avenir'])
    params['user_font'] = user_font

    return params
    
def create_title(params):
    messages = [ {"role": "system", "content":
                "Create a really short movie title inspired by the following words: "} ]
    #keys = list(params.keys())  

    message = (params['genre'] + " " + params['setting'] + " " + params['character'] + " " + " " + params['mood'])
    if message:
        messages.append({"role": "user", "content": message},)
        title = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        title = title.choices[0].message.content

    return title

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title('🎃DALL-E Movie Poster Generator👻')
st.divider()

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

if 'init' not in st.session_state:
    st.session_state.init = True
    st.session_state.poster = None
    st.session_state.title = None
    st.session_state.user_font = None

params = user_input()

if st.button('Enter'):
    prompt = f"Create a image for a {params['genre']} movie with a {params['setting']} setting and these character(s): {params['character']},\
    set in a {params['mood']} atmosphere  with a {params['color_scheme']} color scheme"
    st.session_state.poster = generate_poster(prompt)

    st.session_state.title = create_title(params)
    
    st.session_state.poster = overlay(st.session_state.title, st.session_state.poster, params['user_font'])

    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image(st.session_state.poster, use_column_width=True)
    with col3:
        st.write("")
            