
import streamlit as st
import joblib

model = joblib.load("language_detection_model.pkl")

st.title("🌍 Language Detection App")
st.write("Enter a sentence to detect its language.")

text = st.text_area("Enter your text:")

languages = {
    "ar": "Arabic", "bg": "Bulgarian",
    "de": "German", "el": "Greek",
    "en": "English", "es": "Spanish",
    "fr": "French", "hi": "Hindi",
    "it": "Italian", "ja": "Japanese",
    "nl": "Dutch", "pl": "Polish",
    "pt": "Portuguese", "ru": "Russian",
    "sw": "Swahili", "th": "Thai",
    "tr": "Turkish", "ur": "Urdu",
    "vi": "Vietnamese", "zh": "Chinese"
}

greetings = {
    "ciao": ("Italian", "it"),
    "hello": ("English", "en"),
    "hi": ("English", "en"),
    "bonjour": ("French", "fr"),
    "hola": ("Spanish", "es"),
    "hallo": ("German", "de"),
    "olá": ("Portuguese", "pt"),
    "ola": ("Portuguese", "pt"),
    "namaste": ("Hindi", "hi"),
    "नमस्ते": ("Hindi", "hi")
}

if st.button("Detect Language"):
    if text.strip():
        clean_text = text.strip().lower()
        first_word = clean_text.split()[0].strip(".,!?")

        if clean_text in greetings:
            language, code = greetings[clean_text]
        elif first_word in greetings:
            language, code = greetings[first_word]
        else:
            code = model.predict([text.strip()])[0]
            language = languages.get(code, code)

        st.success(f"Detected Language: {language}")
        st.write(f"Language code: {code}")
    else:
        st.warning("Please enter some text.")
