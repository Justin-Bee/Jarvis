import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audioString):
    print(audioString)
    engine.say(audioString)
    engine.runAndWait()
