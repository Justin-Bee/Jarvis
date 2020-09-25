# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speech_recognition as sr
import os

#obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something")
    #r.adjust_for_ambient_noise(source)
    audio = r.record(source, duration=3)
    text = r.recognize_google(audio, language='en-US')
    text = text+".exe"
    print(text)

os.system(text)
