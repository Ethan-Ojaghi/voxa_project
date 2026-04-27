import time
from translate import Translator

def main():
    print("Translation test mode")

    # load model ONCE and time it
    start = time.time()
    translator = Translator(target_lang="spa_Latn")
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
