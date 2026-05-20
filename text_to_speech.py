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
            import numpy as np
            import sounddevice as sd
    
            audio_chunks = self.voice.synthesize(text)
    
            audio_list = []
    
            for chunk in audio_chunks:
                # extract raw PCM depending on format
                if hasattr(chunk, "audio"):
                    audio_list.append(chunk.audio)
                elif hasattr(chunk, "data"):
                    audio_list.append(chunk.data)
                else:
                    audio_list.append(np.frombuffer(chunk, dtype=np.int16))
    
            audio = np.concatenate(audio_list)
    
            sd.play(audio, 22050)
            sd.wait()
    
        except Exception as e:
            print("TTS error:", e)
            
    def cleanup(self):
        pass
