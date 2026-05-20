import os
import subprocess
import tempfile

class TextToSpeech:
    def __init__(self):
        self.voice_path = "/home/voxa/piper/en_US-lessac-medium.onnx"

    def speak(self, text, lang="en"):
        if not text:
            return

        try:
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                wav_path = f.name

            cmd = [
                "piper",
                "--model", self.voice_path,
                "--output_file", wav_path
            ]

            subprocess.run(
                cmd,
                input=text,
                text=True,
                check=True
            )

            subprocess.run(
                ["aplay", "-D", "plughw:2,0", wav_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            os.remove(wav_path)

        except Exception as e:
            print("TTS error:", e)
