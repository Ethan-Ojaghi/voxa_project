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
            audio_chunks = self.voice.synthesize(text)
    
            all_audio = b"".join(audio_chunks)
            audio = np.frombuffer(all_audio, dtype=np.int16)
    
            import sounddevice as sd
            sd.play(audio, 22050)
            sd.wait()
    
        except Exception as e:
            print("TTS error:", e)
            
    def cleanup(self):
        pass
