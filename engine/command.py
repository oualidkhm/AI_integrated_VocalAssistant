import eel
import pyttsx3
import speech_recognition as sr
import time


@eel.expose
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


@eel.expose
def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        eel.DisplayMessage('And Here is your answer : ....')

        time.sleep(2)
       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
            eel.senderText("")

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
            eel.senderText("")
        
        else: 
            eel.DisplayMessage('And your answer is : ....')
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error !")
    eel.ShowHood()