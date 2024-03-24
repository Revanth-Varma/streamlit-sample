import streamlit as st
from pydub import AudioSegment
import speech_recognition as sr

# Function to convert audio file to text
def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, could not understand audio")
            return ""
        except sr.RequestError as e:
            st.error(f"Error fetching results; {e}")
            return ""

# Main streamlit app
def main():
    st.title("Speech to Text Converter")

    # File upload section
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])

    if uploaded_file is not None:
        # Display the uploaded file
        st.audio(uploaded_file, format='audio/ogg')

        # Convert audio to text
        text = speech_to_text(uploaded_file)

        # Display the converted text
        if text:
            st.header("Converted Text:")
            st.write(text)

if __name__ == "__main__":
    main()
