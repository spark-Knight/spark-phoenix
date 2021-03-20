import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import sys
import time
import os
import os.path
import requests
import cv2
from requests import get
# import pywhatkit as kit 
import smtplib #pip install secure-smtplib
import pyjokes
import pyautogui
import pyPDF2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from operator


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    pt = time.strftime("%I:%M %p")

    if hour>= 0 and hour<12:
        speak("Good Morning Sir !,its {pt}")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !,its {pt}")   
    else:
        speak("Good Evening Sir !,its {pt}")  
  speak("""i am jarvis sir. i'm your assistant.
   please teel me how may i help you""")

#to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('siddhu4718k@gmail.com', 'matkewala')
    server.sendmail('siddhu4718k@gmail.com', to, content)
    server.close()

def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=dd99e5301ef942e0a2748194efc4ad40"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")    