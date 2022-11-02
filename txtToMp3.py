from googletrans import Translator
from gtts import gTTS
import os

with open('test.txt', encoding="utf8") as file:
    long = file.read()
try:
    translator = Translator()
    from_lang = 'en'
    to_lang = 'ta'
    text_to_translate = translator.translate(long, src=from_lang, dest=to_lang)
    text = text_to_translate.text
    speak = gTTS(text=text, lang=to_lang, slow=False)
    print('speak completed')
    speak.save("captured_voice.mp3")
    print("saved")
    os.system("start captured_voice.mp3")
except:
    print("some times went wrong")
