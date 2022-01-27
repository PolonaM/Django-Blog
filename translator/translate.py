from googletrans import Translator

def translate(text):
    try:
        translator = Translator()
        translation = translator.translate(text=text, dest='sl')
        return translation.text
    except:
        pass

