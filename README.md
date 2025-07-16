# 🌐 Multilingual Translator Chatbot

An intelligent chatbot that translates English text into multiple languages like **Hindi**, **Punjabi**, **French**, **Spanish**, and more — with optional voice output using **Text-to-Speech (gTTS)**. Built using Python and Streamlit for a smooth web interface.


## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** – for building the interactive UI
- **Googletrans** – for real-time language translation
- **gTTS (Google Text-to-Speech)** – to generate speech from text


## 🚀 Features

 ✅ Translate English to:
- Hindi (`hi`)
- Punjabi (`pa`)
- French (`fr`)
- Spanish (`es`)
- German (`de`)
  
✅ Hear the translated output via text-to-speech  
✅ Fast, simple, and clean interface  
✅ Easily extendable to new languages or speech input


## 🧠 How It Works

1. User enters English text in the input box.
2. Selects the desired output language from the dropdown.
3. On clicking “Translate”:
   - Text is translated using Google Translate API.
   - Result is displayed on screen.
   - Audio is generated using `gTTS` and played.



## 📦 Installation

git clone https://github.com/niharikagoyal/Multilingual-Chatbot.git

cd multilingual-chatbot

pip install -r requirements.txt

streamlit run app.py

## 📂 Project Structure

multilingual-chatbot
/
│
├── app.py                 
├── translator.py          
├── requirements.txt        
└── README.md   

## 🌟 Future Improvements
🎙️ Add speech input using SpeechRecognition

🧠 Optionally integrate HuggingFace Transformers for better control

☁️ Deploy to Streamlit Cloud or Render for global access

💬 Store translation history for data analysis

## 🤝 Contributors
Niharika Goyal – Developer & Designer

## 📄 License
This project is licensed under the MIT License.

## 🙌 Acknowledgments
Google Translate
Streamlit
gTTS



