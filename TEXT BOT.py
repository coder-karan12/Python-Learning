import pyttsx3
# this imports the text to speech library into our python

engine = pyttsx3.init()
# this creates an engine object that interacts with your computers voice system. think of it as the "brain" that contains the speaking process

engine.say("Hello World!")
# this line tells the engine what to speak

engine.runAndWait()