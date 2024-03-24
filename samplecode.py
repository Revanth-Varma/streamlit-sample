import streamlit as st
from pydub import AudioSegment
import speech_recognition as sr
import requests
import os

# Function to convert audio file to PCM WAV format
def convert_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="wav")

# Function to convert audio file to text
def speech_to_text(audio_file):
    # Convert audio file to PCM WAV format
    wav_file = "/tmp/converted_audio.wav"
    convert_to_wav(audio_file, wav_file)

    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
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

    # File URL input
    file_url = st.text_input("Enter the URL of the audio file:")
    if file_url:
        # Download the file from the URL
        audio_file = requests.get(file_url)
        if audio_file.status_code == 200:
            with open("/tmp/audio_file", "wb") as f:
                f.write(audio_file.content)
            
            # Display the uploaded file
            st.audio(audio_file.content, format='audio/ogg')

            # Convert audio to text
            text = speech_to_text("/tmp/audio_file")

            # Display the converted text
            if text:
                st.header("Converted Text:")
                st.write(text)
                
            # Delete the temporary audio file
            os.remove("/tmp/audio_file")
        else:
            st.error("Failed to download file from the provided URL.")

if __name__ == "__main__":
    main()
