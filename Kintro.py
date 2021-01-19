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


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning  !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon !")   
  
    else:
        speak("Good Evening !")  
  
    a = ("what may i help you?")
    speak("I am Phoenix from Karm Marg.")
    speak(a)


if __name__ == '__main__':
    wish()