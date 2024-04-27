import pathlib
import textwrap
import base64

from gtts import gTTS
import google.generativeai as genai

from IPython.display import display, Audio
from IPython.display import Markdown
import streamlit as st


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY = "AIzaSyB_fU_fKQrs4jN-ygzam5Xk0QUWaajbnok"

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def speech_to_text(audio_data):
    with open(audio_data, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            response_format="text",
            file=audio_file
        )
    return transcript['text']

def text_to_speech(input_text):
    tts = gTTS(text=input_text,lang='en',tld='co.in',slow=False)
    sound_file = '1.wav'
    return sound_file

def get_answer(messages):
    response = model.generate_content(f"You are an caring , loving and consoling chatbot which will hear problems from women answer like sad to hear that, you will be fine soon and suggest some good things to do to lighten up the mood. talk like a human which understand and help in low times. answer should be short and motivating. {messages}")
    text = to_markdown(response.text)
    return text

def autoplay_audio(file_path:str):
    with open(file_path,"rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    md = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.audio(md)        