from gtts import gTTS
import os

def ovoz_chaqir_gTTS(raqam):
    text = f"Navbat raqami {raqam}, iltimos, keling!"
    tts = gTTS(text=text, lang='uz')
    tts.save("chaqiruv.mp3")
    os.system("start chaqiruv.mp3")
