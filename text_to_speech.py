import subprocess
import tempfile
import os


class TextToSpeech:
    def __init__(self):

        self.model_path = "/home/voxa/piper/en_US-lessac-low.onnx"

        # Keep Piper alive
        self.piper = subprocess.Popen(
            [
                "piper",
                "--model",
                self.model_path,
                "--output_raw"
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        )

    def speak(self, text):

        try:
            # Send text to Piper
            self.piper.stdin.write((text + "\n").encode())
            self.piper.stdin.flush()

            # Temporary raw audio file
            raw_path = "/tmp/voxa.raw"
            wav_path = "/tmp/voxa.wav"

            # Read generated raw audio
            raw_audio = self.piper.stdout.read(22050 * 2 * 5)

            with open(raw_path, "wb") as f:
                f.write(raw_audio)

            # Convert raw -> wav
            subprocess.run([
                "ffmpeg",
                "-y",
                "-f", "s16le",
                "-ar", "22050",
                "-ac", "1",
                "-i", raw_path,
                wav_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # Play audio
            subprocess.run(
                ["aplay", wav_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        except Exception as e:
            print("TTS error:", e)

    def cleanup(self):
        self.piper.kill()
