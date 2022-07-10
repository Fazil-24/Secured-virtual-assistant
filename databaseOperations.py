import pymongo
from bson import ObjectId
import speech_recognition as sr
import pyttsx3
import json
import os
import gridfs


# CONNECT TO DATABASE
connection = pymongo.MongoClient("localhost", 27017)

# CREATE DATABASE
database = connection['my_database']
# CREATE COLLECTION
collection = database['my_collection']
print("Database connected")


def insert_data(data):
    """
    Insert new data or document in collection
    :param data:
    :return:
    """
    document = collection.insert_one(data)
    return document.inserted_id

def count():
    """
    Insert new data or document in collection
    :param data:
    :return:
    """
    document = collection.count_documents({})
    return document


def update_or_create(document_id, data):
    """
    This will create new document in collection
    IF same document ID exist then update the data
    :param document_id:
    :param data:
    :return:
    """
    # TO AVOID DUPLICATES - THIS WILL CREATE NEW DOCUMENT IF SAME ID NOT EXIST
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
    return document.acknowledged


def get_single_data(document_id):
    """
    get document data by document ID
    :param document_id:
    :return:
    """
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data


def get_multiple_data():
    """
    get document data by document ID
    :return:
    """
    data = collection.find()
    return list(data)



def update_existing(document_id, data):
    """
    Update existing document data by document ID
    :param document_id:
    :param data:
    :return:
    """
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data})
    return document.acknowledged


def remove_data(document_id):
    document = collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged

#read image
"""
filename = "10.jpg"
datafile = open(filename,"rb")
thedata = datafile.read()
#create a new gridfs object
fs = gridfs.GridFS(database)
#store the data
stored=fs.put(thedata,filename="testimage")
#To retrive what was just stored
outputdata=fs.get(stored).read()
"""
#read audio
"""
filename = "3.wav"
datafile = open(filename,"rb")
thedata = datafile.read()
#create a new gridfs object
fs = gridfs.GridFS(database)
#store the data
stored=fs.put(thedata,filename="testaudio")
#To retrive what was just stored
outputdata=fs.get(stored).read()
"""


# CLOSE DATABASE
connection.close()



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement



speak("What is your full name") 
da1=takeCommand()
speak("What is your age") 
da2=takeCommand()
speak("Which is your city ") 
da3=takeCommand()
speak("What is your phone number ") 
da4=takeCommand()
speak("What is your Date Of Birth") 
da5=takeCommand()



"""da1="ben"
da2="20"
da3="chennai"
da4="9791462614"
da5="2000-24-05"""

i=count()
j=i+1
daa1={'_id':j,'Name':da1,'Age':da2,'City':da3,'Phno':da4,'DOB':da5}
insert_data(daa1)

"""da1="mfazil2409@gmail.com"
da2="alman.alu313@gmail.com"
da3="fazil2000"
daa1={'email':da1,'name':"Fazil"}
daa2={'email':da2,'name':"Azhar"}
insert_data(daa1)
insert_data(daa2)"""

#exec(open('voice_new_user.py').read())



