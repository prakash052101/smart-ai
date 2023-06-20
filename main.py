from voice_recog_func import *
from smartai import *
from ai_basic_function import *

import os



while True:
    print("Listening....")
    #speak("Listening....")
    query = takeCommand().lower() # type: ignore
    if query == 'quit' or query == 'exit':
        break
    
    aiBasic = AiBasicFunctions(query)
    aiBasic.aiBasicFunctions()

    if 'jarvis' in query:
        speak('Hello, Boss, Welcome Back!')
        while True:
            clear = lambda: os.system('cls') 
            print("Listening....")
            query_ai = takeCommand().lower() # type: ignore
            if query_ai == 'quit' or query_ai == 'exit':
                break
            ai = SmartAI(query_ai)
            ai.smartAI()