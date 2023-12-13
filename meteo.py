import requests
from keys import METEO_KEY
import pyttsx3
# pip install SpeechRecognition
import speech_recognition as sr

def audio_a_texto():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 0.8

        
    



'''
ciudad = "Roma"
# ciudad = "Cornella de Llobregat"
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={METEO_KEY}&lang=es&units=metric"
# print(url)
info_ori = requests.get(url)

diccio_meteo = info_ori.json()
# print(diccio_meteo)

mensaje = f"La temperatura actualmente en {ciudad} es de {diccio_meteo['main']['temp']} grados"
# print(mensaje)

# pip install pyttsx3
# engine = pyttsx3.init()
# for voz in engine.getProperty('voices'):
#     print(voz)

def leer(mensaje):
    engine = pyttsx3.init()
    engine.say(mensaje)
    engine.runAndWait()


leer(mensaje)

'''