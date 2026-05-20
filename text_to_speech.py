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

        cmd = f'echo "{text}" | piper --model "{self.voice_path}" --output_file "{wav_path}"'

        subprocess.run(cmd, shell=True, check=True)

        os.system(f"aplay {wav_path} > /dev/null 2>&1")

    except Exception as e:
        print("TTS error:", e)
