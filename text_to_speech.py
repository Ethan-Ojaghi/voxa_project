from piper import PiperVoice
import sounddevice as sd


class TextToSpeech:

    def __init__(self):
        print("Loading Piper voice into memory...")

        self.voice = PiperVoice.load(
            "/home/voxa/piper/en_US-lessac-low.onnx"
        )

        print("Piper ready (fast mode)")

    def speak(self, text):

        try:
            audio = self.voice.synthesize(text)

            sd.play(audio.audio, audio.sample_rate)
            sd.wait()

        except Exception as e:
            print("TTS error:", e)

    def cleanup(self):
        pass
