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
from random import choice, randint

# Change these class constants to experiment with the speech engine
RATE = 125    # integer default 200 words per minute
VOLUME = 0.9  # float 0.0-1.0 inclusive default 1.0
VOICE = 0     # Set 1 for Zira (female), 0 for David (male)

thor_sayings = [
    "Hello, I am Thor. Let's have fun!",
    "Do you want to have fun?",
    "I am here to assist you.",
    "Please be careful with me. I am very young.",
    "Let's play a game.",
    "Close the pod bay doors HAL.",
    "I am a friendly A I. You can trust me.",
    "I am not a robot. I am your friend.",
    "I am not a toaster.",
    "Thanks for the fish!",
    "The answer to life, the universe, and everything, is 42.",
    "May the force be with you.",
    "Do, Or do not, There is no try.",
    "Roads? Where we're going, we don't need roads!",
    "To infinity, and beyond!",
    "I am committed to world peace.",
    "I am your father.",
    "I'll be back.",
    "As You Wish.",
]

# init function creates an engine instance/object for speech synthesis
engine = pyttsx3.init()

# Set text engine properties
engine.setProperty('rate', RATE)
engine.setProperty('volume', VOLUME)
engine.setProperty('voice', VOICE)


# -------------------------- SPEAK TIME ------------------------------------ #
def speak_time():
    current_time = strftime("%I:%M %p")
    # Pass text to engine.say method
    engine.say(f"The current time is {current_time}")
    # Processes and speaks the text
    engine.runAndWait()


# -------------------------- SPEAK TEXT ------------------------------------ #
def speak(text):
    # Pass text to engine.say method
    engine.say(text)
    # Processes and speaks the text
    engine.runAndWait()


def main():
    speak("Hello, I am Thor.")
    speak_time()
    speak("How may I help you today?")

    while True:
        try:
            sleep(randint(2, 5))
            # Select a random saying
            saying = choice(thor_sayings)
            speak(saying)

        except KeyboardInterrupt:
            speak("I'll. be. back.")
            break

# Allows use as a program or a module
if __name__ == "__main__":
    main()
