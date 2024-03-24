import streamlit as st
from pydub import AudioSegment
import speech_recognition as sr
from io import BytesIO

# Function to convert audio file to PCM WAV format
def convert_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="wav")

# Function to convert audio file to text
def speech_to_text(audio_file):
    # Convert audio file to PCM WAV format
    wav_file = "converted_audio.wav"
    convert_to_wav(audio_file, wav_file)

    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, could not understand audio"
        except sr.RequestError as e:
            return f"Error fetching results; {e}"

# Main streamlit app
def main():
    st.title("Speech to Text Converter")

    # File upload section
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])

    if uploaded_file is not None:
        # Convert uploaded file to bytes
        audio_bytes = BytesIO(uploaded_file.read())

        # Convert audio to text
        text = speech_to_text(audio_bytes)

        # Display the converted text
        st.header("Converted Text:")
        st.write(text)

if __name__ == "__main__":
    main()
