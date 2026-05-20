from faster_whisper import WhisperModel
from config import MODEL_SIZE


class SpeechToText:
    def __init__(self):
        print("Loading Faster-Whisper model...")

        self.model = WhisperModel(
            MODEL_SIZE,
            device="cpu",
            compute_type="int8"
        )

    def transcribe(self, audio_file):
        try:
            segments, info = self.model.transcribe(
                audio_file,
                language="en",
                beam_size=1
            )

            text = " ".join(segment.text for segment in segments).strip()

            if not text:
                return ""

            print("Detected:", text)
            return text

        except Exception as e:
            print("Speech-to-text error:", e)
            return ""
