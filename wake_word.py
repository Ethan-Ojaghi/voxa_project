# wake_word.py

import speech_recognition as sr


def listen_for_wake_word():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio).lower()

        return "voxa" in text

    except Exception:
        return False
