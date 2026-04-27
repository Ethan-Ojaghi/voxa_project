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
        print('5 - Mandarin')

        op = input('Option: ')

        lang_map = {
            "1": "fra_Latn",
            "2": "ita_Latn",
            "3": "spa_Latn",
            "4": "deu_Latn",
            "5": "zho_Hans"
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
            translator = Translator(target_lang=target_lang)
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
    main()import os

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
        print('5 - Mandarin')

        op = input('Option: ')

        lang_map = {
            "1": "fra_Latn",
            "2": "ita_Latn",
            "3": "spa_Latn",
            "4": "deu_Latn",
            "5": "zho_Hans"
        }

        if op not in lang_map:
            print("Invalid option")
            continue

        target_lang = lang_map[op]

       
        if translator is None or translator.target_lang != target_lang:
            translator = Translator(target_lang=target_lang)

        audio_file = audio_recorder.record_ptt()
        if not audio_file:
            print("Recording failed")
            continue

        text = stt.transcribe(audio_file)
        if not text:
            print("No speech detected")
            continue

        translated = translator.translate(text)

        print("Translated:", translated)

        tts.speak(translated, lang="en")

        break


if __name__ == "__main__":
    main()
