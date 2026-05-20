from piper import PiperVoice
import sounddevice as sd
import numpy as np


class TextToSpeech:

    def __init__(self):
        print("Loading Piper voice...")

        self.voice = PiperVoice.load(
            "/home/voxa/piper/en_US-lessac-low.onnx"
        )

        print("Piper ready")

    def speak(self, text):
        try:
            # Piper returns PCM generator (NOT AudioChunk objects you inspect)
            audio = b"".join(self.voice.synthesize(text))

            # convert PCM16 -> numpy
            audio_np = np.frombuffer(audio, dtype=np.int16)

            sd.play(audio_np, samplerate=22050)
            sd.wait()

        except Exception as e:
            print("TTS error:", e)

    def cleanup(self):
        pass
