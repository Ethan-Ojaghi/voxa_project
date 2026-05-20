import subprocess
import tempfile
import wave
from piper import PiperVoice


class TextToSpeech:

    def __init__(self):
        print("Loading Piper voice...")
        self.voice = PiperVoice.load(
            "/home/voxa/piper/en_US-lessac-low.onnx"
        )
        print("Piper ready")

    def speak(self, text):
        try:
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                wav_path = f.name

            # Piper writes directly to wav
            with wave.open(wav_path, "wb") as wav_file:
                self.voice.synthesize_wav(text, wav_file)

            # play it (ALSA fallback is fine)
            subprocess.run(
                ["aplay", wav_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        except Exception as e:
            print("TTS error:", e)

    def cleanup(self):
        pass
