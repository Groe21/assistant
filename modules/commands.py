import webbrowser
import os
from modules.database import Database
from modules.email_utils import send_email
from modules.weather import get_weather

class CommandHandler:
    def __init__(self, assistant):
        self.assistant = assistant
        self.db = Database('assistant.db')

    def handle(self, query):
        if 'wikipedia' in query:
            self.assistant.speak('Buscando en Wikipedia...')
            # Lógica para buscar en Wikipedia
        elif 'abre youtube' in query:
            self.assistant.speak("Abriendo YouTube")
            webbrowser.open("youtube.com")
        elif 'escribe una nota' in query:
            self.assistant.speak("¿Qué debo escribir, señor?")
            note = self.assistant.take_command()
            self.db.add_note(note)
            self.assistant.speak("Nota guardada.")
        elif 'muestra la nota' in query:
            notes = self.db.get_notes()
            for note in notes:
                self.assistant.speak(note[1])
        elif 'envía un correo' in query:
            self.assistant.speak("¿Qué debo decir?")
            content = self.assistant.take_command()
            self.assistant.speak("¿A quién debo enviarlo?")
            to = self.assistant.take_command()
            send_email(to, content)
            self.assistant.speak("Correo enviado")
        elif 'clima' in query:
            self.assistant.speak("Nombre de la ciudad")
            city_name = self.assistant.take_command()
            weather = get_weather(city_name)
            self.assistant.speak(weather)
        # Otros comandos...
