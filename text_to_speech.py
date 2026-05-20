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
    
            pcm_parts = []
    
            for chunk in audio_chunks:
    
                # Case 1: already numpy-like
                if hasattr(chunk, "audio"):
                    pcm_parts.append(chunk.audio)
    
                # Case 2: raw data field
                elif hasattr(chunk, "pcm"):
                    pcm_parts.append(chunk.pcm)
    
                elif hasattr(chunk, "data"):
                    pcm_parts.append(chunk.data)
    
                # Case 3: fallback (AudioChunk object → extract buffer)
                else:
                    pcm_parts.append(np.array(chunk, dtype=np.int16))
    
            audio = np.concatenate(pcm_parts)
    
            sd.play(audio, 22050)
            sd.wait()
    
        except Exception as e:
            print("TTS error:", e)
            
    def cleanup(self):
        pass
