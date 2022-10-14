# Import the required module for text
# to speech conversion
import pyttsx3
import yolo_with_opencv

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

# say method on the engine that passing input text to be spoken
engine.say(text+f", Distance: {round(yolo_with_opencv.Distance/12,2)} ft")

# run and wait method, it processes the voice commands.
engine.runAndWait()
