import speech_recognition as sr
import pyttsx3
import datetime
import os
import time
import json
import requests
import smtplib


ctime = datetime.datetime.now()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak('Welcome to our institution')
while True:
    speak("Tell me how can I help you now?")
    statement = takeCommand().lower()
    if statement == 0:
        continue

    if "good bye" in statement or "stop" in statement:
        speak('your general assistant  is shutting down')
        print('your general assistant  is shutting down')
        break

    if 'fix an appointment' in statement:
        speak('What is your name')
        uname=takeCommand()
        speak('With whom do you like to make appointment')
        name=takeCommand()
        speak('What is purpose of meeting')
        pur=takeCommand()
        speak('Ok Thank you ')
        speak('your appointment has been succesfully booked and you will be intimated with confirmation mail')
        file1 = open("Appointment.txt","w")
        file1.write("Appointment details \n")

        with open('Appointment.txt','a',encoding='utf-8') as f:
            file1.write("Name :")
            file1.write(uname)
            file1.write(" \n")
            file1.write("Appointment fixed with: ")
            file1.write(name)
            file1.write(" \n")
            file1.write("purpose of meeting: ")
            file1.write(pur)
            file1.write(" \n")
            file1.write("time: ")
            file1.write(str(ctime))
            file1.write(" \n")
            #file1.writelines(L)
            file1.close()
            
            



    elif 'account section' in statement:
        speak("please go to the ground floor and head towards right ")
        time.sleep(5)

    elif 'where is the library' in statement:
        speak("please go to first floor and take left ")
        time.sleep(5)

    elif 'take attendance' in statement:
        speak("please look into the camera ")
        import attendance
        time.sleep(5)

    elif 'dean academics' in statement:
        speak("please go to third floor ")
        speak("We have lift services . Please make use of it ")
        time.sleep(5)

    elif 'principal' in statement:
        speak("please go to ground floor ")
        speak(" head towards left, Next to main stairs ")
        time.sleep(5)