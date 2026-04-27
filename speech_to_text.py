# speech_to_text.py

import whisper
from config import MODEL_SIZE


class SpeechToText:
    def __init__(self):
        print("Loading Whisper model...")
        self.model = whisper.load_model(MODEL_SIZE)

    def transcribe(self, audio_file):
        try:
            result = self.model.transcribe(audio_file)

            text = result.get("text", "").strip()
            _ = result.get("language", "")  # FIXED: unused variable

            if not text:
                return ""

            print("Detected:", text)
            return text

        except Exception as e:
            print("Speech-to-text error:", e)
            return ""
