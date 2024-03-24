import streamlit as st
import os
from pydub import AudioSegment
import speech_recognition as sr
import re
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys

# Function to convert audio file to text
def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))
            return ""

# Function to preprocess text
def preprocess_text(text):
    # Remove non-alphabetic characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize the text
    tokens = word_tokenize(text)

    porter_stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    stemmed_tokens = [porter_stemmer.stem(token) for token in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    lemmatized_text = ' '.join(lemmatized_tokens)

    return lemmatized_text

@st.experimental_memo
def load_model():
    from modelscope.pipelines import pipeline
    return pipeline('text-to-video-synthesis', 'damo/text-to-video-synthesis')

def main():
    uploaded_file = st.file_uploader("Upload an audio file", type=["ogg"])
    if uploaded_file is not None:
        # Save the uploaded file
        audio_path = "uploaded_audio.ogg"
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        # Convert audio to text
        text = speech_to_text(audio_path)
        st.write("Text from audio:", text)

        # Preprocess text
        preprocessed_text = preprocess_text(text)
        st.write("Preprocessed text:", preprocessed_text)

        # Load the model
        p = load_model()

        test_text = {
            'text': preprocessed_text,
        }
        output_video_path = p(test_text,)[OutputKeys.OUTPUT_VIDEO]
        st.write('output_video_path:', output_video_path)

        # Provide a download link for the video
        st.markdown(f"Download video [here]({output_video_path})")

        # Clean up uploaded audio file
        os.remove(audio_path)

if __name__ == "__main__":
    main()
