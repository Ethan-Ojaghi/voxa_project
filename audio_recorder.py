import speech_recognition as sr
from datetime import datetime
import os


def record_ptt(device_index=1):
    """Record audio from microphone and save to a file."""
    recognizer = sr.Recognizer()

    try:
        # 👇 FORCE correct mic here
        with sr.Microphone(device_index=device_index) as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Recording...")
            audio = recognizer.listen(source, timeout=10)

        os.makedirs("recordings", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        audio_file = f"recordings/audio_{timestamp}.wav"

        with open(audio_file, "wb") as f:
            f.write(audio.get_wav_data())

        print(f"Audio saved to {audio_file}")
        return audio_file

    except sr.UnknownValueError:
        print("Audio recognition error: Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Audio recording error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error during recording: {e}")
        return None
