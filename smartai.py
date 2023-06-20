import openai
from voice_recog_func import *
from api_secrets import API_KEY_OPENAI

openai.api_key = API_KEY_OPENAI



messages = []

class SmartAI:
    def __init__(self, query):
        self.query = query
        

    def smartAI(self):
        message = self.query 
        messages.append({"role":"user", "content": self.query})
        try:
            speak("Searching....")
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            reply = response["choices"][0]["message"]["content"] # type: ignore
            messages.append({"role":"assistant", "content": reply})
            print("\n" + reply + "\n")
            if reply:
                speak(reply)

        except Exception as e:
            print("Error:", e)

   
