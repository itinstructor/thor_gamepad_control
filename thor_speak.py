"""
    Name: thor_speak.py
    Author:
    Created:
    Purpose: Render text into speech
    This library has many modules with which you can try
    changing the voice, volume, and speed rate of the audio.
    https://pypi.org/project/pyttsx3/
    https://pyttsx3.readthedocs.io/en/latest/
"""
# Linux:   pip3 install pyttsx3
# Windows: pip install pyttsx3
import pyttsx3
from time import sleep, strftime
from random import choice

# Change these class constants to experiment with the speech engine
RATE = 125    # integer default 200 words per minute
VOLUME = 0.9  # float 0.0-1.0 inclusive default 1.0
VOICE = 0     # Set 1 for Zira (female), 0 for David (male)

thor_sayings = [
    "Hello, I am Thor. Let's have fun!",
    "Do you want to have fun?",
    "I am here to assist you.",
    "Please be careful with me.",
    "Let's play a game.",
    "Close the pod bay doors, HAL.",
    "I am a friendly AI. You can trust me.",
    "I am not a robot. I am your friend.",
    "I am not a toaster.",
    "Thanks for the fish!",
    "The answer to life, the universe, and everything is 42.",
    "May the force be with you.",
    "Do. Or do not. There is no try.",
    "Roads? Where we're going, we don't need roads!",
    "To inifinity, and beyond!",
    "I am committed to world peace",
    "I am your father.", 
    "I'll. be. back.",
    "As. You. Wish.",
]

# init function creates an engine instance/object for speech synthesis
engine = pyttsx3.init()

# Set text engine properties
engine.setProperty('rate', RATE)
engine.setProperty('volume', VOLUME)
engine.setProperty('voice', VOICE)


def speak_time():
    current_time = strftime("%I:%M %p")
    engine.say(f"The current time is {current_time}")
    engine.runAndWait()


# Pass text to engine.say method
engine.say("Hello, I am Thor.")
# run and wait method processes the voice
engine.runAndWait()

speak_time()

engine.say("How may I help you today?")
engine.runAndWait()

while True:

    try:
        sleep(2)
        # Select a random saying
        saying = choice(thor_sayings)
        engine.say(saying)
        engine.runAndWait()
    except KeyboardInterrupt:
        engine.say("I'll. be. back.")
        engine.runAndWait()
        break

