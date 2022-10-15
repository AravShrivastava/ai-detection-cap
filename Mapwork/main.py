import datetime
import pyttsx3
import speech_recognition as sr
import requests
import bs4
from time import sleep

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    with sr.Microphone() as source:
        print('listening...')
        listener.pause_threshold = 1
        voice = listener.listen(source)
    try:
        print("Recognizing...")
        query = listener.recognize_google(voice, language = 'en-in')
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        speak("Let's Start!!!")
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
            speak("Please tell your location : ")
            place1 = takeCommand().lower()
            print("Current location : " + place1)
            speak(place1)
            sleep(3)
            speak("Please tell your destination")
            place2 = takeCommand().lower()
            print("Destination : "+place2)
            speak(place2)
            import map as m
            m.searchplace(place2)
            m.direction()
            m.find(place1)