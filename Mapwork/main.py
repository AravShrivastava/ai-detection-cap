import datetime
import pyttsx3
import speech_recognition as sr
import requests
import bs4
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        listener.pause_threshold = 1
        listener.energy_threshold= 300
        audio = listener.listen(source,0,4)
    try:
        print("Recognizing...")
        query = listener.recognize_google(audio, language = 'en-in')
    except Exception as e:
        print("Unable to Recognize your voice.")
        return "None"
    return query

if __name__ == "__main__":
    while True:


        query = takeCommand().lower()
        if "go to sleep" in query:
            speak("Ok , You can me call anytime")
            break

        elif "hello" in query:
            speak("Hello , how are you ?")
        elif "i am fine" in query:
            speak("that's great ")
        elif "how are you" in query:
            speak("Perfect")
        elif "thank you" in query:
            speak("you are welcome")
        elif "weather" in query:
            search = "temperature in your location"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = bs4.BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {strTime}")
        elif "what is the date" in query:
            strTime = datetime.datetime.now().strftime("%d-%m-%y")
            speak(f"the time is {strTime}")
   
        elif "open map" in query:
         t = sr.Recognizer()
         with sr.Microphone() as source1:
            speak("Please tell your location : ")
            print('listening...')
            t.adjust_for_ambient_noise(source1, duration=0.2)
            audio = t.listen(source1,0,4)
            place1 = t.recognize_google(audio)
            place1 = place1.lower()
            print("Current location : " + place1)
            speak(place1)

            sleep(2)

            speak("Please tell your destination")
            print('listening...')
            t.adjust_for_ambient_noise(source1, duration=0.2)
            audio = t.listen(source1,0,4)
            place2 = t.recognize_google(audio)
            place2 = place2.lower()
            print("Destination : "+place2)
            speak(place2)
            import map 
            map.searchplace(place2)
            map.direction()
            map.find(place1)