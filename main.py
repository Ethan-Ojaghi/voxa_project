import os
import time 

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from translate import Translator
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech
import audio_recorder


def main():
    stt = SpeechToText()
    tts = TextToSpeech()

    translator = None  

    while True:
        print('\nMain Menu: Choose language')
        print('1 - French')
        print('2 - Italian')
        print('3 - Spanish')
        print('4 - German')

        op = input('Option: ')

        lang_map = {
            "1": "Helsinki-NLP/opus-mt-en-fr",
            "2": "Helsinki-NLP/opus-mt-en-it",
            "3": "Helsinki-NLP/opus-mt-en-es",
            "4": "Helsinki-NLP/opus-mt-en-de"
        }

        if op not in lang_map:
            print("Invalid option")
            continue

        target_lang = lang_map[op]

        # =========================
        # TRANSLATOR INIT TIMER
        # =========================
        if translator is None or translator.target_lang != target_lang:
            start = time.time()
            translator = Translator(model_name=target_lang)
            print(f"MODEL LOAD TIME: {time.time() - start:.2f}s")

        # =========================
        # AUDIO RECORD
        # =========================
        start = time.time()
        audio_file = audio_recorder.record_ptt()
        print(f"RECORDING TIME: {time.time() - start:.2f}s")

        if not audio_file:
            print("Recording failed")
            continue

        # =========================
        # STT TIMER
        # =========================
        start = time.time()
        text = stt.transcribe(audio_file)
        print(f"STT TIME: {time.time() - start:.2f}s")

        if not text:
            print("No speech detected")
            continue

        # =========================
        # TRANSLATION TIMER
        # =========================
        start = time.time()
        translated = translator.translate(text)
        print(f"TRANSLATION TIME: {time.time() - start:.2f}s")

        print("Translated:", translated)

        # =========================
        # TTS TIMER
        # =========================
        start = time.time()
        tts.speak(translated, lang="en")
        print(f"TTS TIME: {time.time() - start:.2f}s")

        break


if __name__ == "__main__":
    main()
