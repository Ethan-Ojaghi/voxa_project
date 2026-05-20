import subprocess
import tempfile
import os


class TextToSpeech:

    def __init__(self):
        self.model_path = "/home/voxa/piper/en_US-lessac-low.onnx"

    def speak(self, text):

        try:

            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                wav_path = f.name

            subprocess.run(
                [
                    "piper",
                    "--model",
                    self.model_path,
                    "--output_file",
                    wav_path
                ],
                input=text.encode(),
                check=True
            )

            subprocess.run(
                ["paplay", wav_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            os.remove(wav_path)

        except Exception as e:
            print("TTS error:", e)

    def cleanup(self):
        pass
