import subprocess
from urllib.request import urlopen
import json
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import time
import requests
import smtplib
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from voice_recog_func import *



class AiBasicFunctions:
    def __init__(self, query):
        self.query = query

    def aiBasicFunctions(self):
            if 'wikipedia' in self.query:
                speak("Searching...")
                query = \
                result = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            
            elif 'open youtube' in self.query:
                speak("What should I search?")
                Search_term = takeCommand().lower() # type: ignore
                speak("Here we go to Youtube\n")
                wb.open("https://www.youtube.com/results?search_query="+Search_term)
                time.sleep(5)
                
            elif 'search on google' in self.query:
                speak("What should I search?")
                Search_term = takeCommand().lower() # type: ignore
                wb.open('https://www.google.com/search?q='+Search_term)
            

            elif 'send email' in self.query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    speak("Who is the Reciever?")
                    reciept =  takeCommand().lower() # type: ignore
                    to = (reciept)
                    sendEmail(to,content) # type: ignore
                    speak(content)
                    speak("Email has been sent.")
                except Exception as e:
                    print(e)
                    speak("Unable to send the email.")

            elif 'search in chrome' in self.query:
                speak("What should I search ?")
                chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                search = takeCommand().lower() # type: ignore
                wb.get(chromepath).open_new_tab(search+'.com')
            
            #songs             
            
            #notes
            elif "write a note" in self.query:
                speak("What should i write, sir")
                note = takeCommand()
                file = open('note.txt', 'w')
                speak("Sir, Should i include date and time")
                dt = takeCommand()
                if 'yes' in dt or 'sure' in dt:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note) # type: ignore
                    speak('done')
                else:
                    file.write(note) # type: ignore
                    
            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("note.txt", "r")
                #print(file.read())
                speak(file.read()) 

            elif "weather" in self.query: 
                
                # Google Open weather website 
                # to get API of Open weather
                api_key = "open weather api"
                base_url = "http://api.openweathermap.org/data /2.5/weather?q="
                speak(" City name ")
                print("City name : ")
                city_name = takeCommand()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name # type: ignore
                response = requests.get(complete_url)
                x = response.json()
                
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                    
                else:
                    speak(" City Not Found ") 



            #news
            elif 'news' in self.query:
                
                try:

                    jsonObj = urlopen('''news api link''')
                    data = json.load(jsonObj)
                    i = 1
                    
                    speak('here are some top news from the times of india')
                    print('''=============== TOP HEADLINES ============'''+ '\n')
                    
                    for item in data['articles']:
                        
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                        
                except Exception as e:
                    print(str(e)) 


            
            #show location on map
    

            # Whatsapp Function