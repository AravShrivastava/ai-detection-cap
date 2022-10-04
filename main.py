import datetime
from tokenize import Double
import pyttsx3
import speech_recognition
import requests
import bs4
import selenium 
from selenium import webdriver
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour1 = int(datetime.datetime.now().hour1)
    if hour1>=0 and hour1<=12:
        speak("Good Morning")
    elif hour1 >12 and hour1<=18:
        speak("Good Afternoon ")

    else:
        speak("Good Evening")

    speak("Please tell me, How can I help you ?")

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greet import greetMe
            greetMe()

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
                elif "Show me the way to " in query:
                    from SearchNow import searchGoogle

                    searchGoogle(query)
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
                elif "Open Maps" in query:
                    speak("Please tell your location")
                    place1 = query
                    speak("Please tell your destination")
                    place2 = query 
                    driver = webdriver.Chrome("C://chromedriver.exe")
  
                    driver.get("https://www.google.com/maps/@23.232512,77.430784,12z")

sleep(2)

def searchplace():
    place = driver.find_element_by_class_name("tactile-searchbox-input" )
    place.send_keys(place1)
    submit= driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    submit.click()

    searchplace()

    def direction():
        sleep(6)
        direction= driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")

        direction.click()

        direction()

        def find():
            sleep(5)
            find= driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
            find.send_keys(place2)
            search_btn= driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
            search_btn.click()

            find()
