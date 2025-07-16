from gtts import gTTS
import os
from playsound import playsound

def speak_text(text, lang='hi'):
    tts = gTTS(text=text, lang=lang)
    filename = "response.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
