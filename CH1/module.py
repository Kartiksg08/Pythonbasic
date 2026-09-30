#import pyjokes
#joke = pyjokes.get_joke()
#print(joke)

import pyttsx3

engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')
print(voices)

# Select voice
engine.setProperty('voice', voices[0].id)   # usually male
# engine.setProperty('voice', voices[1].id) # usually female

# Speak
engine.say("mach1")
engine.runAndWait()

import os

# Specify the directory
path = "/"

# Get the contents of the directory
contents = os.listdir(path)

# Print each item
for item in contents:
    print(item)


