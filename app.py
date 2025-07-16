import streamlit as st
from translator import translate_text
from speech import speak_text

st.set_page_config(page_title="🗣️ Multilingual Translator Chatbot")

st.title("🌍 Multilingual Chatbot")
st.markdown("Type in English and get responses in your selected language!")

# User input
user_input = st.text_input("Enter your message in English:")

# Language options
language_options = {
    "Hindi": "hi",
    "Punjabi": "pa",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Spanish": "es",
    "Korean": "ko"
}

# Language selector
selected_lang = st.selectbox("Choose response language:", list(language_options.keys()))
lang_code = language_options[selected_lang]

# Generate button
if st.button("Translate and Speak"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated = translate_text(user_input, lang_code)
        st.success(f"🤖 Bot ({selected_lang}): {translated}")
        
        try:
            speak_text(translated, lang=lang_code)
        except Exception as e:
            st.error(f"Could not play audio: {e}")
