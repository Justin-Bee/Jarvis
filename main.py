# Jarvis - Personal Assistant
# Author - Justin Bee
# Version - 0.0.1


import speech_recognition as sr
import os
from speak import speak
import webbrowser, time
import subprocess
import time


def listen_function(source):
    audio = r.record(source, duration=3)
    try:
        user = r.recognize_google(audio, language='en-US')
        print(user)
        if "note" in user:
            speak("Opening Notepad for you.")
            os.system("notepad.exe")
        elif "text" in user:
            speak("Opening Notepad for you.")
            os.system("notepad.exe")
        elif "how are you" in user:
            speak("I am doing well, thank you for asking.")
        elif "you the man" in user:
            speak("I am a program")
        elif "Google" in user:
            speak("Opening google")
            user = user.replace("Google", "")
            webbrowser.open('www.google.com/search?q=' +user)
        elif "YouTube" in user:
            speak("Opening YouTube")
            webbrowser.open("www.youtube.com")
        elif "music" in user:
            speak("Opening spotify")
            os.system("spotify.exe")
        elif "games" in user:
            speak("Opening Steam")
            file = "C:\Program Files (x86)\Steam\Steam.exe"
            subprocess.call([file])
        elif "Jarvis say" in user:
            user = user.replace("say", "")
            speak(user)
        elif "thank you" in user:
            speak("You are most welcome.")
        elif "what time" in user:
            speak(time.ctime())
        elif "shut down" in user:
            speak("Shutting down, bye")
            exit(1)
        elif "joke" in user:
            speak("Knock knock")
        elif "who's there" in user:
            speak("I am")  #android humor
        elif "terminal" in user:
            speak("opening command prompt")
            os.system("cmd.exe")
        elif "what is your name" in user:
            speak("I am Jarvis")
        else:
            speak("I did not understand your request.")
    except:
        print("nothing was heard")


if __name__ == "__main__":

    speak("Hello, I am Jarvis. How can I help you?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            listen_function(source)
