import pyttsx3
import speech_recognition as sr
import os
import datetime
from modules.commands import CommandHandler
from modules.database import Database

class Assistant:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.db = Database('assistant.db')
        self.command_handler = CommandHandler(self)
        self.assistant_name = "Jarvis"
        
    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def wish_me(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak("¡Buenos días!")
        elif 12 <= hour < 18:
            self.speak("¡Buenas tardes!") 
        else:
            self.speak("¡Buenas noches!") 
        self.speak(f"Hola Emilio Soy tu asistente {self.assistant_name}. ¿Cómo puedo ayudarte?")

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Escuchando...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Reconociendo...")
            query = r.recognize_google(audio, language='es-ES')
            print(f"El usuario dijo: {query}\n")
        except Exception as e:
            print(e)
            print("No se pudo reconocer tu voz.")
            return "None"
        return query.lower()

    def start(self):
        self.wish_me()
        while True:
            query = self.take_command()
            if query != "None":
                self.command_handler.handle(query)
