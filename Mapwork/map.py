import pyttsx3
from googlemaps import Client
import re

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Add you API key here
map = Client(key='AIzaSyDuuebkKk-BFjb5ExduSDiBMQHn3QGyRMY')
directions = map.directions('Mount Carmel School, Baghmugalia, Bhopal', 'Kanha Fun CIty')
directions = directions[0]
i=1
for leg in directions['legs']:
    place1 = "Start Address: "+leg['start_address']
    speak(place1)
    place2 = "End Address"+leg['end_address']
    speak(place2)
    for step in leg['steps']:
        hi = step['html_instructions']
        s = "STEP {} {}".format(i ,hi)
        speak(re.sub(CLEANR, ' ', s))
        i = i+1
