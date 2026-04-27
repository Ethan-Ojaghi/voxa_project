# text_to_speech.py

from gtts import gTTS
import os

import os

class TextToSpeech:

    def speak(self, text):
        if not text:
            return

        try:
            os.system(f'espeak "{text}"')

        except Exception as e:
            print("TTS error:", e)
