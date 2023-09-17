import openai
from sqlalchemy import PrimaryKeyConstraint
import streamlit as st
import openai
import emoji
from PIL import Image, ImageOps, ImageDraw, ImageFont
from io import BytesIO
from dotenv import load_dotenv
import os
import requests

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

c1, c2, c3 = st.columns([0.9, 5, 0.2])

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

    # setting = st.text_input('Input a Setting:')
    # character = st.text_input('Input Characters/Monsters(Seperated by a Comma)')
    # mood = st.text_input('Input your Atmosphere')
    # color_scheme = st.selectbox('Choose your color scheme', [])
    # font = st.selectbox('Choose Font Type', [])

    params = {}

    setting = st.text_input('Input a Setting:')
    params['setting'] = setting

    character = st.text_input('Input Characters/Monsters(Seperated by a Comma)')
    params['character'] = character
    
    mood = st.text_input('Input the Atmosphere')
    params['mood'] = mood

    color_scheme = st.selectbox('Choose your color scheme', ['monochromatic', 'analogous', 'complementary', 'triadic', 'tetradic'])
    params['color_scheme'] = color_scheme

    user_font = st.selectbox("Select Poster Font: ", ['Impact','Trajan Pro', 'Helvetica Neue', 'Futura', 'Bank Gothic', 'Franklin Gothic', 'Avenir'])
    params['user_font'] = user_font

    return params

def create_title(params, genre):
    messages = [ {"role": "system", "content":
                f"You will create a short {genre} movie title inspired by the following list of words. \
                The inputs are as follows The first line is the setting, \
                the second is the characters/monsters and the third is the atmosphere"} ]
    #keys = list(params.keys())  

    message = (params['setting'] + " " + params['character'] + " " + " " + params['mood'])
    if message:
        messages.append({"role": "user", "content": message},)
        title = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        title = title.choices[0].message.content

    return title

def create_premise(params, title):
    # "You will create a one paragraph plot to a horror movie inspired by the following words. The first line is the setting, / 
    # the second is the characters/monsters and the third is the atmosphere and the last line is the title"
    messages = [ {"role": "system", "content":
                f"You will create a one paragraph plot to a {params['genre']} movie inspired by the following words. The first line is the setting,\
                the second is the characters/monsters and the third is the atmosphere and the last line is the title"} ]
    #keys = list(params.keys())  

    message = (params['setting'] + " " + params['character'] + " " + params['mood'] + " " + " " + title)
    if message:
        messages.append({"role": "user", "content": message},)
        premise = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        premise = title.choices[0].message.content

    return premise

def overlay(title,poster,user_font):
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


if "page" not in st.session_state:
    st.session_state.page = 0

def horror():
    st.session_state.page += 1

def comedy():
    st.session_state.page += 2

def action():
    st.session_state.page += 3

def scifi():
    st.session_state.page += 4


if st.session_state.page == 0:
    image = Image.open("ai_movie.jpg")
    c2.image(image, width=500)
    st.write("<div style='text-align: center;'>Discover creativity at its finest on our website powered by OpenAI's ChatGPT and DALL·E. Simply input your ideas, and watch as our AI crafts captivating movie poster titles and synopses that will leave you excited for a film that doesn't even exist yet.</div>", unsafe_allow_html=True)
    st.write("\n")
    # st.subheader("How to:")

    # c1, c2, c3 = st.columns([3, 3.5, 1.8])
    # c1.write("Step 1: Choose a genre ")
    # c2.write("Step 2: Complete the catagories ")
    # c3.write("Step 3: Generate! ")

    # c1, c2, c3 = st.columns([2.5, 3.8, 1.8])
    # image = Image.open("Menu1.png")
    # c1.image(image, width=200)
    # video_file = open('movievideo2.mp4', 'rb')
    # video_bytes = video_file.read()
    # c2.video(video_bytes)
    # video_file = open("Generate1.mp4", 'rb')
    # video_bytes = video_file.read()
    # c3.video(video_bytes)


    m = st.markdown("""
        <style>
            div.stButton > button:first-child {
                background-color: #42454c;color:white;font-size:20px;height:2.8em;width:36em;border-radius:10px 10px 10px 10px;);
            }
        </style>""", unsafe_allow_html=True)
    
    st.button("Horror", on_click=horror)
    st.button("Comedy", on_click=comedy)
    st.button("Action", on_click=action)
    st.button("Sci-Fi", on_click=scifi)
        
elif st.session_state.page == 1:
    # def PATGenerator(setting, character, mood):
    #     openai.api_key = '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'
    #     messages = [ {"role": "system", "content":
    #         "You will create a short horror movie title inspired by the following list of words. The inputs are as follows The first line is the setting, the second is the characters/monsters and the third is the atmosphere"} ]
    #     prompts = [ {"role": "system", "content":
    #         "You will create a one paragraph plot to a horror movie inspired by the following words. The first line is the setting, the second is the characters/monsters and the third is the atmosphere and the last line is the title"} ]
    #     message = (setting + "\n" + character + "\n" + mood)
    #     if message:
    #         messages.append({"role": "user", "content": message})
    #         title = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    #         reply = title.choices[0].message.content
    #     st.write(reply)
    #     messages.append({"role": "assistant", "content": reply})
    #     prompt = (setting  + "\n" + character + "\n" + mood + "\n" + reply)
    #     if prompt:
    #         prompts.append({"role": "user", "content": prompt})
    #         plot = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=prompts)
    #         reply2 = plot.choices[0].message.content
    #     st.write(reply2)
    #     prompts.append({"role": "assistant", "content": reply2})



# Parameters?
# setting, characters, mood, color scheme, text style

    genre = 'Horror'
    params = user_input()
    if st.button("Generate"):
        title = create_title(params, genre)
        premise = create_premise(params,genre)
        prompt = f"Create a image for a {genre} movie with a {params['setting']} setting and these character(s): {params['character']},\
        set in a {params['mood']} atmosphere  with a {params['color_scheme']} color scheme"

        poster = generate_poster(prompt)
        poster = overlay(title, poster, params['user_font'])
        col1, col2, col3 = st.columns([1,6,1])
        with col1:
            st.write("")
        with col2:
            st.image(poster, use_column_width=True)
        with col3:
            st.write("")


elif st.session_state.page == 2:
    genre = 'Comedy'
    params = user_input()
    if st.button("Generate"):
        title = create_title(params, genre)
        premise = create_premise(params,genre)
        prompt = f"Create a image for a {genre} movie with a {params['setting']} setting and these character(s): {params['character']},\
        set in a {params['mood']} atmosphere  with a {params['color_scheme']} color scheme"

        poster = generate_poster(prompt)
        poster = overlay(title, poster, params['user_font'])
        col1, col2, col3 = st.columns([1,6,1])
        with col1:
            st.write("")
        with col2:
            st.image(poster, use_column_width=True)
        with col3:
            st.write("") 
        

elif st.session_state.page == 3:
    genre = 'Action'
    params = user_input()

    if st.button("Generate"):
        title = create_title(params, genre)
        premise = create_premise(params,genre)
        prompt = f"Create a image for a {genre} movie with a {params['setting']} setting and these character(s): {params['character']},\
        set in a {params['mood']} atmosphere  with a {params['color_scheme']} color scheme"

        poster = generate_poster(prompt)
        poster = overlay(title, poster, params['user_font'])
        col1, col2, col3 = st.columns([1,6,1])
        with col1:
            st.write("")
        with col2:
            st.image(poster, use_column_width=True)
        with col3:
            st.write("") 

    
elif st.session_state.page == 4:

    genre = 'Sci-Fi'
    params = user_input()
    if st.button("Generate"):
        title = create_title(params, genre)
        premise = create_premise(params,genre)
        prompt = f"Create a image for a {genre} movie with a {params['setting']} setting and these character(s): {params['character']},\
        set in a {params['mood']} atmosphere  with a {params['color_scheme']} color scheme"

        poster = generate_poster(prompt)
        poster = overlay(title, poster, params['user_font'])
        col1, col2, col3 = st.columns([1,6,1])
        with col1:
            st.write("")
        with col2:
            st.image(poster, use_column_width=True)
        with col3:
            st.write("") 
        

        
