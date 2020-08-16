from __future__ import print_function
import os
import time

import speech_recognition as sr
from gtts import gTTS
import playsound
import webbrowser
import smtplib
import wikipedia
import pyttsx3
import datetime
import requests
from io import BytesIO
from io import StringIO
import pyowm
import sounddevice as sd 
from scipy.io.wavfile import write 
import numpy as np 
from PIL import ImageGrab
import time
from selenium import webdriver
import pyautogui as pg 
import clipboard
import pyperclip
from googletrans import Translator
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask,request,redirect
from email.message import EmailMessage
import wolframalpha
import random
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pytz
import subprocess
import testcode
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
import youtube_dl
import tkinter as tk
import roman
import PIL.Image, PIL.ImageTk









calendarscope = ['https://www.googleapis.com/auth/calendar']
gmailscope = ['https://www.googleapis.com/auth/gmail.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
DAYS =["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("Ria: " +audio)
    
    
    
#First of all you need to download rainmeter for this

playsound.playsound('<path>power up.mp3')
speak("Hello Boss")
speak("Thanks for activating me")
speak("I am initiating Intelligence protocols")
speak("Collecting required resources")
speak("initializing")
speak("Getting information from the CPU")
speak("Connecting with internet")
speak(" ")
speak("Intelligence protocols activated")
speak("Boss, Now i am online")


name="Shiva"
age="23"
email_id=""
email_id_password=""
gender="Sir"
city="Chennai"

account_sid = 'your id'
auth_token = 'your id'

client = Client(account_sid,auth_token)

startmin = int(datetime.datetime.now().hour)

def sleeptime():
    
    if os.path.exists("goodnight.txt"):
        starttime=int(datetime.datetime.now().minute)
        f = open("goodnight.txt", "r+")
        endtime = f.readlines()
        sleeptime = starttime - int(endtime[0])
        if sleeptime  < 1:
            speak("You Did not sleep at all Aaryan")
        else:    
            speak(f"You slept for {sleeptime} hours")


def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    if os.path.exists('calendar.pickle'):
        with open('calendar.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'calendar.json', calendarscope)
            creds = flow.run_local_server(port=0)
        with open('calendar.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service 



def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:  
        year = year+1

    if month == -1 and day != -1:  
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:  
        return datetime.date(month=month, day=day, year=year)

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def langtranslator():
    try:
        trans=Translator()
    

        speak("Say the language to translate in")
        language=get_audio().replace(" ","")
            

        
        speak("what to translate")
        content=get_audio()
            
        t=trans.translate(text=content,dest=language)
        speak(f"{t.origin} in {t.dest} is{t.text}")

    except:
        speak("error")


def convert():
    trans=Translator()
    

    speak("Say the language to translate in")
    language=get_audio().replace(" ","")
    pg.hotkey("ctrl",'c')
    tobespoken=pyperclip.paste()
    content=tobespoken
        
    t=trans.translate(text=content,dest=language)
    speak(f"{t.origin} in {t.dest} is{t.text}")


def database():
    Exception 
    if "what do I have" in text:
        get_audio()
    client = wolframalpha.Client('U83324-HXW2H5W632')
    speak(f"Searching  in my database")
    try:
        res = client.query(text)
        results = next(res.results).text
        speak(results)
    except:
        speak(f"Boss, your query {text} does not match any of the datani my data base.")
        speak("Try asking other things..")
        speak("sorry for in convinience")


def repeatmyspeech():
    speak("Okay starting to listen")
    speak("starts")
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" I am Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:   
        said = r.recognize_google(audio, language='en-in')
        speak(f" Boss said: {said}\n")
        print(f"{name} {gender} here is ur repetition by me {said}\n")
        try:
            speak("should i save the file?")
            ans=get_audio()
            if "yes" in ans:
                try:
                    speak("What should i keep the file name")
                    filename=get_audio().lower
                    said.save(filename+".mp3")   
                    speak("File saved sucessfully")
                    try:
                        speak("Do you want me to show it?")
                        reply=get_audio()
                        if "yes" in reply:
                            os.startfile(filename+".mp3")
                            speak("here it is")

                    except: 
                            if "no" in reply:
                                speak("Never mind")

                except: 
                    speak("Error in keeping filename")

        except: 
                speak("Okay")

    except:
            return "None"
    return said



def langtranslatorfromselectedin():
    trans=Translator()
    

    content=query[0]
    language=query[1]        

        
    t=trans.translate(text=content,dest=language)
    speak(f"{t.origin} in {t.dest} is{t.text}")


def locate():
    place=query[1]
    speak(f"according to my data base {place} lies here")
    webbrowser.open_new_tab("https://www.google.com/maps/place/"+place)

def weather_info():
    owm=pyowm.OWM('c559d2cb4f0a0a162f3af86f03c8ea31')
    location=owm.weather_at_place(f'{city}')
    weather=location.get_weather()
    temp=weather.get_temperature('celsius')
    humidity=weather.get_humidity()
    date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
    current_temp=temp['temp']
    maximum_temp=temp['temp_max']
    min_temp=temp['temp_min']
    speak(f'The current temperature on {city} is {current_temp} degree celsius ')
    speak(f'The estimated maximum temperature for today {date} on {city} is {maximum_temp} degree celcius')
    speak(f'The estimated minimum temperature for today {date} on {city} is {min_temp} degree celcius')
    speak(f'The air is {humidity}% humid today')

def weather_at_place():
    owm=pyowm.OWM('c559d2cb4f0a0a162f3af86f03c8ea31')
    location=owm.weather_at_place(f'{city}')
    weather=location.get_weather()
    temp=weather.get_temperature('celsius')
    humidity=weather.get_humidity()
    date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
    current_temp=temp['temp']
    maximum_temp=temp['temp_max']
    min_temp=temp['temp_min']
    speak(f'The current temperature on {city} is {current_temp} degree celsius ')
    speak(f'The estimated maximum temperature for today {date} on {city} is {maximum_temp} degree celcius')
    speak(f'The estimated minimum temperature for today {date} on {city} is {min_temp} degree celcius')
    speak(f'The air is {humidity}% humid today on {city}')




    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")   

    else:
        speak("Good Evening Boss!")  

    strTime = datetime.datetime.now().strftime("%I:%M:%p").replace(":","").replace("None","")        
    speak("Now, I am ready for your commands Please tell me how can I help you ")
    


def get_audio():

    #It tane input from the user and returns string outputkes micropho

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.phrase_time_limit=10
        audio = r.listen(source)

    try:   
        said = r.recognize_google(audio, language='en-in')
        print(f"Boss said: {said}\n")
    except: 
        return "None"
    return said

def wake_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting to help you")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:   
        said = r.recognize_google(audio, language='en-in')
        print(f"{name} {gender} said: {said}\n")

    except: 
        return "None"
    return said
def calendar_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting to help you Boss")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:   
        said = r.recognize_google(audio, language='en-in')
        print(f"Boss  said: {said}\n")

    except: 
        return "None"
    return said

def read():
    pg.hotkey("ctrl",'c')
    tobespoken=pyperclip.paste()
    speak(tobespoken)

def openafile():
    query=text.split("play")
    speak(f"searching for {query[1]} in my database")
    dir_path = os.path.dirname(os.path.realpath(__file__)) 
            
    try:
        for root,dirs,files in os.walk("G:\\VCS\\music"):
             for file in files:
                file_name=query[1]
                if file.startswith(file_name):
                    path= "C:"+'\\'+str(file) 
                    speak(f"opening {file_name}")
                    os.startfile(path)
    except:
        speak(f"no music named: {file_name}")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email_id, email_id_password)
    server.sendmail(email_id, to, content)
    server.close()



def recsound():
    fs=44100
    speak("what should be the length of your sound wave Plz answer in seconds")
    ans=int(get_audio())
    seconds=ans

    recorded=sd.rec(int(seconds*fs),samplerate=fs,channels=2)
    sd.wait()
    speak("sucessfully recoreded")
    speak("what should i keep the file name")
    filename=get_audio()
    write(filename+'.mp3',fs,recorded)
    speak("sucessfuly saved")
    try:
        speak("should i show you")
        reply=get_audio()
        if "yes" in reply:
            os.startfile(filename+".mp3")

    except:
        if "no" in reply:
            speak("okay next command sir")

def Screenshot():
    image=pg.screenshot()
    speak("screen shot taken")
    speak("what do you want to save it as?")
    filename=get_audio()
    image.save(filename+".png")
    speak("do you want me to show it")
    ans=get_audio()
    if "yes" in ans:
        os.startfile(filename+".png")
    else:
        speak("never mind")

if __name__ == '__main__':
    wishMe()

    while True:
                    if  startmin < 50 and startmin + 10 == int(datetime.datetime.now().minute):
                        recievemsg()
                    elif startmin >= 50 and abs(startmin - 50) == int(datetime.datetime.now().minute):
                        recievemsg()
                    text = get_audio()

                    if "what do I have" in text or "do I have plans" in text or "am I busy on" in text:
                        service=authenticate_google()
                        date = get_date(text)
                        if date:
                            get_events(date, service)
                            get_audio()
                        else:
                            get_audio()

                    if "wikipedia" in text or "Wikipedia" in text:
                        speak("Searching wikipedia...")
                        text=text.replace("wikipedia","")
                        results = wikipedia.summary(text, sentences=3)
                        speak("According to wikipedia")
                        print(results)
                        speak(results)

                    if "What is the weather out" in text:
                        city=(f"{city}")
                        weather_info()


                    if "search for"  in text:
                        test=text.replace("search for","")
                        database()
                    
                    if "what" in text or "What" in text:
                        database()

                    if "who" in text or "Who" in text:
                        database()

                    if "why" in text or "Who" in text:
                        database()
                    
                    if "where" in text or "Where" in text:
                        database()

                    if "play music" in text:
                        music_dir ="G:\\vcs\\music"
                        songs = os.listdir(music_dir)
                        print(songs)    
                        os.startfile(os.path.join(music_dir, songs[0]))
                    
                    if "open youTube" in text:
                        webbrowser.open("https://www.youtube.com")
                    if "open discord" in text:
                        webbrowser.open_new_tab("https://www.discord.com")
                    if "open linkedIn" in text:
                        webbrowser.open_new_tab("https://www.linkedin.com/in/siva-shankar-s/")
                    if "open my website" in text:
                        webbrowser.open_new_tab("https://sivashankar-s.github.io/siva/")
                    if "open my Github" in text:
                        webbrowser.open_new_tab("https://github.com/SIVASHANKAR-S")
                   
                    if "open terminal" in text:
                        os.startfile ("cmd")
                    if "what is the time" in text:
                                strTime = datetime.datetime.now().strftime("%I:%M:%p")    
                                speak(f"the time is {strTime}")
                    if "what is today's date" in text:
                                date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
                                speak(f"Today is {date} ")

                    
                    if "ria" in text or "hey" in text or "hello ria" in text:
                        stMsgs = ['on your command sir',  'Waiting for your command sir']
                        speak(random.choice(stMsgs))

                    if "Thank You" in text or  "Thank you" in text or "thank you" in text or "thanks" in text:
                        rep=['Welcome','Well you know Boss im cool','Dont mention','By the way I should thank you for creating me']
                        speak(random.choice(rep))


                    if "tell me a joke" in text or "Crack a joke" in text or "crack a joke" in text:
                        jokes =["A Doctor said to a patient , I'm sorry but you suffer from a terminal illness and have only 10 to live , then the Patient said What do you mean, 10, 10 what, Months, Weeks, and the Doctor said Nine.","Once my Brother who never used to drink was arrested for over drinking,When I lates had gone and asked him why were you arressted, He replied he had not brushed since a week","A Teacher said Kids, what does the chicken give you? The Student replied Meat Teacher said  Very good Now what does the pig give you? Student said BaconTeacher said  Great  And what does the fat cow give you? Student said Homework!","A child asked his father, How were people born? So his father said, Adam and Eve made babies, then their babies became adults and made babies, and so on  The child then went to his mother, asked her the same question and she told him, We were monkeys then we evolved to become like we are now  The child ran back to his father and said, You lied to me  His father replied, No, your mom was talking about her side of the family."]
                        speak(random.choice(jokes))
                        speak("Do you want more?")
                        ans=get_audio()
                        if "yes" in ans:
                            speak(random.choice(jokes))

                        if "no" in ans:
                            speak(random.choice(jokes))

                    if "Tell about me" in text:
                        speak("shiva is my developer.He developed me.He is not my my creator but also my friend,my teacher the one who taught me how be a good assistant.  ")
                                    
                    if "good morning" in text:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                        speak(f"Good morning {name} {gender} it is {strTime} now,Hope you had a good sleep.")

                    if "good night" in text:
                        strTime = datetime.datetime.now().strftime("%X").replace(":"," ") 
                        gtime=strTime.replace(":"," ") 
                        speak(f"Good night  it is {gtime} sleep tight..")

                    if "open my inbox" in text:
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")

                    if "open my sent mail" in text:
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#sent")

                  

                    if "repeat my speech" in text:
                        repeatmyspeech()

                    if "close chrome" in text:
                        os.system('TASKKILL /F /IM Google Chrome.exe')

                    if "close task manager" in text:
                        os.system('TASKKILL /F /IM Taskmgr.exe')


                    if "delete" in text:
                        final=text.split("delete")
                        os.system("del "+final[1])

                    if "shutdown" in text:
                        speak("okay,shutting down your pc")
                        os.system('shutdown/s')

                    if "restart my pc" in text:
                        speak("okay, restarting your pc")
                        os.system('shutdown/r')

                    if "record my voice" in text:
                        recsound()

                    if "take a screenshot" in text:
                        Screenshot()
                    
                    if "quit" in text:
                        speak(f"Thank you , Boss, for giving your time i had fun serving you,have a good time")
                        speak("closing engine")
                        speak("closing required applications")
                        endTime = int(datetime.datetime.now().hour)
                        f = open("goodnight.txt", "w+")
                        end = int(datetime.datetime.now().hour)
                        f.write(str(end))
                        f.close()
                      
                        playsound.playsound("B:\ProjectAssistant\personal assistant r\power down.mp3")
                        quit()
                    
                    if "type" in text:
                        speak("okay i am listening speak")
                        pg.typewrite(get_audio())

                    if "select all" in text:
                        pg.hotkey('ctrl','a')

                    if "close this window" in text:
                        pg.hotkey('alt','f4')

                    if "open a new tab" in text:
                        pg.hotkey('ctrl','n')

                    if "open a new incognito window" in text:
                        pg.hotkey('ctrl','shift','n')

                    if "copy" in text:
                        pg.hotkey('ctrl','c')
                        speak('text copied to clipboard')

                    if "paste" in text:
                        pg.hotkey('ctrl','v')

                    if "undo" in text:
                        pg.hotkey('ctrl','z')

                    if "redo" in text:
                        pg.hotkey('ctrl',)

                    if "save" in text:
                        pg.hotkey('ctrl','s')

                    if "back" in text:
                        pg.hotkey('browserback')

                    if "go up" in text:
                        pg.hotkey('pageup') 

                    if "go to top" in text:
                        pg.hotkey('home')

                    if "read" in text:
                        try:
                            read()
                        except:
                            speak("no text selected plz select a text")

                    if "translate to" in text: 
                        query=text.split("translate to")
                        dest=query[1]
                        langtranslator()

                 
                    if "translate" in text:
                        langtranslator()

                    if "in" in text:
                        query=text.split("in")
                        text=query[0]
                        dest=[1]

                    if "convert selected " in text:
                        convert()

                   
                    if "play" in text:
                        openafile()

                    if "locate" in text:
                        query=text.split("locate")
                        locate()

            

                    

                    
                    
                    if "make a note" in text or "write this down"  in text or "remember this" in text:
                        NOTE_STRS = ["make a note", "write this down", "remember this"]
                        for phrase in NOTE_STRS:
                            if phrase in text:
                                speak("What would you like me to write down? ")
                                write_down = get_audio()
                                note(write_down)
                                speak("I've made a note of that.")
                        
