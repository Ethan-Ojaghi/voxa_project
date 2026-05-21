import speech_recognition as sr
from datetime import datetime
import os
import subprocess


def beep():
    subprocess.run(
        ["aplay", "-q", "beep.wav"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def record_ptt(device_index=1):

    recognizer = sr.Recognizer()

    try:
        print("Using microphone index:", device_index)

        with sr.Microphone(device_index=device_index) as source:

            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            # =========================
            # MORE NATURAL SPEECH PAUSES
            # =========================
            recognizer.pause_threshold = 2.5
            recognizer.non_speaking_duration = 0.8

            print("Recording...")
            beep()

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=12
            )

        os.makedirs("recordings", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        audio_file = f"recordings/audio_{timestamp}.wav"

        with open(audio_file, "wb") as f:
            f.write(audio.get_wav_data())

        print(f"Audio saved to {audio_file}")

        return audio_file

    except Exception as e:
        print(f"Recording error: {e}")
        return None
