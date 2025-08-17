from googletrans import Translator
Translator = Translator()
sentece = input("Enter the sentence you want to translate: ")
to_lang = input("Enter the language you want to translate to: ")
output = Translator.translate(sentece, dest=to_lang)
print(output.text)
