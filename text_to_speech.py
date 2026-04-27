# text_to_speech.py

from gtts import gTTS
import os


class TextToSpeech:

    def speak(self, text, lang="en"):
        if not text:
            return

        try:
            tts = gTTS(text=text, lang=lang)
            tts.save("output.mp3")

            os.system("mpg321 output.mp3 > /dev/null 2>&1")

        except Exception as e:
            print("TTS error:", e)
