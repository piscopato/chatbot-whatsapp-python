import requests
from deep_translator import GoogleTranslator

def conselho():
    tradutor = GoogleTranslator(source='en', target='pt')
    conselhor = requests.get('https://api.adviceslip.com/advice')
    conselho = conselhor.json()['slip']['advice']
    conselho_br = tradutor.translate(conselho)
    return (conselho_br)

print(conselho())
