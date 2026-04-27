import os

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

        # 1. Record audio
        audio_file = audio_recorder.record_ptt()
        if not audio_file:
            print("Recording failed")
            continue

        # 2. Speech to text
        text = stt.transcribe(audio_file)
        if not text:
            print("No speech detected")
            continue

        # 3. Translate
        translator = Translator(target_lang=target_lang)
        translated = translator.translate(text)

        print("Translated:", translated)

        # 4. Speak
        tts.speak(translated, lang="en")

        break


if __name__ == "__main__":
    main()
