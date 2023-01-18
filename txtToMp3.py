import aspose.words as aw
from googletrans import Translator
from gtts import gTTS
import os

path = input("Enter Your Path")
print(path.find("."))
doc = aw.Document("D:\Python\storybook\Muthu Raman.docx")
doc.save("123.txt")

print(path.find("."))

with open("D:\Python\storybook\Muthu Raman.docx", encoding="utf8") as file:
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
