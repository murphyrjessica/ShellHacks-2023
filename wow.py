import openai
from sqlalchemy import PrimaryKeyConstraint
import streamlit as st
from PIL import Image

c1, c2, c3 = st.columns([0.9, 5, 0.2])


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
    st.write("<div style='text-align: center;'>Description</div>", unsafe_allow_html=True)
    st.write("How to:")

    c1, c2, c3 = st.columns([3, 3.8, 1.8])
    c1.write("Step 1: Choose a genre ")
    c2.write("Step 2: Complete the catagories ")
    c3.write("Step 3: Generate! ")

    c1, c2, c3 = st.columns([3, 3.8, 1.8])
    

    m = st.markdown("""
        <style>
            div.stButton > button:first-child {
                background-color: #42454c;color:white;font-size:20px;height:4em;width:36em;border-radius:10px 10px 10px 10px;);
            }
        </style>""", unsafe_allow_html=True)
    
    st.button("Horror", on_click=horror)
    st.button("Comedy", on_click=comedy)
    st.button("Action", on_click=action)
    st.button("Sci-Fi", on_click=scifi)
        
elif st.session_state.page == 1:
    def PATGenerator(setting, character, mood):
        openai.api_key = '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'
        messages = [ {"role": "system", "content":
            "You will create a short horror movie title inspired by the following list of words. The inputs are as follows The first line is the setting, the second is the characters/monsters and the third is the atmosphere"} ]
        prompts = [ {"role": "system", "content":
            "You will create a one paragraph plot to a horror movie inspired by the following words. The first line is the setting, the second is the characters/monsters and the third is the atmosphere and the last line is the title"} ]
        message = (setting + "\n" + character + "\n" + mood)
        if message:
            messages.append({"role": "user", "content": message})
            title = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = title.choices[0].message.content
        st.write(reply)
        messages.append({"role": "assistant", "content": reply})
        prompt = (setting  + "\n" + character + "\n" + mood + "\n" + reply)
        if prompt:
            prompts.append({"role": "user", "content": prompt})
            plot = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=prompts)
            reply2 = plot.choices[0].message.content
        st.write(reply2)
        prompts.append({"role": "assistant", "content": reply2})

# Parameters?
# setting, characters, mood, color scheme, text style
    setting = st.text_input('Input a Setting:')
    character = st.text_input('Input Characters/Monsters(Seperated by a Comma)')
    mood = st.text_input('Input your Atmosphere')
    color_scheme = st.selectbox('Choose your color scheme', [])
    font = st.selectbox('Choose Font Type', [])
    if st.button("Generate"):
        PATGenerator(setting, character, mood)

elif st.session_state.page == 2:
    def PATGenerator(setting, character, mood):
        openai.api_key = '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'
        messages = [ {"role": "system", "content":
            "You will create a short comedy movie title inspired by the following list of words. The inputs are as follows The first line is the setting, the second is the characters/monsters and the third is the atmosphere"} ]
        prompts = [ {"role": "system", "content":
            "You will create a one paragraph plot to a comedy movie inspired by the following words. The first line is the setting, the second is the characters/monsters and the third is the atmosphere and the last line is the title"} ]
        message = (setting + "\n" + character + "\n" + mood)
        if message:
            messages.append({"role": "user", "content": message})
            title = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = title.choices[0].message.content
        st.write(reply)
        messages.append({"role": "assistant", "content": reply})
        prompt = (setting  + "\n" + character + "\n" + mood + "\n" + reply)
        if prompt:
            prompts.append({"role": "user", "content": prompt})
            plot = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=prompts)
            reply2 = plot.choices[0].message.content
        st.write(reply2)
        prompts.append({"role": "assistant", "content": reply2})

# Parameters?
# setting, characters, mood, color scheme, text style
    setting = st.text_input('Input a Setting:')
    character = st.text_input('Input Characters/Monsters(Seperated by a Comma)')
    mood = st.text_input('Input your Atmosphere')
    color_scheme = st.selectbox('Choose your color scheme', [])
    font = st.selectbox('Choose Font Type', [])
    if st.button("Generate"):
        PATGenerator(setting, character, mood)

elif st.session_state.page == 3:
    def PATGenerator(setting, character, mood):
        openai.api_key = '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'
        messages = [ {"role": "system", "content":
            "You will create a short action movie title inspired by the following list of words. The inputs are as follows The first line is the setting, the second is the characters/monsters and the third is the atmosphere"} ]
        prompts = [ {"role": "system", "content":
            "You will create a one paragraph plot to a action movie inspired by the following words. The first line is the setting, the second is the characters/monsters and the third is the atmosphere and the last line is the title"} ]
        message = (setting + "\n" + character + "\n" + mood)
        if message:
            messages.append({"role": "user", "content": message})
            title = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = title.choices[0].message.content
        st.write(reply)
        messages.append({"role": "assistant", "content": reply})
        prompt = (setting  + "\n" + character + "\n" + mood + "\n" + reply)
        if prompt:
            prompts.append({"role": "user", "content": prompt})
            plot = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=prompts)
            reply2 = plot.choices[0].message.content
        st.write(reply2)
        prompts.append({"role": "assistant", "content": reply2})

# Parameters?
# setting, characters, mood, color scheme, text style
    setting = st.text_input('Input a Setting:')
    character = st.text_input('Input Characters/Monsters(Seperated by a Comma)')
    mood = st.text_input('Input your Atmosphere')
    color_scheme = st.selectbox('Choose your color scheme', [])
    font = st.selectbox('Choose Font Type', [])
    if st.button("Generate"):
        PATGenerator(setting, character, mood)
    
elif st.session_state.page == 4:
    def PATGenerator(setting, character, mood):
        openai.api_key = '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'
        messages = [ {"role": "system", "content":
            "You will create a short scifi movie title inspired by the following list of words. The inputs are as follows The first line is the setting, the second is the characters/monsters and the third is the atmosphere"} ]
        prompts = [ {"role": "system", "content":
            "You will create a one paragraph plot to a scifi movie inspired by the following words. The first line is the setting, the second is the characters/monsters and the third is the atmosphere and the last line is the title"} ]
        message = (setting + "\n" + character + "\n" + mood)
        if message:
            messages.append({"role": "user", "content": message})
            title = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = title.choices[0].message.content
        st.write(reply)
        messages.append({"role": "assistant", "content": reply})
        prompt = (setting  + "\n" + character + "\n" + mood + "\n" + reply)
        if prompt:
            prompts.append({"role": "user", "content": prompt})
            plot = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=prompts)
            reply2 = plot.choices[0].message.content
        st.write(reply2)
        prompts.append({"role": "assistant", "content": reply2})

# Parameters?
# setting, characters, mood, color scheme, text style
    setting = st.text_input('Input a Setting:')
    character = st.text_input('Input Characters/Monsters(Seperated by a Comma)')
    mood = st.text_input('Input your Atmosphere')
    color_scheme = st.selectbox('Choose your color scheme', [])
    font = st.selectbox('Choose Font Type', [])
    if st.button("Generate"):
        PATGenerator(setting, character, mood)

        
