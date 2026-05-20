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
    lang_code = None

    lang_map = {
        "1": "Helsinki-NLP/opus-mt-en-fr",
        "2": "Helsinki-NLP/opus-mt-en-it",
        "3": "Helsinki-NLP/opus-mt-en-es",
        "4": "Helsinki-NLP/opus-mt-en-de"
    }

    lang_code_map = {
        "Helsinki-NLP/opus-mt-en-fr": "fr",
        "Helsinki-NLP/opus-mt-en-it": "it",
        "Helsinki-NLP/opus-mt-en-es": "es",
        "Helsinki-NLP/opus-mt-en-de": "de",
    }

    try:

        while True:

            # =========================
            # LANGUAGE MENU
            # =========================
            if translator is None:
                print("\nMain Menu: Choose language")
                print("1 - French")
                print("2 - Italian")
                print("3 - Spanish")
                print("4 - German")
                print("Type 'exit' to quit")

                op = input("Option: ").strip().lower()

                if op == "exit":
                    print("Exiting VOXA")
                    break

                if op not in lang_map:
                    print("Invalid option")
                    continue

                target_lang = lang_map[op]
                lang_code = lang_code_map[target_lang]

                start = time.time()
                translator = Translator(model_name=target_lang)
                print(f"MODEL LOAD TIME: {time.time() - start:.2f}s")

            # =========================
            # CONVERSATION LOOP
            # =========================
            print("\nChoose Option (ENTER = start | 1 = change language | 2 = quit)")
            cont = input("> ").strip().lower()

            if cont == "2":
                print("Exiting VOXA")
                break

            if cont == "1":
                translator = None
                continue

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
            # STT
            # =========================
            start = time.time()
            text = stt.transcribe(audio_file)
            print(f"STT TIME: {time.time() - start:.2f}s")

            if not text:
                print("No speech detected")
                continue

            print("You said:", text)

            # =========================
            # TRANSLATION
            # =========================
            start = time.time()
            translated = translator.translate(text)
            print(f"TRANSLATION TIME: {time.time() - start:.2f}s")

            print("Translated:", translated)

            # =========================
            # TTS
            # =========================
            start = time.time()
            tts.speak(translated)
            print(f"TTS TIME: {time.time() - start:.2f}s")

    finally:
        tts.cleanup()


if __name__ == "__main__":
    main()
