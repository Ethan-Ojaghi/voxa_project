import subprocess


class TextToSpeech:

    def __init__(self):
        print("Using eSpeak TTS (fast mode)")

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

            subprocess.run(
                [
                    "espeak-ng",
                    "-v", voice,
                    "-s", "155",   # slower = clearer (default ~175–200)
                    text
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        except Exception as e:
            print("TTS error:", e)

    def cleanup(self):
        pass
