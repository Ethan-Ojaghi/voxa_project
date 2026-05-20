from piper import PiperVoice
import wave
import sounddevice as sd
import numpy as np
import tempfile


class TextToSpeech:

    def __init__(self):
        print("Loading Piper voice...")
        self.voice = PiperVoice.load(
            "/home/voxa/piper/en_US-lessac-low.onnx"
        )
        print("Piper ready")

    def speak(self, text):
        try:
            # create temp wav file
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                wav_path = f.name

            # let Piper handle EVERYTHING
            with wave.open(wav_path, "wb") as wav_file:
                self.voice.synthesize_wav(text, wav_file)

            # play result
            data, samplerate = sf.read(wav_path, dtype="int16")
            sd.play(data, samplerate)
            sd.wait()

        except Exception as e:
            print("TTS error:", e)

    def cleanup(self):
        pass
