import pyttsx3
import json
import operator
import speech_recognition as sr
import webbrowser
import os
import datetime
# import winshell
# import smtplib
# import ctypes
# import time
# import requests
# import shutil
# from bs4 import BeautifulSoup
# import win32com.client as wincl
# from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()


def nameinput():
    speak("what is your name?")
    a = takeCommand()
    speak(a)
    # speak("how can help u?")




def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning  !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon !")   
  
    else:
        speak("Good Evening !")  
  
    # a = ("what may i help you?")
    speak("I am Phoenix from Karm Marg.")
    # speak(a)


def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
     
    return query

if __name__ == '__main__':
    wish()
    takeCommand()
    nameinput()
    while True:

        query = takeCommand().lower()

        if "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop phoenix from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 