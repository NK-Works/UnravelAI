import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import tempfile

# Convert text to audio
def convert_text_to_audio(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        tts_audio_path = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False).name
        tts.save(tts_audio_path)
        st.audio(tts_audio_path, format='audio/mp3')
    except Exception as e:
        st.error(f"Error converting text to audio: {e}")

# Convert audio to text
def convert_audio_to_text(audio_file_path, lang):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data, language=lang)
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError:
            return "Speech recognition service is unavailable."
