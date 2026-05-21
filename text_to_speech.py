import subprocess
import tempfile
import wave
import re
from piper import PiperVoice


class TextToSpeech:

    def __init__(self):
        print("Loading Piper voice...")
        self.voice = PiperVoice.load(
            "/home/voxa/piper/en_US-lessac-medium.onnx"
        )
        print("Piper ready")

    def speak(self, text):
        try:
            # =====================
            # CLEAN TEXT
            # =====================
            text = text.strip()
            text = re.sub(r"[^\w\s.,?!'’-]", "", text)
            text = text.replace("..", ".")
            text = text.replace("  ", " ")

            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                wav_path = f.name

            # =====================
            # SYNTHESIS
            # =====================
            with wave.open(wav_path, "wb") as wav_file:
                self.voice.synthesize_wav(text, wav_file, set_wav_format=True)

            # =====================
            # PLAYBACK
            # =====================
            subprocess.run(
                ["aplay", wav_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        except Exception as e:
            print("TTS error:", e)

    def cleanup(self):
        pass
