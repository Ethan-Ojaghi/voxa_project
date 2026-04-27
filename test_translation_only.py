import time
from translate import Translator

def main():
    print("Translation test mode")

    # Pick OPUS-MT model (Spanish example)
    model_name = "Helsinki-NLP/opus-mt-en-es"

    # load model ONCE and time it
    start = time.time()
    translator = Translator(model_name=model_name)
    print(f"MODEL LOAD TIME: {time.time() - start:.2f}s\n")

    while True:
        text = input("Enter text (or 'exit'): ")

        if text.lower() == "exit":
            break

        # time translation only
        start = time.time()
        result = translator.translate(text)

        print(f"\nTranslated: {result}")
        print(f"TRANSLATION TIME: {time.time() - start:.2f}s\n")


if __name__ == "__main__":
    main()
