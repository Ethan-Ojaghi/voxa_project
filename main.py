from translate import Translator
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech
import audio_recorder


def main():
    #main menu
    while True:
        print('Main Menu: Please chose an output language below.')
        print('1 - French')
        print('2 - Italian')
        print('3 - Spanish')
        print('4 - German')
        print('5 - Mandarin')
        op = input('Option: ')
        if op == '1':
            translator = Translator(target_lang="fra_Latn")
            output = translator.translate(input(SpeechToText.transcribe(audio_file=any)))
            TextToSpeech.speak(output)
            break
        elif op == '2':
            translator = Translator(target_lang="ita_Latn")
            output = translator.translate(input(SpeechToText.transcribe(audio_file=any)))
            TextToSpeech.speak(output)
            break
        elif op == '3':
            translator = Translator(target_lang="spa_Latn")  
            output = translator.translate(input(SpeechToText.transcribe(audio_file=any)))
            TextToSpeech.speak(output)
            break
        elif op == '4': 
            translator = Translator(target_lang="deu_Latn")
            output = translator.translate(input(SpeechToText.transcribe(audio_file=any)))
            TextToSpeech.speak(output)
            break
        elif op == '5':  
            translator = Translator(target_lang="zho_Hans")
            output = translator.translate(input(SpeechToText.transcribe(audio_file=any)))
            TextToSpeech.speak(output)
            break   
        else: 
            print('Please try again')

if __name__ == '__main__':
    main()
