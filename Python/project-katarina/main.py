import speech_recognition as sr
import time
import pyttsx3
import os
# import logging
import keyboard
import wikipedia

# query = ("wikipedia", "what is jbl speaker?")
# results = wikipedia.summary(query, sentences=3)
# print(results)

# configuration
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 140)
engine.setProperty('voice', voices[1].id)
# logging.basicConfig(format='%(levelname)s (%(asctime)s): %(message)s',
#                     datefmt='%d/%m/%Y %I:%M %p',
#                     level=logging.DEBUG)

# logging.info("System Initializing")
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak: ")
    audio = r.listen(source)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def FileManager():
    feedbackVoice = speak("opening file manager")
    engine.runAndWait()
    print(feedback)
    print("success")
    os.startfile("C:/Users/xxamujrc/Desktop")
    return feedbackVoice


def Search():
    feedbackVoice = speak("opening Microsoft Edge")
    print(feedback)
    print("success")
    os.startfile(
        "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
    return feedbackVoice

def searchQuery():
    feedbackSearch = r.recognize_google(audio).lower().strip()

try:
    # print("you said " + r.recognize_google(audio))
    feedback = r.recognize_google(audio).lower().strip()
    time.sleep(2)
    if "file manager" in feedback:
        FileManager()
    elif "microsoft edge" in feedback:
        Search()
        feedback_search = r.recognize_google(audio)
        time.sleep(2)
        type = "google.com"
        keyboard.write(type)
        keyboard.press_and_release('enter')

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))
