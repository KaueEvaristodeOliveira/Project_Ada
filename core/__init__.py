from cgitb import text
import datetime
from os import uname
import pyaudio
import json
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

class SystemInfo:
    def __init__y(self):
        pass
    
    def get_time():
        now = datetime.datetime.now()
        answer = 'Agora são {} horas e {} minutos.'.format(now.hour,now.minute)
        return answer
    
    def whoIm():
        answer = 'Eu sou Ada, a sua assistente pessoal'
        return answer
    
    def username():
        speak("Como devo-lhe chamar")
        uname = takeCommand()
        speak("Bem-vindo")
        speak(uname)
        columns = shutil.get_terminal_size().columns
