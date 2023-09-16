import openai
import streamlit as st

st.title('Movie Poster Generator & Story Generator')
st.write("please")

# Parameters?
# setting, characters, mood, color scheme, text style
setting = st.text_input('Input a Setting:')
character = st.text_input('Input Characters/Monsters')
mood = st.text_input('Input your Atmosphere')
color_scheme = st.selectbox('Choose your color scheme', [])
font = st.selectbox('Choose Font Type', [])

# # if st.button('Generate Poster'):
# #     generate_poster(setting,character,mood,color_scheme,font);
# #     if st.button('Add Premise:'):
# #         generate_premise(setting,character,mood,color_scheme,font)


# # generating poster using model/API do some research?





# # Other group, find something for generating poster title, premise <-- Use Open API, integrate with Streamlit

if st.button("Generate"):
    openai.api_key = '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'
    messages = [ {"role": "system", "content":
                "You will create a horor movie title inspired by the following words"} ]
    prompts = [ {"role": "system", "content":
                "You will create a one paragraph plot to a horror movie inspired by the following words"} ]
    message = (setting + " " + character + " " + mood)
    prompt = (setting + " " + character + " " + mood)
    if message:
        messages.append({"role": "user", "content": message},)
        title = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        plot = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=prompts)

        reply = title.choices[0].message.content
        reply2 = plot.choices[0].message.content
    st.write(reply)
    st.write(reply2)
    messages.append({"role": "assistant", "content": reply})
    messages.append({"role": "assistant", "content": reply2})

        