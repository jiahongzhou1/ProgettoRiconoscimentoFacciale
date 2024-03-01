# Progetto di riconoscimento vocale.
import speech_recognition as sr

recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer

with sr.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    print("Sto ascoltando...")
    audio = recognizer_instance.listen(source)
    print("Ok, sto elaborando")
try:
    text = recognizer_instance.recognize_google(audio, language="it-IT")
    print("Ecco cosa ho capito: \n", text)
except Exception as e:
    print(e)