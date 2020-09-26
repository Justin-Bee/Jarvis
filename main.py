# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speech_recognition as sr
import os
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audioString):
    print(audioString)
    engine.say(audioString)
    engine.runAndWait()


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
        elif "Chrome" in user:
            os.system("chrome-browser")
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
