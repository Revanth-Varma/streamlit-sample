import streamlit as st
from pydub import AudioSegment
import speech_recognition as sr
import re
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import os
import tempfile

nltk.download('punkt')
nltk.download('wordnet')


# Function to convert audio file to WAV format
def convert_to_wav(audio_file, output_file_path):
    with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
        temp_audio.write(audio_file.read())
        temp_audio_path = temp_audio.name
    audio = AudioSegment.from_file(temp_audio_path)
    audio.export(output_file_path, format="wav")
    os.unlink(temp_audio_path)  # Delete the temporary audio file


# Function to convert speech to text
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
            st.error("Error fetching results; {0}".format(e))
            return ""

# Function to preprocess text
def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)

    porter_stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    stemmed_tokens = [porter_stemmer.stem(token) for token in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    lemmatized_text = ' '.join(lemmatized_tokens)

    return lemmatized_text

# Streamlit app
def main():
    st.title("Speech-to-Video Synthesis")

    option = st.radio("Choose an option:", ("Upload audio file", "Record audio"))

    if option == "Upload audio file":
        audio_file = st.file_uploader("Upload audio file", type=["mp3", "wav", "ogg"])
        if audio_file is not None:
            output_file_path = "converted_audio.wav"
            convert_to_wav(audio_file, output_file_path)
            text = speech_to_text(output_file_path)
            preprocessed_text = preprocess_text(text)
            test_text = {
                'text': preprocessed_text,
            }
            # Generate video and display it
            output_video_path = p(test_text)[OutputKeys.OUTPUT_VIDEO]
            st.video(output_video_path)

    elif option == "Record audio":
        st.write("Recording audio...")  # Placeholder for recording functionality

if __name__ == "__main__":
    main()
