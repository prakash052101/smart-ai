import pyttsx3
import speech_recognition as sr

#initializing speech engine
engine = pyttsx3.init()

def speak(word):
    engine.setProperty('rate', 190)
    engine.setProperty('voulme', 1.8)

    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)

    engine.say(str(word))
    engine.runAndWait()



def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        #r.pause_threshold = 1
        #audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        speak("Unable to Recognize your voice.") 
        return "None"
     
    return query