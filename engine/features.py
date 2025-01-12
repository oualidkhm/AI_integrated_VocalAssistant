import eel
import os
import re
import sqlite3
import struct
import subprocess
import time
import webbrowser
from playsound import playsound
import eel
import pyaudio
import pyautogui
from engine.command import speak
import pywhatkit as kit
import ollama
from engine.config import ASSISTANT_NAME
#Playing assiatnt sound function
#import pywhatkit as kit
import pvporcupine

from engine.helper import extract_yt_term
from hugchat import hugchat

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

@eel.expose()
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT path FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

       
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

@eel.expose
# chat bot 
def chatBot(query):
    user_input = query.lower()
    response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": user_input+"P.s: keep answers short",
        },
    ],
)
    print(response["message"]["content"])
    speak(response["message"]["content"])