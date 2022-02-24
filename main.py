from datetime import datetime

from time import sleep, time
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import webbrowser as wb
import urllib.parse as a


curDT = datetime.now()

name = "Alex"
wakeUpList = ['wake up','launch','z']
greetings = ['hi','hello']
SocialMedia = ['instagram','youtube']



def listening ():
            while True:
                print("listening ")
                response = get_audio()
                if name.lower()   in response.lower():
                    speak("Yes Turki what would you like me to do?")
                    to_do  = get_audio()
                    job(to_do)


                elif  response.lower() in  wakeUpList:
                    speak("Yes Turki what would you like me to do?")
                    to_do  = get_audio()
                    job(to_do)

                elif "stop" in response.lower()   :
                    speak("ok shutting down")
                    quit()
                else:
                    listening()

def AI ():

        


                


                    
                    

                listening()
    
            

            


def job (ToDo):
                if "look" in ToDo.lower():
                 speak("what would you like to search for ")
                 search = get_audio()
                 base_url = "https://www.google.com/search?q="
                 final_url = base_url + a.quote(search)
                 wb.open(f'{final_url}')
                 speak("done")

                elif ("open") in ToDo.lower():
                #  search = input("what would you like me to open for you ")
                #  if ("novel" or "novels") in search.lower():
                    if ("reading") in ToDo.lower():
                     wb.open("wuxiaworld.com")
                     speak("done")


                    elif  "comic" in ToDo.lower():
                       wb.open("mangakakalot.com")
                       speak("done")

                    elif "social" in ToDo.lower():
                        social_media(ToDo)
                    
                    else:
                        speak("sorry i couldn't open that")
                        listening()


                # elif ("open" and ) in ToDo.lower():
                #      wb.open("mangakakalot.com")
                #      print("done")

                #  else:
                #      print("sorry i couldn't do that")

                # elif "social " in ToDo.lower():
                #     social_media()
                
                elif "bye" in ToDo.lower():
                    speak("bye")
                    listening()

                elif "date" in ToDo.lower():
                    TodayDate = curDT.strftime("%m/%d/%Y, %H:%M:%S")
                    speak(TodayDate)
                    
                    listening()
                elif ToDo is None:
                    speak("bye you didn't say anything")
                    listening()
                
                else:
                    speak("sorry i couldn't understand you")
                    sleep(1)
                    # speak("could you tell me what you want me to do once more ")
                    # again = get_audio()
                    # job(again)  
                listening()

def social_media (app):
            # speak("which social media app should i open for you? ")
            search = app
            for i in range(len(SocialMedia)):
                if SocialMedia[i].lower() in search.lower():
                    wb.open(f"{SocialMedia[i]}.com")
                    speak("done")
                    listening()
            speak("i couldn't open the social media app that you were looking for")
            listening()    


def speak(text):
       tts = gTTS(text=text, lang="en")
       filename = "voice.mp3"
       tts.save(filename) #saves the audio file
       playsound.playsound(filename)
       os.remove(filename)



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            # print("Exception: " + str(e))
            print("nothing was said")

    return said


AI()

