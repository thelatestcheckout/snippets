import pyttsx3
engine = pyttsx3.init()

"""VOLUME"""
engine.setProperty('volume', 1.0)

""" RATE/SPEED"""
engine.setProperty('rate', 180)     # setting up new voice rate

engine.say('There are several APIs available to convert text to speech in Python. One of such APIs is the Google Text to Speech API commonly known as the gTTS API. gTTS is a very easy to use tool which converts the text entered, into audio which can be saved as a mp3 file.')

engine.runAndWait()
engine.stop()
