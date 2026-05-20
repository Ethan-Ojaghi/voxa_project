# text_to_speech.py

from gtts import gTTS
from pydub import AudioSegment
import os

class TextToSpeech:
    def speak(self, text, lang="en"):
        if not text:
            return

        try:
            tts = gTTS(text=text, lang=lang)
            tts.save("output.mp3")

            # convert to wav
            sound = AudioSegment.from_mp3("output.mp3")
            sound.export("output.wav", format="wav")

            os.system("aplay -D plughw:2,0 output.wav > /dev/null 2>&1")

        except Exception as e:
            print("TTS error:", e)
