import subprocess
import unicodedata

text = unicodedata.normalize("NFKD", text)
text = text.encode("ascii", "ignore").decode("ascii")


class TextToSpeech:

    def __init__(self):
        print("Using eSpeak TTS (balanced mode)")

    def speak(self, text, lang="en"):

        try:

            lang_map = {
                "en": "en",
                "fr": "fr",
                "it": "it",
                "es": "es",
                "de": "de"
            }

            voice = lang_map.get(lang, "en")

            # ---- IMPROVE CLARITY ----
            text = text.strip() + "."

            # split long sentences for clarity
            chunks = text.split(".")

            for chunk in chunks:
                chunk = chunk.strip()
                if not chunk:
                    continue

                subprocess.run([
                    "espeak-ng",
                    "-v", voice,
                    "-s", "145",   # speed tuning
                    chunk
                ])

        except Exception as e:
            print("TTS error:", e)

    def cleanup(self):
        pass
